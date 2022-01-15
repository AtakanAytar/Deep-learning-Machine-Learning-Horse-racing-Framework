
from itertools import combinations
import random

def drop_columns(line , col_list):
    if line !="\n":
        line = line.split(",")
        del line[1]
        del line[3]
        del line[3]
        del line[3]
        del line[3]
        del line[3]
        del line[4]
        del line[4]
        del line[4]
        del line[4]
        del line[4]
        del line[len(line)-1]
    for_bidden = ["[","]","'"," "]
    line = str(line)
    
    for char in for_bidden:
        line = line.replace(char , "")

    return line+"\n"

def re_write_check_correct(path_to_parsed_results5,path_to_parsed_results6,city,distance):
    fin = open(path_to_parsed_results5,"r",encoding="utf-8")
    fout = open(path_to_parsed_results6,"w+",encoding="utf-8")
    #fout.write("sıra_0,yaş_0,kilo_0,starting_position_0,handikap_0,normalized_time_for_horse_0,lengths_behind_winner_0,normalized_time_for_comp_0,avg_position_0,new_dist_0,jokey_win_rate_0,owner_win_rate_0,trainer_win_rate_0,city_pref_0,distance_pref_0,mat_pref_0,days_since_last_race_0,sıra_1,yaş_1,kilo_1,starting_position_1,handikap_1,normalized_time_for_horse_1,lengths_behind_winner_1,normalized_time_for_comp_1,avg_position_1,new_dist_1,jokey_win_rate_1,owner_win_rate_1,trainer_win_rate_1,city_pref_1,distance_pref_1,mat_pref_1,days_since_last_race_1\n")
    
    #next(fin)
    comma_no = 0
    lock = True
    prev_line = ""
    for line in fin:
        if lock:
            comma_no = line.count(",")
            lock = False


        if line.count("%") > 0:
            indx_s = line.find("%")
            indx_f = line.find(")")
            to_be_replaced = line[indx_s:indx_f+1]
            line = line.replace(to_be_replaced,"NULL")
        
        col_list = []
        
        if (line.count("pdfsonuçlar|özetpdfsonuçlar|") == 0 and line.count(",") == comma_no and line.count(city)>=1 and line.count(distance)>=1):
            
            # 2 \n  arka arkaya yazılamasın
           
            line = drop_columns(line,col_list)
            line_temp = line.split(",")
            
            if line_temp[0] =="1":
                fout.write("\n")
            
            fout.write(line)
        prev_line  = line
    fin.close()
    fout.close()
    return None

def return_colum_names(n):
    orj_str = "sıra_0,age_0,kilo_0,starting_position_0,handikap_0,normalized_time_for_horse_0,lengths_behind_winner_0,normalized_time_for_comp_0,avg_position_0,new_dist_0,jokey_win_rate_0,owner_win_rate_0,trainer_win_rate_0,city_pref_0,distance_pref_0,mat_pref_0,days_since_last_race_0,ganyan_0"
    final_Str =""
    for a in range(n):
        final_Str = final_Str + orj_str.replace(str(0),str(a)) + ","
    final_Str = final_Str + "win_bit\n"
    return final_Str

def take_n_way_combinations_and_parse(path_to_parsed_results6,n,bound):
    fin = open(path_to_parsed_results6,"r",encoding="utf-8")
    next(fin)
    total_comb = []
    two_way_comb = []
    temp_race_array = []
    
    line_no = 0
    for line in fin:
        print(line_no)
        line_no = line_no + 1
       
        if line !="\n":
            temp_race_array.append(line.replace("\n",""))
        else:          
            if   n + bound > len(temp_race_array) > n-1:
                two_way_comb = list(combinations(temp_race_array,n))
                total_comb = total_comb + two_way_comb 
                temp_race_array.clear()
            temp_race_array.clear()
      
            
            
    
    fin.close()
    return total_comb


def swap_and_write_to_a_file_2way(total_comb,outfile):
    fout = open(outfile,"w+",encoding="utf-8")
    fout.write("sıra_0,age_0,kilo_0,starting_position_0,handikap_0,normalized_time_for_horse_0,lengths_behind_winner_0,normalized_time_for_comp_0,avg_position_0,new_dist_0,jokey_win_rate_0,owner_win_rate_0,trainer_win_rate_0,city_pref_0,distance_pref_0,mat_pref_0,days_since_last_race_0,ganyan_0,sıra_1,age_1,kilo_1,starting_position_1,handikap_1,normalized_time_for_horse_1,lengths_behind_winner_1,normalized_time_for_comp_1,avg_position_1,new_dist_1,jokey_win_rate_1,owner_win_rate_1,trainer_win_rate_1,city_pref_1,distance_pref_1,mat_pref_1,days_since_last_race_1,ganyan_1,win_bit\n")
    count_for_odd = 0
    for a in total_comb:
        count_for_odd = count_for_odd % 2

        if count_for_odd == 0:
            line = a[0] + "," + a[1] + ",0\n"
            fout.write(line.replace("NULL", "NaN"))
            
        else:
            line = a[1] + "," + a[0] + ",1\n"
            fout.write(line.replace("NULL", "NaN"))
        
        count_for_odd = count_for_odd + 1
    fout.close()
    return None

def swap_and_write_to_a_file_4way(total_comb,outfile):
    fout = open(outfile,"w+",encoding="utf-8")
    fout.write("sıra_0,age_0,kilo_0,starting_position_0,handikap_0,normalized_time_for_horse_0,lengths_behind_winner_0,normalized_time_for_comp_0,avg_position_0,new_dist_0,jokey_win_rate_0,owner_win_rate_0,trainer_win_rate_0,city_pref_0,distance_pref_0,mat_pref_0,days_since_last_race_0,ganyan_0,sıra_1,age_1,kilo_1,starting_position_1,handikap_1,normalized_time_for_horse_1,lengths_behind_winner_1,normalized_time_for_comp_1,avg_position_1,new_dist_1,jokey_win_rate_1,owner_win_rate_1,trainer_win_rate_1,city_pref_1,distance_pref_1,mat_pref_1,days_since_last_race_1,ganyan_1,sıra_2,age_2,kilo_2,starting_position_2,handikap_2,normalized_time_for_horse_2,lengths_behind_winner_2,normalized_time_for_comp_2,avg_position_2,new_dist_2,jokey_win_rate_2,owner_win_rate_2,trainer_win_rate_2,city_pref_2,distance_pref_2,mat_pref_2,days_since_last_race_2,ganyan_2,sıra_3,age_3,kilo_3,starting_position_3,handikap_3,normalized_time_for_horse_3,lengths_behind_winner_3,normalized_time_for_comp_3,avg_position_3,new_dist_3,jokey_win_rate_3,owner_win_rate_3,trainer_win_rate_3,city_pref_3,distance_pref_3,mat_pref_3,days_since_last_race_3,ganyan_3,win_bit\n")
    count_for_odd = 0
    for a in total_comb:
        count_for_odd = count_for_odd % 4

        if count_for_odd == 0:
            line = a[0] + "," + a[1] +","+a[2] + "," + a[3]  + ",0\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd == 1:
            line = a[1] + "," + a[0] +","+a[2] + "," + a[3]  + ",1\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==2:
            line = a[2] + "," + a[1] +","+a[0] + "," + a[3]  + ",2\n"
            fout.write(line.replace("NULL", "NaN"))
        else:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[0]  + ",3\n"
            fout.write(line.replace("NULL", "NaN"))
        count_for_odd = count_for_odd + 1
    fout.close()
    return None
def swap_and_write_to_a_file_5way(total_comb,outfile):
    fout = open(outfile,"w+",encoding="utf-8")
    fout.write("sıra_0,age_0,kilo_0,starting_position_0,handikap_0,normalized_time_for_horse_0,lengths_behind_winner_0,normalized_time_for_comp_0,avg_position_0,new_dist_0,jokey_win_rate_0,owner_win_rate_0,trainer_win_rate_0,city_pref_0,distance_pref_0,mat_pref_0,days_since_last_race_0,ganyan_0,sıra_1,age_1,kilo_1,starting_position_1,handikap_1,normalized_time_for_horse_1,lengths_behind_winner_1,normalized_time_for_comp_1,avg_position_1,new_dist_1,jokey_win_rate_1,owner_win_rate_1,trainer_win_rate_1,city_pref_1,distance_pref_1,mat_pref_1,days_since_last_race_1,ganyan_1,sıra_2,age_2,kilo_2,starting_position_2,handikap_2,normalized_time_for_horse_2,lengths_behind_winner_2,normalized_time_for_comp_2,avg_position_2,new_dist_2,jokey_win_rate_2,owner_win_rate_2,trainer_win_rate_2,city_pref_2,distance_pref_2,mat_pref_2,days_since_last_race_2,ganyan_2,sıra_3,age_3,kilo_3,starting_position_3,handikap_3,normalized_time_for_horse_3,lengths_behind_winner_3,normalized_time_for_comp_3,avg_position_3,new_dist_3,jokey_win_rate_3,owner_win_rate_3,trainer_win_rate_3,city_pref_3,distance_pref_3,mat_pref_3,days_since_last_race_3,ganyan_3,sıra_4,age_4,kilo_4,starting_position_4,handikap_4,normalized_time_for_horse_4,lengths_behind_winner_4,normalized_time_for_comp_4,avg_position_4,new_dist_4,jokey_win_rate_4,owner_win_rate_4,trainer_win_rate_4,city_pref_4,distance_pref_4,mat_pref_4,days_since_last_race_4,ganyan_4,win_bit\n")
    count_for_odd = 0
    for a in total_comb:
        count_for_odd = count_for_odd % 5

        if count_for_odd == 0:
            line = a[0] + "," + a[1] +","+a[2] + "," + a[3] +","+ a[4] + ",0\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd == 1:
            line = a[1] + "," + a[0] +","+a[2] + "," + a[3]  + ","+ a[4] + ",1\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==2:
            line = a[2] + "," + a[1] +","+a[0] + "," + a[3]  + ","+ a[4] + ",2\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==3:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[0]  + "," + a[4]  + ",3\n"
            fout.write(line.replace("NULL", "NaN"))
        else:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[0] + ",4\n"
            fout.write(line.replace("NULL", "NaN"))
        count_for_odd = count_for_odd + 1
    fout.close()
    return None
def swap_and_write_to_a_file_6way(total_comb,outfile):
    fout = open(outfile,"w+",encoding="utf-8")
    fout.write("sıra_0,age_0,kilo_0,starting_position_0,handikap_0,normalized_time_for_horse_0,lengths_behind_winner_0,normalized_time_for_comp_0,avg_position_0,new_dist_0,jokey_win_rate_0,owner_win_rate_0,trainer_win_rate_0,city_pref_0,distance_pref_0,mat_pref_0,days_since_last_race_0,ganyan_0,sıra_1,age_1,kilo_1,starting_position_1,handikap_1,normalized_time_for_horse_1,lengths_behind_winner_1,normalized_time_for_comp_1,avg_position_1,new_dist_1,jokey_win_rate_1,owner_win_rate_1,trainer_win_rate_1,city_pref_1,distance_pref_1,mat_pref_1,days_since_last_race_1,ganyan_1,sıra_2,age_2,kilo_2,starting_position_2,handikap_2,normalized_time_for_horse_2,lengths_behind_winner_2,normalized_time_for_comp_2,avg_position_2,new_dist_2,jokey_win_rate_2,owner_win_rate_2,trainer_win_rate_2,city_pref_2,distance_pref_2,mat_pref_2,days_since_last_race_2,ganyan_2,sıra_3,age_3,kilo_3,starting_position_3,handikap_3,normalized_time_for_horse_3,lengths_behind_winner_3,normalized_time_for_comp_3,avg_position_3,new_dist_3,jokey_win_rate_3,owner_win_rate_3,trainer_win_rate_3,city_pref_3,distance_pref_3,mat_pref_3,days_since_last_race_3,ganyan_3,sıra_4,age_4,kilo_4,starting_position_4,handikap_4,normalized_time_for_horse_4,lengths_behind_winner_4,normalized_time_for_comp_4,avg_position_4,new_dist_4,jokey_win_rate_4,owner_win_rate_4,trainer_win_rate_4,city_pref_4,distance_pref_4,mat_pref_4,days_since_last_race_4,ganyan_4,sıra_5,age_5,kilo_5,starting_position_5,handikap_5,normalized_time_for_horse_5,lengths_behind_winner_5,normalized_time_for_comp_5,avg_position_5,new_dist_5,jokey_win_rate_5,owner_win_rate_5,trainer_win_rate_5,city_pref_5,distance_pref_5,mat_pref_5,days_since_last_race_5,ganyan_5,win_bit\n")
    count_for_odd = 0
    for a in total_comb:
        count_for_odd = count_for_odd % 6

        if count_for_odd == 0:
            line = a[0] + "," + a[1] +","+a[2] + "," + a[3] +","+ a[4] + ","+ a[5] + ",0\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd == 1:
            line = a[1] + "," + a[0] +","+a[2] + "," + a[3]  + ","+ a[4] + ","+ a[5] + ",1\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==2:
            line = a[2] + "," + a[1] +","+a[0] + "," + a[3]  + ","+ a[4] + ","+ a[5] + ",2\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==3:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[0]  + "," + a[4]  + ","+ a[5] + ",3\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==4:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[0] + ","+ a[5] + ",4\n"
            fout.write(line.replace("NULL", "NaN"))
        else:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[0] + ",5\n"
            fout.write(line.replace("NULL", "NaN"))

        count_for_odd = count_for_odd + 1
    fout.close()
    return None
def swap_and_write_to_a_file_7way(total_comb,outfile):
    fout = open(outfile,"w+",encoding="utf-8")
    fout.write("sıra_0,age_0,kilo_0,starting_position_0,handikap_0,normalized_time_for_horse_0,lengths_behind_winner_0,normalized_time_for_comp_0,avg_position_0,new_dist_0,jokey_win_rate_0,owner_win_rate_0,trainer_win_rate_0,city_pref_0,distance_pref_0,mat_pref_0,days_since_last_race_0,ganyan_0,sıra_1,age_1,kilo_1,starting_position_1,handikap_1,normalized_time_for_horse_1,lengths_behind_winner_1,normalized_time_for_comp_1,avg_position_1,new_dist_1,jokey_win_rate_1,owner_win_rate_1,trainer_win_rate_1,city_pref_1,distance_pref_1,mat_pref_1,days_since_last_race_1,ganyan_1,sıra_2,age_2,kilo_2,starting_position_2,handikap_2,normalized_time_for_horse_2,lengths_behind_winner_2,normalized_time_for_comp_2,avg_position_2,new_dist_2,jokey_win_rate_2,owner_win_rate_2,trainer_win_rate_2,city_pref_2,distance_pref_2,mat_pref_2,days_since_last_race_2,ganyan_2,sıra_3,age_3,kilo_3,starting_position_3,handikap_3,normalized_time_for_horse_3,lengths_behind_winner_3,normalized_time_for_comp_3,avg_position_3,new_dist_3,jokey_win_rate_3,owner_win_rate_3,trainer_win_rate_3,city_pref_3,distance_pref_3,mat_pref_3,days_since_last_race_3,ganyan_3,sıra_4,age_4,kilo_4,starting_position_4,handikap_4,normalized_time_for_horse_4,lengths_behind_winner_4,normalized_time_for_comp_4,avg_position_4,new_dist_4,jokey_win_rate_4,owner_win_rate_4,trainer_win_rate_4,city_pref_4,distance_pref_4,mat_pref_4,days_since_last_race_4,ganyan_4,sıra_5,age_5,kilo_5,starting_position_5,handikap_5,normalized_time_for_horse_5,lengths_behind_winner_5,normalized_time_for_comp_5,avg_position_5,new_dist_5,jokey_win_rate_5,owner_win_rate_5,trainer_win_rate_5,city_pref_5,distance_pref_5,mat_pref_5,days_since_last_race_5,ganyan_5,sıra_6,age_6,kilo_6,starting_position_6,handikap_6,normalized_time_for_horse_6,lengths_behind_winner_6,normalized_time_for_comp_6,avg_position_6,new_dist_6,jokey_win_rate_6,owner_win_rate_6,trainer_win_rate_6,city_pref_6,distance_pref_6,mat_pref_6,days_since_last_race_6,ganyan_6,win_bit\n")
    count_for_odd = 0
    for a in total_comb:
        count_for_odd = count_for_odd % 7

        if count_for_odd == 0:
            line = a[0] + "," + a[1] +","+a[2] + "," + a[3] +","+ a[4] + ","+ a[5] + "," + a[6] +  ",0\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd == 1:
            line = a[1] + "," + a[0] +","+a[2] + "," + a[3]  + ","+ a[4] + ","+ a[5] + ","+ a[6] + ",1\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==2:
            line = a[2] + "," + a[1] +","+a[0] + "," + a[3]  + ","+ a[4] + ","+ a[5] + ","+ a[6] + ",2\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==3:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[0]  + "," + a[4]  + ","+ a[5] + ","+ a[6] + ",3\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==4:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[0] + ","+ a[5] + ","+ a[6] + ",4\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==5:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[0] + ","+ a[6] + ",5\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd == 6:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[6] + ","+ a[0] + ",6\n"
            fout.write(line.replace("NULL", "NaN"))
        count_for_odd = count_for_odd + 1
    fout.close()
    return None
def swap_and_write_to_a_file_8way(total_comb,outfile):
    fout = open(outfile,"w+",encoding="utf-8")
    fout.write("sıra_0,age_0,kilo_0,starting_position_0,handikap_0,normalized_time_for_horse_0,lengths_behind_winner_0,normalized_time_for_comp_0,avg_position_0,new_dist_0,jokey_win_rate_0,owner_win_rate_0,trainer_win_rate_0,city_pref_0,distance_pref_0,mat_pref_0,days_since_last_race_0,ganyan_0,sıra_1,age_1,kilo_1,starting_position_1,handikap_1,normalized_time_for_horse_1,lengths_behind_winner_1,normalized_time_for_comp_1,avg_position_1,new_dist_1,jokey_win_rate_1,owner_win_rate_1,trainer_win_rate_1,city_pref_1,distance_pref_1,mat_pref_1,days_since_last_race_1,ganyan_1,sıra_2,age_2,kilo_2,starting_position_2,handikap_2,normalized_time_for_horse_2,lengths_behind_winner_2,normalized_time_for_comp_2,avg_position_2,new_dist_2,jokey_win_rate_2,owner_win_rate_2,trainer_win_rate_2,city_pref_2,distance_pref_2,mat_pref_2,days_since_last_race_2,ganyan_2,sıra_3,age_3,kilo_3,starting_position_3,handikap_3,normalized_time_for_horse_3,lengths_behind_winner_3,normalized_time_for_comp_3,avg_position_3,new_dist_3,jokey_win_rate_3,owner_win_rate_3,trainer_win_rate_3,city_pref_3,distance_pref_3,mat_pref_3,days_since_last_race_3,ganyan_3,sıra_4,age_4,kilo_4,starting_position_4,handikap_4,normalized_time_for_horse_4,lengths_behind_winner_4,normalized_time_for_comp_4,avg_position_4,new_dist_4,jokey_win_rate_4,owner_win_rate_4,trainer_win_rate_4,city_pref_4,distance_pref_4,mat_pref_4,days_since_last_race_4,ganyan_4,sıra_5,age_5,kilo_5,starting_position_5,handikap_5,normalized_time_for_horse_5,lengths_behind_winner_5,normalized_time_for_comp_5,avg_position_5,new_dist_5,jokey_win_rate_5,owner_win_rate_5,trainer_win_rate_5,city_pref_5,distance_pref_5,mat_pref_5,days_since_last_race_5,ganyan_5,sıra_6,age_6,kilo_6,starting_position_6,handikap_6,normalized_time_for_horse_6,lengths_behind_winner_6,normalized_time_for_comp_6,avg_position_6,new_dist_6,jokey_win_rate_6,owner_win_rate_6,trainer_win_rate_6,city_pref_6,distance_pref_6,mat_pref_6,days_since_last_race_6,ganyan_6,sıra_7,age_7,kilo_7,starting_position_7,handikap_7,normalized_time_for_horse_7,lengths_behind_winner_7,normalized_time_for_comp_7,avg_position_7,new_dist_7,jokey_win_rate_7,owner_win_rate_7,trainer_win_rate_7,city_pref_7,distance_pref_7,mat_pref_7,days_since_last_race_7,ganyan_7,win_bit\n")
    count_for_odd = 0
    for a in total_comb:
        count_for_odd = count_for_odd % 8

        if count_for_odd == 0:
            line = a[0] + "," + a[1] +","+a[2] + "," + a[3] +","+ a[4] + ","+ a[5] + "," + a[6] + "," + a[7] + ",0\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd == 1:
            line = a[1] + "," + a[0] +","+a[2] + "," + a[3]  + ","+ a[4] + ","+ a[5] + ","+ a[6] + "," + a[7] + ",1\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==2:
            line = a[2] + "," + a[1] +","+a[0] + "," + a[3]  + ","+ a[4] + ","+ a[5] + ","+ a[6] + "," + a[7] + ",2\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==3:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[0]  + "," + a[4]  + ","+ a[5] + ","+ a[6] + "," + a[7] + ",3\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==4:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[0] + ","+ a[5] + ","+ a[6] + "," + a[7] + ",4\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==5:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[0] + ","+ a[6] + "," + a[7] + ",5\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd == 6:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[6] + ","+ a[0] + "," + a[7] + ",6\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd == 7 :
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[6] + ","+ a[7] + "," + a[0] + ", 7\n"
            fout.write(line.replace("NULL", "NaN"))
        count_for_odd = count_for_odd + 1
    fout.close()
    return None
def swap_and_write_to_a_file_9way(total_comb,outfile):
    fout = open(outfile,"w+",encoding="utf-8")
    fout.write("sıra_0,age_0,kilo_0,starting_position_0,handikap_0,normalized_time_for_horse_0,lengths_behind_winner_0,normalized_time_for_comp_0,avg_position_0,new_dist_0,jokey_win_rate_0,owner_win_rate_0,trainer_win_rate_0,city_pref_0,distance_pref_0,mat_pref_0,days_since_last_race_0,ganyan_0,sıra_1,age_1,kilo_1,starting_position_1,handikap_1,normalized_time_for_horse_1,lengths_behind_winner_1,normalized_time_for_comp_1,avg_position_1,new_dist_1,jokey_win_rate_1,owner_win_rate_1,trainer_win_rate_1,city_pref_1,distance_pref_1,mat_pref_1,days_since_last_race_1,ganyan_1,sıra_2,age_2,kilo_2,starting_position_2,handikap_2,normalized_time_for_horse_2,lengths_behind_winner_2,normalized_time_for_comp_2,avg_position_2,new_dist_2,jokey_win_rate_2,owner_win_rate_2,trainer_win_rate_2,city_pref_2,distance_pref_2,mat_pref_2,days_since_last_race_2,ganyan_2,sıra_3,age_3,kilo_3,starting_position_3,handikap_3,normalized_time_for_horse_3,lengths_behind_winner_3,normalized_time_for_comp_3,avg_position_3,new_dist_3,jokey_win_rate_3,owner_win_rate_3,trainer_win_rate_3,city_pref_3,distance_pref_3,mat_pref_3,days_since_last_race_3,ganyan_3,sıra_4,age_4,kilo_4,starting_position_4,handikap_4,normalized_time_for_horse_4,lengths_behind_winner_4,normalized_time_for_comp_4,avg_position_4,new_dist_4,jokey_win_rate_4,owner_win_rate_4,trainer_win_rate_4,city_pref_4,distance_pref_4,mat_pref_4,days_since_last_race_4,ganyan_4,sıra_5,age_5,kilo_5,starting_position_5,handikap_5,normalized_time_for_horse_5,lengths_behind_winner_5,normalized_time_for_comp_5,avg_position_5,new_dist_5,jokey_win_rate_5,owner_win_rate_5,trainer_win_rate_5,city_pref_5,distance_pref_5,mat_pref_5,days_since_last_race_5,ganyan_5,sıra_6,age_6,kilo_6,starting_position_6,handikap_6,normalized_time_for_horse_6,lengths_behind_winner_6,normalized_time_for_comp_6,avg_position_6,new_dist_6,jokey_win_rate_6,owner_win_rate_6,trainer_win_rate_6,city_pref_6,distance_pref_6,mat_pref_6,days_since_last_race_6,ganyan_6,sıra_7,age_7,kilo_7,starting_position_7,handikap_7,normalized_time_for_horse_7,lengths_behind_winner_7,normalized_time_for_comp_7,avg_position_7,new_dist_7,jokey_win_rate_7,owner_win_rate_7,trainer_win_rate_7,city_pref_7,distance_pref_7,mat_pref_7,days_since_last_race_7,ganyan_7,sıra_8,age_8,kilo_8,starting_position_8,handikap_8,normalized_time_for_horse_8,lengths_behind_winner_8,normalized_time_for_comp_8,avg_position_8,new_dist_8,jokey_win_rate_8,owner_win_rate_8,trainer_win_rate_8,city_pref_8,distance_pref_8,mat_pref_8,days_since_last_race_8,ganyan_8,win_bit\n")
    count_for_odd = 0
    for a in total_comb:
        count_for_odd = count_for_odd % 9

        if count_for_odd == 0:
            line = a[0] + "," + a[1] +","+a[2] + "," + a[3] +","+ a[4] + ","+ a[5] + "," + a[6] + "," + a[7] + "," +a[8] + ",0\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd == 1:
            line = a[1] + "," + a[0] +","+a[2] + "," + a[3]  + ","+ a[4] + ","+ a[5] + ","+ a[6] + "," + a[7] + "," +a[8] + ",1\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==2:
            line = a[2] + "," + a[1] +","+a[0] + "," + a[3]  + ","+ a[4] + ","+ a[5] + ","+ a[6] + "," + a[7] + "," +a[8] + ",2\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==3:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[0]  + "," + a[4]  + ","+ a[5] + ","+ a[6] + "," + a[7] + "," +a[8] + ",3\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==4:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[0] + ","+ a[5] + ","+ a[6] + "," + a[7] + "," +a[8] +  ",4\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==5:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[0] + ","+ a[6] + "," + a[7] + "," +a[8] + ",5\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd == 6:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[6] + ","+ a[0] + "," + a[7] + "," +a[8] + ",6\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd == 7 :
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[6] + ","+ a[7] + "," + a[0] + "," +a[8] + ",7\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==8:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[6] + ","+ a[7] + "," + a[8] + "," +a[0] + ",8\n"
            fout.write(line.replace("NULL", "NaN"))
        count_for_odd = count_for_odd + 1
    fout.close()
    return None
def swap_and_write_to_a_file_10way(total_comb,outfile):
    fout = open(outfile,"w+",encoding="utf-8")
    fout.write("sıra_0,age_0,kilo_0,starting_position_0,handikap_0,normalized_time_for_horse_0,lengths_behind_winner_0,normalized_time_for_comp_0,avg_position_0,new_dist_0,jokey_win_rate_0,owner_win_rate_0,trainer_win_rate_0,city_pref_0,distance_pref_0,mat_pref_0,days_since_last_race_0,ganyan_0,sıra_1,age_1,kilo_1,starting_position_1,handikap_1,normalized_time_for_horse_1,lengths_behind_winner_1,normalized_time_for_comp_1,avg_position_1,new_dist_1,jokey_win_rate_1,owner_win_rate_1,trainer_win_rate_1,city_pref_1,distance_pref_1,mat_pref_1,days_since_last_race_1,ganyan_1,sıra_2,age_2,kilo_2,starting_position_2,handikap_2,normalized_time_for_horse_2,lengths_behind_winner_2,normalized_time_for_comp_2,avg_position_2,new_dist_2,jokey_win_rate_2,owner_win_rate_2,trainer_win_rate_2,city_pref_2,distance_pref_2,mat_pref_2,days_since_last_race_2,ganyan_2,sıra_3,age_3,kilo_3,starting_position_3,handikap_3,normalized_time_for_horse_3,lengths_behind_winner_3,normalized_time_for_comp_3,avg_position_3,new_dist_3,jokey_win_rate_3,owner_win_rate_3,trainer_win_rate_3,city_pref_3,distance_pref_3,mat_pref_3,days_since_last_race_3,ganyan_3,sıra_4,age_4,kilo_4,starting_position_4,handikap_4,normalized_time_for_horse_4,lengths_behind_winner_4,normalized_time_for_comp_4,avg_position_4,new_dist_4,jokey_win_rate_4,owner_win_rate_4,trainer_win_rate_4,city_pref_4,distance_pref_4,mat_pref_4,days_since_last_race_4,ganyan_4,sıra_5,age_5,kilo_5,starting_position_5,handikap_5,normalized_time_for_horse_5,lengths_behind_winner_5,normalized_time_for_comp_5,avg_position_5,new_dist_5,jokey_win_rate_5,owner_win_rate_5,trainer_win_rate_5,city_pref_5,distance_pref_5,mat_pref_5,days_since_last_race_5,ganyan_5,sıra_6,age_6,kilo_6,starting_position_6,handikap_6,normalized_time_for_horse_6,lengths_behind_winner_6,normalized_time_for_comp_6,avg_position_6,new_dist_6,jokey_win_rate_6,owner_win_rate_6,trainer_win_rate_6,city_pref_6,distance_pref_6,mat_pref_6,days_since_last_race_6,ganyan_6,sıra_7,age_7,kilo_7,starting_position_7,handikap_7,normalized_time_for_horse_7,lengths_behind_winner_7,normalized_time_for_comp_7,avg_position_7,new_dist_7,jokey_win_rate_7,owner_win_rate_7,trainer_win_rate_7,city_pref_7,distance_pref_7,mat_pref_7,days_since_last_race_7,ganyan_7,sıra_8,age_8,kilo_8,starting_position_8,handikap_8,normalized_time_for_horse_8,lengths_behind_winner_8,normalized_time_for_comp_8,avg_position_8,new_dist_8,jokey_win_rate_8,owner_win_rate_8,trainer_win_rate_8,city_pref_8,distance_pref_8,mat_pref_8,days_since_last_race_8,ganyan_8,sıra_9,age_9,kilo_9,starting_position_9,handikap_9,normalized_time_for_horse_9,lengths_behind_winner_9,normalized_time_for_comp_9,avg_position_9,new_dist_9,jokey_win_rate_9,owner_win_rate_9,trainer_win_rate_9,city_pref_9,distance_pref_9,mat_pref_9,days_since_last_race_9,ganyan_9,win_bit\n")
    count_for_odd = 0
    for a in total_comb:
        count_for_odd = count_for_odd % 10

        if count_for_odd == 0:
            line = a[0] + "," + a[1] +","+a[2] + "," + a[3] +","+ a[4] + ","+ a[5] + "," + a[6] + "," + a[7] + "," +a[8] + ","+a[9] + ",0\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd == 1:
            line = a[1] + "," + a[0] +","+a[2] + "," + a[3]  + ","+ a[4] + ","+ a[5] + ","+ a[6] + "," + a[7] + "," +a[8] + ","+a[9] + ",1\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==2:
            line = a[2] + "," + a[1] +","+a[0] + "," + a[3]  + ","+ a[4] + ","+ a[5] + ","+ a[6] + "," + a[7] + "," +a[8] + ","+a[9] +",2\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==3:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[0]  + "," + a[4]  + ","+ a[5] + ","+ a[6] + "," + a[7] + "," +a[8] + ","+a[9] + ",3\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==4:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[0] + ","+ a[5] + ","+ a[6] + "," + a[7] + "," +a[8] + ","+a[9] + ",4\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==5:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[0] + ","+ a[6] + "," + a[7] + "," +a[8] + ","+a[9] + ",5\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd == 6:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[6] + ","+ a[0] + "," + a[7] + "," +a[8] + ","+a[9] + ",6\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd == 7 :
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[6] + ","+ a[7] + "," + a[0] + "," +a[8] +  ","+a[9] + ",7\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==8:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[6] + ","+ a[7] + "," + a[8] + "," +a[0] +  ","+a[9] +",8\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==9:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[6] + ","+ a[7] + "," + a[8] + "," +a[9] +  ","+a[0] +",9\n"
            fout.write(line.replace("NULL", "NaN"))
        count_for_odd = count_for_odd + 1
    fout.close()
    return None
def swap_and_write_to_a_file_11way(total_comb,outfile):
    fout = open(outfile,"w+",encoding="utf-8")
    
    final_Str = return_colum_names(11)
    fout.write(final_Str)

    count_for_odd = 0
    for a in total_comb:
        count_for_odd = count_for_odd % 11

        if count_for_odd == 0:
            line = a[0] + "," + a[1] +","+a[2] + "," + a[3] +","+ a[4] + ","+ a[5] + "," + a[6] + "," + a[7] + "," +a[8] + ","+a[9] + ","+a[10] + ",0\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd == 1:
            line = a[1] + "," + a[0] +","+a[2] + "," + a[3]  + ","+ a[4] + ","+ a[5] + ","+ a[6] + "," + a[7] + "," +a[8] + ","+a[9] + ","+a[10] + ",1\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==2:
            line = a[2] + "," + a[1] +","+a[0] + "," + a[3]  + ","+ a[4] + ","+ a[5] + ","+ a[6] + "," + a[7] + "," +a[8] + ","+a[9] + ","+a[10] +",2\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==3:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[0]  + "," + a[4]  + ","+ a[5] + ","+ a[6] + "," + a[7] + "," +a[8] + ","+a[9] + ","+a[10] + ",3\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==4:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[0] + ","+ a[5] + ","+ a[6] + "," + a[7] + "," +a[8] + ","+a[9] + ","+a[10] + ",4\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==5:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[0] + ","+ a[6] + "," + a[7] + "," +a[8] + ","+a[9] + ","+a[10] + ",5\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd == 6:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[6] + ","+ a[0] + "," + a[7] + "," +a[8] + ","+a[9] + ","+a[10] + ",6\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd == 7 :
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[6] + ","+ a[7] + "," + a[0] + "," +a[8] +  ","+a[9] + ","+a[10] + ",7\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==8:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[6] + ","+ a[7] + "," + a[8] + "," +a[0] +  ","+a[9] + ","+a[10] +",8\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==9:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[6] + ","+ a[7] + "," + a[8] + "," +a[9] +  ","+a[0] + ","+a[10] +",9\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==10:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[6] + ","+ a[7] + "," + a[8] + "," +a[9] +  ","+a[10] + "," + a[0] +",10\n"
            fout.write(line.replace("NULL", "NaN"))
        count_for_odd = count_for_odd + 1

    fout.close
    return None    
def swap_and_write_to_a_file_12way(total_comb,outfile):
    fout = open(outfile,"w+",encoding="utf-8")
    
    final_Str = return_colum_names(12)
    fout.write(final_Str)

    count_for_odd = 0
    for a in total_comb:
        count_for_odd = count_for_odd % 12
        
        if count_for_odd == 0:
            line = a[0] + "," + a[1] +","+a[2] + "," + a[3] +","+ a[4] + ","+ a[5] + "," + a[6] + "," + a[7] + "," +a[8] + ","+a[9] + ","+a[10] + ","+a[11] + ",0\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd == 1:
            line = a[1] + "," + a[0] +","+a[2] + "," + a[3]  + ","+ a[4] + ","+ a[5] + ","+ a[6] + "," + a[7] + "," +a[8] + ","+a[9] + ","+a[10] + ","+a[11] + ",1\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==2:
            line = a[2] + "," + a[1] +","+a[0] + "," + a[3]  + ","+ a[4] + ","+ a[5] + ","+ a[6] + "," + a[7] + "," +a[8] + ","+a[9] + ","+a[10] + ","+a[11] + ",2\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==3:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[0]  + "," + a[4]  + ","+ a[5] + ","+ a[6] + "," + a[7] + "," +a[8] + ","+a[9] + ","+a[10] + ","+a[11] + ",3\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==4:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[0] + ","+ a[5] + ","+ a[6] + "," + a[7] + "," +a[8] + ","+a[9] + ","+a[10] + ","+a[11] + ",4\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==5:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[0] + ","+ a[6] + "," + a[7] + "," +a[8] + ","+a[9] + ","+a[10] + ","+a[11] + ",5\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd == 6:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[6] + ","+ a[0] + "," + a[7] + "," +a[8] + ","+a[9] + ","+a[10] + ","+a[11] + ",6\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd == 7 :
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[6] + ","+ a[7] + "," + a[0] + "," +a[8] +  ","+a[9] + ","+a[10] + ","+a[11] + ",7\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==8:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[6] + ","+ a[7] + "," + a[8] + "," +a[0] +  ","+a[9] + ","+a[10] + ","+a[11] +",8\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==9:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[6] + ","+ a[7] + "," + a[8] + "," +a[9] +  ","+a[0] + ","+a[10] + ","+a[11] + ",9\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==10:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[6] + ","+ a[7] + "," + a[8] + "," +a[9] +  ","+a[10] + "," + a[0] + "," +a[11] + ",10\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==11:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[6] + ","+ a[7] + "," + a[8] + "," +a[9] +  ","+a[10] + "," + a[11] + "," +a[0] + ",11\n"
            fout.write(line.replace("NULL", "NaN"))
        count_for_odd = count_for_odd + 1

    fout.close
    return None
def swap_and_write_to_a_file_13way(total_comb,outfile):
    fout = open(outfile,"w+",encoding="utf-8")
    
    final_Str = return_colum_names(13)
    fout.write(final_Str)

    count_for_odd = 0
    for a in total_comb:
        count_for_odd = count_for_odd % 13
        
        if count_for_odd == 0:
            line = a[0] + "," + a[1] +","+a[2] + "," + a[3] +","+ a[4] + ","+ a[5] + "," + a[6] + "," + a[7] + "," +a[8] + ","+a[9] + ","+a[10] + ","+a[11] + ","+a[12] + ",0\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd == 1:
            line = a[1] + "," + a[0] +","+a[2] + "," + a[3]  + ","+ a[4] + ","+ a[5] + ","+ a[6] + "," + a[7] + "," +a[8] + ","+a[9] + ","+a[10] + ","+a[11] + ","+a[12] + ",1\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==2:
            line = a[2] + "," + a[1] +","+a[0] + "," + a[3]  + ","+ a[4] + ","+ a[5] + ","+ a[6] + "," + a[7] + "," +a[8] + ","+a[9] + ","+a[10] + ","+a[11] + ","+a[12] + ",2\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==3:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[0]  + "," + a[4]  + ","+ a[5] + ","+ a[6] + "," + a[7] + "," +a[8] + ","+a[9] + ","+a[10] + ","+a[11] + ","+a[12] + ",3\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==4:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[0] + ","+ a[5] + ","+ a[6] + "," + a[7] + "," +a[8] + ","+a[9] + ","+a[10] + ","+a[11] + ","+a[12] + ",4\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==5:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[0] + ","+ a[6] + "," + a[7] + "," +a[8] + ","+a[9] + ","+a[10] + ","+a[11] + ","+a[12] + ",5\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd == 6:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[6] + ","+ a[0] + "," + a[7] + "," +a[8] + ","+a[9] + ","+a[10] + ","+a[11] + ","+a[12] + ",6\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd == 7 :
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[6] + ","+ a[7] + "," + a[0] + "," +a[8] +  ","+a[9] + ","+a[10] + ","+a[11] + ","+a[12] + ",7\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==8:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[6] + ","+ a[7] + "," + a[8] + "," +a[0] +  ","+a[9] + ","+a[10] + ","+a[11] + ","+a[12] + ",8\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==9:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[6] + ","+ a[7] + "," + a[8] + "," +a[9] +  ","+a[0] + ","+a[10] + ","+a[11] + ","+a[12] + ",9\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==10:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[6] + ","+ a[7] + "," + a[8] + "," +a[9] +  ","+a[10] + "," + a[0] + "," +a[11] + ","+a[12] + ",10\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==11:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[6] + ","+ a[7] + "," + a[8] + "," +a[9] +  ","+a[10] + "," + a[11] + "," +a[0] + ","+a[12] + ",11\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==12:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[6] + ","+ a[7] + "," + a[8] + "," +a[9] +  ","+a[10] + "," + a[11] + "," +a[12] + ","+a[0] + ",12\n"
            fout.write(line.replace("NULL", "NaN"))
        count_for_odd = count_for_odd + 1

    fout.close
    return None
def swap_and_write_to_a_file_14way(total_comb,outfile):
    fout = open(outfile,"w+",encoding="utf-8")
    
    final_Str = return_colum_names(14)
    fout.write(final_Str)

    count_for_odd = 0
    for a in total_comb:
        count_for_odd = count_for_odd % 14
        
        if count_for_odd == 0:
            line = a[0] + "," + a[1] +","+a[2] + "," + a[3] +","+ a[4] + ","+ a[5] + "," + a[6] + "," + a[7] + "," +a[8] + ","+a[9] + ","+a[10] + ","+a[11] + ","+a[12] + ","+a[13] + ",0\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd == 1:
            line = a[1] + "," + a[0] +","+a[2] + "," + a[3]  + ","+ a[4] + ","+ a[5] + ","+ a[6] + "," + a[7] + "," +a[8] + ","+a[9] + ","+a[10] + ","+a[11] + ","+a[12] + ","+a[13] + ",1\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==2:
            line = a[2] + "," + a[1] +","+a[0] + "," + a[3]  + ","+ a[4] + ","+ a[5] + ","+ a[6] + "," + a[7] + "," +a[8] + ","+a[9] + ","+a[10] + ","+a[11] + ","+a[12] + ","+a[13] + ",2\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==3:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[0]  + "," + a[4]  + ","+ a[5] + ","+ a[6] + "," + a[7] + "," +a[8] + ","+a[9] + ","+a[10] + ","+a[11] + ","+a[12] + ","+a[13] + ",3\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==4:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[0] + ","+ a[5] + ","+ a[6] + "," + a[7] + "," +a[8] + ","+a[9] + ","+a[10] + ","+a[11] + ","+a[12] + ","+a[13] + ",4\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==5:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[0] + ","+ a[6] + "," + a[7] + "," +a[8] + ","+a[9] + ","+a[10] + ","+a[11] + ","+a[12] + ","+a[13] + ",5\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd == 6:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[6] + ","+ a[0] + "," + a[7] + "," +a[8] + ","+a[9] + ","+a[10] + ","+a[11] + ","+a[12] + ","+a[13] + ",6\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd == 7 :
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[6] + ","+ a[7] + "," + a[0] + "," +a[8] +  ","+a[9] + ","+a[10] + ","+a[11] + ","+a[12] + ","+a[13] + ",7\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==8:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[6] + ","+ a[7] + "," + a[8] + "," +a[0] +  ","+a[9] + ","+a[10] + ","+a[11] + ","+a[12] + ","+a[13] + ",8\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==9:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[6] + ","+ a[7] + "," + a[8] + "," +a[9] +  ","+a[0] + ","+a[10] + ","+a[11] + ","+a[12] + ","+a[13] + ",9\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==10:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[6] + ","+ a[7] + "," + a[8] + "," +a[9] +  ","+a[10] + "," + a[0] + "," +a[11] + ","+a[12] + ","+a[13] + ",10\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==11:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[6] + ","+ a[7] + "," + a[8] + "," +a[9] +  ","+a[10] + "," + a[11] + "," +a[0] + ","+a[12] + ","+a[13] + ",11\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==12:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[6] + ","+ a[7] + "," + a[8] + "," +a[9] +  ","+a[10] + "," + a[11] + "," +a[12] + ","+a[0] + ","+a[13] + ",12\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==13:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[6] + ","+ a[7] + "," + a[8] + "," +a[9] +  ","+a[10] + "," + a[11] + "," +a[12] + ","+a[13] + ","+a[0] + ",13\n"
            fout.write(line.replace("NULL", "NaN"))
        count_for_odd = count_for_odd + 1

    fout.close
    return None
def swap_and_write_to_a_file_15way(total_comb,outfile):
    fout = open(outfile,"w+",encoding="utf-8")
    
    final_Str = return_colum_names(15)
    fout.write(final_Str)

    count_for_odd = 0
    for a in total_comb:
        count_for_odd = count_for_odd % 15
   
        if count_for_odd == 0:
            line = a[0] + "," + a[1] +","+a[2] + "," + a[3] +","+ a[4] + ","+ a[5] + "," + a[6] + "," + a[7] + "," +a[8] + ","+a[9] + ","+a[10] + ","+a[11] + ","+a[12] + ","+a[13] + ","+a[14] + ",0\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd == 1:
            line = a[1] + "," + a[0] +","+a[2] + "," + a[3]  + ","+ a[4] + ","+ a[5] + ","+ a[6] + "," + a[7] + "," +a[8] + ","+a[9] + ","+a[10] + ","+a[11] + ","+a[12] + ","+a[13] + ","+a[14] + ",1\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==2:
            line = a[2] + "," + a[1] +","+a[0] + "," + a[3]  + ","+ a[4] + ","+ a[5] + ","+ a[6] + "," + a[7] + "," +a[8] + ","+a[9] + ","+a[10] + ","+a[11] + ","+a[12] + ","+a[13] + ","+a[14] + ",2\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==3:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[0]  + "," + a[4]  + ","+ a[5] + ","+ a[6] + "," + a[7] + "," +a[8] + ","+a[9] + ","+a[10] + ","+a[11] + ","+a[12] + ","+a[13] + ","+a[14] + ",3\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==4:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[0] + ","+ a[5] + ","+ a[6] + "," + a[7] + "," +a[8] + ","+a[9] + ","+a[10] + ","+a[11] + ","+a[12] + ","+a[13] + ","+a[14] + ",4\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==5:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[0] + ","+ a[6] + "," + a[7] + "," +a[8] + ","+a[9] + ","+a[10] + ","+a[11] + ","+a[12] + ","+a[13] + ","+a[14] + ",5\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd == 6:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[6] + ","+ a[0] + "," + a[7] + "," +a[8] + ","+a[9] + ","+a[10] + ","+a[11] + ","+a[12] + ","+a[13] + ","+a[14] + ",6\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd == 7 :
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[6] + ","+ a[7] + "," + a[0] + "," +a[8] +  ","+a[9] + ","+a[10] + ","+a[11] + ","+a[12] + ","+a[13] + ","+a[14] +  ",7\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==8:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[6] + ","+ a[7] + "," + a[8] + "," +a[0] +  ","+a[9] + ","+a[10] + ","+a[11] + ","+a[12] + ","+a[13] + ","+a[14] + ",8\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==9:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[6] + ","+ a[7] + "," + a[8] + "," +a[9] +  ","+a[0] + ","+a[10] + ","+a[11] + ","+a[12] + ","+a[13] + ","+a[14] + ",9\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==10:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[6] + ","+ a[7] + "," + a[8] + "," +a[9] +  ","+a[10] + "," + a[0] + "," +a[11] + ","+a[12] + ","+a[13] + ","+a[14] + ",10\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==11:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[6] + ","+ a[7] + "," + a[8] + "," +a[9] +  ","+a[10] + "," + a[11] + "," +a[0] + ","+a[12] + ","+a[13] + ","+a[14] + ",11\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==12:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[6] + ","+ a[7] + "," + a[8] + "," +a[9] +  ","+a[10] + "," + a[11] + "," +a[12] + ","+a[0] + ","+a[13] + ","+a[14] + ",12\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==13:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[6] + ","+ a[7] + "," + a[8] + "," +a[9] +  ","+a[10] + "," + a[11] + "," +a[12] + ","+a[13] + ","+a[0] + ","+a[14] + ",13\n"
            fout.write(line.replace("NULL", "NaN"))
        elif count_for_odd ==14:
            line = a[3] + "," + a[1] +","+a[2] + "," + a[4]  + ","+ a[5] + ","+ a[6] + ","+ a[7] + "," + a[8] + "," +a[9] +  ","+a[10] + "," + a[11] + "," +a[12] + ","+a[13] + ","+a[14] + ","+a[0] + ",14\n"
            fout.write(line.replace("NULL", "NaN"))
        count_for_odd = count_for_odd + 1

    fout.close
    return None

def redirect_to_n_way(total_comb,path_to_parsed_results8,n):
    if n==2:       
        swap_and_write_to_a_file_2way(total_comb,path_to_parsed_results8)
    elif n==4:     
        swap_and_write_to_a_file_4way(total_comb,path_to_parsed_results8)
    elif n==5:
        swap_and_write_to_a_file_5way(total_comb,path_to_parsed_results8)
    elif n==6:  
        swap_and_write_to_a_file_6way(total_comb,path_to_parsed_results8)
    elif n==7:  
        swap_and_write_to_a_file_7way(total_comb,path_to_parsed_results8)
    elif n==8:
        swap_and_write_to_a_file_8way(total_comb,path_to_parsed_results8)
    elif n==9:
        swap_and_write_to_a_file_9way(total_comb,path_to_parsed_results8)
    elif n==10:
        swap_and_write_to_a_file_10way(total_comb,path_to_parsed_results8)
    elif n==11: 
        swap_and_write_to_a_file_11way(total_comb,path_to_parsed_results8)
    elif n==12:
        swap_and_write_to_a_file_12way(total_comb,path_to_parsed_results8)
    elif n==13:
        swap_and_write_to_a_file_13way(total_comb,path_to_parsed_results8)
    elif n==14:
        swap_and_write_to_a_file_14way(total_comb,path_to_parsed_results8)
    elif n==15:
        swap_and_write_to_a_file_15way(total_comb,path_to_parsed_results8)
    elif n==16:
        swap_and_write_to_a_file_15way(total_comb,path_to_parsed_results8)
    return None

def main():
    path_to_parsed_results5 = "C:\\Users\\AtakanPavilion\\Desktop\Atakan\\01.Work\\projects\\horse_racing\\data\\race_results_parsed\\final_dataset.txt"
    path_to_parsed_results6 = "C:\\Users\\AtakanPavilion\\Desktop\Atakan\\01.Work\\projects\\horse_racing\\data\\race_results_parsed\\final_dataset2.txt"
    path_to_parsed_results8 = "C:\\Users\\AtakanPavilion\\Desktop\Atakan\\01.Work\\projects\\horse_racing\\data\\race_results_parsed\\final.csv"
    
    n_way = 13
    bound = 6
    city = "," # "," means all the cities
    distance = "," # "," means all the dist
    
    re_write_check_correct(path_to_parsed_results5,path_to_parsed_results6,city,distance)
    print("done")
    total_comb = take_n_way_combinations_and_parse(path_to_parsed_results6,n_way,bound)
    print("done")
    redirect_to_n_way(total_comb,path_to_parsed_results8,n_way)
    print("done")
    
    
    return None




main()
