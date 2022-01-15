from itertools import combinations
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import statsmodels.api as sm
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import GaussianNB
import pickle









def create_file_for_bet(file_name,model):
    fin = open(file_name,"r",encoding="utf-8")
    fout = open("modified_"+file_name,"w+",encoding="utf-8")
    fout.write("Sıra,Yaş,Ganyan,ModelOlasılık,OlmasıGerekenGanyan,PotansiyelKazanç"+" \n")
    line_list = []
    prob_array = []
    predict_array = []
    for line in fin:
        if line !="\n":
            line_list.append(line)
        else:
            line = next(fin)
            line = line.split(",")
            for x in line:
                predict_array.append(float(x))
    x = model.predict_proba([predict_array])
    prob_array = list(x[0])

    indx = 0
    for n_line in line_list:
        n_line = n_line.split(",")
        ganyan = float(n_line[len(n_line)-1].replace("\n",""))
        win_prop_of_horse = prob_array[indx]
        expected_money = 1 / float(win_prop_of_horse) 
        per_tl_profit = ganyan - expected_money
        n_line = str(n_line[0]) + "," + str(n_line[1]) + "," + str(n_line[2]) + "," + str(ganyan) + "," + str(win_prop_of_horse) + "," + str(expected_money) + "," + str(per_tl_profit) +"\n" 
        fout.write(n_line)
        indx = indx + 1
    return None






def trial():
    
    
    pkl = "vnm_t10.pkl"
    file_name ="2_10.txt"


    with open(pkl, 'rb') as file:
        pickle_model = pickle.load(file)
    
    
    #sample = [5,59,2,89,0.00011328877294522659,0.0,0.00011109425256988465,0.1626082251082251,0,0.11059371362048893,0.18,0.16911764705882354,0.6,0.2,0.6,17,10.15,6,59,5,69,0.00013297841509032665,-0.030980583626693533,0.00013238800944094056,0.3987373737373737,0,0.1341019417475728,0.09821428571428571,0.07964601769911504,0.13333333333333333,0.03333333333333333,0.13333333333333333,28,23.45,6,59,8,100,0.00013981052899431868,-0.025332122954649754,0.00013991514544234426,0.6805555555555556,0,0.1572673085740486,0.24183006535947713,0.16138328530259366,0.0967741935483871,0.06451612903225806,0.12903225806451613,18,27.25,6,59,6,104,0.0001168366724349727,-0.019122235128777865,0.0001161044467622651,0.6165674603174602,0,0.21634241245136188,0.11627906976744186,0.15020576131687244,0.0,0.06666666666666667,0.0,35,23.80,8,59,7,99,0.00011247538452613734,-0.009088085043781766,0.00011123334101747543,0.5099206349206349,0,0.16666666666666666,0.14426229508196722,0.13555555555555557,0.044444444444444446,0.022222222222222223,0.044444444444444446,24,15.65,7,59,3,81,0.00011689590098045905,-0.012858618813656984,0.00011651586792550687,0.7095238095238096,0,0.10224948875255624,0.06896551724137931,0.12781954887218044,0.08928571428571429,0.0,0.05357142857142857,17,33.70,5,59,4,86,0.00012366297562731404,-0.010920431788122562,0.0001215711000908918,0.47916666666666663,0,0.10576923076923077,0.09821428571428571,0.07964601769911504,0.25,0.03125,0.25,17,23.45,5,59,1,91,0.00011839853877304167,-0.008795008523380525,0.00011650364609473406,0.3625,0,0.2861610633307271,0.12579762989972654,0.11949685534591195,0.17857142857142858,0.03571428571428571,0.03571428571428571,24,7.10,5,59,10,105,0.00013147946788456298,-0.0012860389998803684,0.00012778685970206332,0.15476190476190477,0,0.2256198347107438,0.2159090909090909,0.1553398058252427,0.25,0.0,0.5357142857142857,35,1.05,9,59,9,83,0.00010300485852117543,-0.10430819619503852,0.0001105594249970595,0.96875,0,0.10251798561151079,0.14426229508196722,0.13555555555555557,0.1388888888888889,0.1111111111111111,0.1388888888888889,24,15.65]
    #x = pickle_model.predict_proba([sample])
    
    create_file_for_bet(file_name,pickle_model)
    


    return None


# son yarışı eofe diye kabul etmiyor


# \n e kadar git ondan sonraki satırı  öğrenmeye sok temiz bir formatta yaz
trial()
