import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import statsmodels.api as sm
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
import pickle
from sklearn.utils import shuffle
from keras import layers
from keras import models
from keras import optimizers
from keras import losses
from keras import metrics
from keras.layers import Dropout
from keras.layers import BatchNormalization
from keras.models import load_model


def log_reg(X_train, X_test, y_train, y_test):
    print("entered")
    model = LogisticRegression(solver='sag', multi_class='multinomial' ,verbose=1,max_iter=10000,n_jobs = -1)
    model.fit(X_train, y_train)
    print(model.score(X_test,y_test))
    return model


def nn_2(x_train, x_test, y_train, y_test):

    # split an additional validation dataset
    val_size = round(len(x_train) / 9)
    x_validation=x_train[:val_size]
    x_partial_train=x_train[val_size:]
    y_validation=y_train[:val_size]
    y_partial_train=y_train[val_size:]
    model=models.Sequential()
    model.add(layers.Dense(34,activation='relu',input_shape=(34,)))
    model.add(BatchNormalization())
    model.add(Dropout(0.2))
    model.add(layers.Dense(34,activation='relu'))
    model.add(BatchNormalization())
    model.add(Dropout(0.2))
    model.add(layers.Dense(1,activation='sigmoid'))
    model.compile(optimizer='sgd',loss='binary_crossentropy',metrics=['binary_accuracy'])
    model.fit(x_partial_train,y_partial_train,epochs=50,batch_size=512,validation_data=(x_validation,y_validation))
    print("score on test: " + str(model.evaluate(x_test,y_test)[1]))
    #print("score on train: "+ str(model.evaluate(x_train,y_train)[1]))
    
def nn_n(x_train, x_test, y_train, y_test,n):
    from keras import layers
    from keras import models
    from keras import optimizers
    from keras import losses
    from keras import metrics
    from keras.layers import Dropout
    from keras.layers import BatchNormalization
    ratio = 0.6
    # split an additional validation dataset
    val_size = round(len(x_train) / 9)
    x_validation=x_train[:val_size]
    x_partial_train=x_train[val_size:]
    y_validation=y_train[:val_size]
    y_partial_train=y_train[val_size:]
    model=models.Sequential()
    model.add(layers.Dense(round((n*17*ratio)+n),activation='relu',input_shape=(n * 17,)))
    model.add(BatchNormalization())
    model.add(Dropout(0.2))
    model.add(layers.Dense(round((n*17*ratio)+n),activation='relu'))
    model.add(BatchNormalization())
    model.add(Dropout(0.2))
    model.add(layers.Dense(n,activation='softmax'))
    model.compile(optimizer='sgd',loss='sparse_categorical_crossentropy',metrics=['acc'])
    model.fit(x_partial_train,y_partial_train,epochs=100,batch_size=512,validation_data=(x_validation,y_validation))
    print("score on test: " + str(model.evaluate(x_test,y_test)[1]))
    #print("score on train: "+ str(model.evaluate(x_train,y_train)[1]))   
   
    print(model.predict([[7,60,13,70,0.000119924641212853,-0.007777261600577668,0.0001172061808746975,0.4603625541125541,0,0.08591885441527446,0.12234042553191489,0.12158808933002481,0.1774193548387097,0.016129032258064516,0.1774193548387097,20,5.90,7,61.5,4,69,0.0001845300476531538,-0.013200418791833122,0.000182397826610376,0.49464285714285716,0,0.11932555123216602,0.06422018348623854,0.0703125,0.01818181818181818,0.01818181818181818,0.09090909090909091,15,6.80,5,61,11,66,0.0001750420437576001,-0.026634765665107044,0.00017563861089905916,0.6479166666666667,0,0.09343263371699391,0.06474820143884892,0.04854368932038835,0.1,0.025,0.15,8,17.75,6,59,7,66,0.00016533468700324894,-0.03520403857506699,0.00016596847563798723,0.6212121212121211,0,0.08414239482200647,0.07352941176470588,0.06976744186046512,0.027777777777777776,0.0,0.08333333333333333,32,20.20,7,58.1,3,66,0.00016109108453301032,-0.010326467648756565,0.00015816005519934866,0.4092365967365968,0,0.04,0.06993006993006994,0.11875,0.06666666666666667,0.044444444444444446,0.06666666666666667,69,10.80,11,57.5,5,65,0.00015570583223333695,-0.007909446546469264,0.000150719674660343,0.3392857142857143,0,0.04395604395604396,0.05387931034482758,0.0703125,0.025,0.075,0.05,13,12.35,8,59.5,10,63,0.00012767523855345935,-0.02276076645232587,0.0001275508619431634,0.6226481851481851,0,0.0546984572230014,0.2,0.16037735849056603,0.1111111111111111,0.022222222222222223,0.1111111111111111,20,15.65,5,57.5,6,59,0.00016014543485370843,-0.013557409500194384,0.00015789345123137717,0.3835497835497836,0,0.15244322092222987,0.19594594594594594,0.19130434782608696,0.038461538461538464,0.038461538461538464,0.07692307692307693,11,2.35,9,55.5,2,59,0.0001411688170346727,-0.0282152376043174,0.00014013674551857164,0.4625,0,0.045951859956236324,0.043478260869565216,0.02040816326530612,0.0,0.0,0.10256410256410256,7,18.90,6,56,8,56,0.0001429519319717356,-0.02170629551049861,0.00014259080200640094,0.5966880341880342,0,0.09882583170254403,0.0,0.08,0.0,0.0,0.0,19,11.05,7,50.8,12,51,0.00015497615735526047,-0.030782679873539633,0.0001535374847968495,0.5137867647058824,0,0.0390625,0.03333333333333333,0.04984423676012461,0.02857142857142857,0.0,0.02857142857142857,13,10.85,5,51.6,9,34,0.00012637141906610776,-0.06027393910857966,0.00012781792384607973,0.7413194444444444,0,0.04266958424507659,0.02,0.0,0.0,0.043478260869565216,0.043478260869565216,13,45.55,6,52.0,1,30,0.00015001030534795694,-0.015423677074507522,0.00014775557413839878,0.40646853146853146,0,0.04225352112676056,0.12093023255813953,0.14583333333333334,0.0,0.0,0.07142857142857142,23,11.30]]))
    return model
path_to_parsed_results8 = "C:\\Users\\AtakanPavilion\\Desktop\\Atakan\\01.Work\\projects\\horse_racing\\data\\race_results_parsed\\final.csv"
df = pd.read_csv(path_to_parsed_results8)
pkl_filename = "t13_model.pkl" 
n_way = 13

to_be_dropped = []
for a in range(13):
    to_be_dropped.append("sıra_"+str(a))


to_be_dropped = []
for a in range(n_way):
    to_be_dropped.append("sıra_"+str(a))


for a in to_be_dropped:
    del df[a]



X_list = []
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')
    df[col].fillna((df[col].mean()), inplace=True)
    if col !="win_bit":
        X_list.append(col)



#df =df[10000:]
df = shuffle(df)
y = df["win_bit"]
X = df[X_list]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

df = []

#model = log_reg(X_train, X_test, y_train, y_test) 
#model = nn_2(X_train, X_test, y_train, y_test)
model = nn_n(X_train, X_test, y_train, y_test,n_way)

model.save(str(n_way)+".h5")
#model = load_model('model.h5')

