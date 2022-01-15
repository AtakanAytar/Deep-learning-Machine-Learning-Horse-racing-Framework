from datetime import date
import os

def clear_other_then_race_results(infile,outfile):
    in_file = open(infile,"r",encoding="utf-8")
    out_file = open(outfile,"w+",encoding="utf-8")
    first_line = in_file.readline()
    city = first_line[:first_line.find("(")]
    race_array = []
    lock = False
    eid = ""
    material = ""
    distance = ""
    for line in in_file:
        if line[0].isdigit() and line[1]=="." and line[2]==" ":
            if lock:
                line = line.split(" ")
                eid = line[len(line)-2]
                material = line[len(line)-6]
                distance = line[len(line)-7]

                
            lock = True
        if line.count("N	At İsmi	Yaş	Orijin (Baba - Anne)	Kilo	Jokey	Sahip	Antrenör	St	HP	Son 6 Y.	KGS	s20	En İyi D.	Gny	AGF") != 0:
            line = next(in_file)
            while line[0].isdigit() and (line[1]=="\t" or line[1].isdigit()):
                line = line.replace("\n","")
                line = line.replace(",",".")
                line = line.replace("\t",",")
                line = line + "," + eid + "," + material + "," + distance + ","+city + "\n"


                out_file.write(line.lower().replace("ds",""))
                line = next(in_file)
                
                if line[0] =="%":
                    line = next(in_file)
            out_file.write("\n")
    return None

def turn_names_to_ids(horse_name,jokey_name,owner_name,trainer_name):
    path_for_ids = "C:\\Users\\AtakanPavilion\\Desktop\\Atakan\\01.Work\\projects\\horse_racing\\data\\race_results_parsed"
    horse_file = open(path_for_ids+"\\horse_ids.txt","r",encoding="utf-8")
    jokey_file = open(path_for_ids+"\\jokey_ids.txt","r",encoding="utf-8")
    owner_file = open(path_for_ids+"\\owner_ids.txt","r",encoding="utf-8")
    trainer_file = open(path_for_ids+"\\trainer_ids.txt","r",encoding="utf-8")
    horse_id , jokey_id , owner_id ,trainer_id =  "-1" , "-1" , "-1" , "-1"
    
    for line in horse_file:
        line = line.replace("\n","").split(",")
        if line[1]==horse_name:
            horse_id = line[0]
            break
    
    for line in jokey_file:
        line = line.replace("\n","").split(",")
        if line[1]==jokey_name:
            jokey_id = line[0]
            break
    
    for line in owner_file:
        line = line.replace("\n","").split(",")
        if line[1]==owner_name:
            owner_id = line[0]
            break
    
    for line in trainer_file:
        line = line.replace("\n","").split(",")
        if line[1]== trainer_name:
            trainer_id = line[0]
            break
    
    return horse_id , jokey_id , owner_id ,trainer_id


def reparse(infile,outfile):
    in_file = open(infile,"r",encoding="utf-8")
    out_file = open(outfile,"w+",encoding="utf-8")
    
    
    for line in in_file:
        if line !="\n":
            line = line.split(",")
            indx = 0
            to_be_written = ""
            to_be_dropped =[3,10,11,12,13,15]
            forbidden = ["kg","k","db","sk","skg","ts","gkr","tgk","yp","sgkr","ap","ög","bb"]
            horsename = ""
            for a in line:
                if indx ==1:
                    #GET HORSE NAME FOOL PROOF
                    a = a.split(" ")
                    horsename = ""
                    for sample in a:
                        if sample.find("(") == -1:
                            if sample not in forbidden:
                                horsename= horsename + sample
                    a = horsename   
                   
                
                if indx ==2:
                    a = a.split(" ")
                    a = a[0].replace("y","")

                if indx == 4:
                    if a.find("+") !=-1:
                        a = a.split("+")
                        a = str(float(a[0]) + float(a[1]))

                if indx not in to_be_dropped:
                    to_be_written = to_be_written +"," + str(a)
                indx = indx + 1
            
            to_be_written = to_be_written[1:].replace(" ","")
            temp = to_be_written.split(",")
            sıra = temp[0]
            at = temp[1]
            yaş = temp[2]
            kilo = temp[3]
            jokey = temp[4]
            sahip = temp[5]
            antrenör = temp[6]
            horse_time = ""
            eid = ""
            starting_position = temp[7]
            date_today = str(date.today())
            track_condition = ""
            city_name = temp[len(temp)-1].replace("\n","")
            distance = temp[len(temp)-2]  
            material = temp[len(temp)-3]
            handikap = temp[len(temp)-6]
            normalized_time_for_horse = ""
            lengths_behind_winner = ""
            normalized_time_for_opponents = ""
            ganyan = temp[9]
            horse_id , jokey_id , owner_id ,trainer_id = turn_names_to_ids(at,jokey,sahip,antrenör)
            to_be_written= sıra + "," + horse_id + "," + yaş + "," +  kilo + "," + jokey_id + "," + owner_id + ","+ trainer_id+"," + horse_time + "," + eid + "," + starting_position +","+date_today + "," + track_condition + "," + city_name + "," + distance + "," + material +","+ handikap +"," +normalized_time_for_horse + ","+ lengths_behind_winner + "," + normalized_time_for_horse +","+ganyan+ "\n"
            out_file.write(to_be_written)
        else:
            out_file.write("\n")
    return None

#not sure if i take age 10 as 10 and not 1 




from datetime import datetime , date, timedelta






def create_trainer_tables(in_file,out_file):
    fin = open(in_file,"r",encoding="utf-8")
    fout = open(out_file,"w+",encoding="utf-8")
    horses = {}
    for line in fin:
        if line != "\n":            
            temp_list = line.split(",")
            horse_id = temp_list[7]
            if horse_id not in horses:
                horses[horse_id] = []
                horses[horse_id].append(line)
            else:
                horses[horse_id].append(line)
    
    for key in horses.keys():
        temp_list = horses[key]
        
        for alist in temp_list: #each race of the horse 
            fout.write(alist)
        fout.write("\n")
           
    fin.close()
    fout.close()
    return horses

def create_owner_tables(in_file,out_file):
    fin = open(in_file,"r",encoding="utf-8")
    fout = open(out_file,"w+",encoding="utf-8")
    horses = {}
    for line in fin:
        if line != "\n":            
            temp_list = line.split(",")
            horse_id = temp_list[6]
            if horse_id not in horses:
                horses[horse_id] = []
                horses[horse_id].append(line)
            else:
                horses[horse_id].append(line)
    
    for key in horses.keys():
        temp_list = horses[key]
        
        for alist in temp_list: #each race of the horse 
            fout.write(alist)
        fout.write("\n")
           
    fin.close()
    fout.close()
    return horses
def create_jokey_tables(in_file,out_file):
    fin = open(in_file,"r",encoding="utf-8")
    fout = open(out_file,"w+",encoding="utf-8")
    horses = {}
    for line in fin:
        if line != "\n":            
            temp_list = line.split(",")
            horse_id = temp_list[5]
            if horse_id not in horses:
                horses[horse_id] = []
                horses[horse_id].append(line)
            else:
                horses[horse_id].append(line)
    
    for key in horses.keys():
        temp_list = horses[key]
        
        for alist in temp_list: #each race of the horse 
            fout.write(alist)
        fout.write("\n")
           
    fin.close()
    fout.close()
    return horses

def create_horse_tables(in_file,out_file):
    fin = open(in_file,"r",encoding="utf-8")
    fout = open(out_file,"w+",encoding="utf-8")
    horses = {}
    for line in fin:
        if line != "\n":            
            temp_list = line.split(",")
            horse_id = temp_list[1]
            if horse_id not in horses:
                horses[horse_id] = []
                horses[horse_id].append(line)
            else:
                horses[horse_id].append(line)
    
    for key in horses.keys():
        temp_list = horses[key]
        
        for alist in temp_list: #each race of the horse 
            fout.write(alist)
        fout.write("\n")
           
    fin.close()
    fout.close()
    return horses



def return_last_n_races(curr_date,horse_table,horse_id,n):
    
    last_n_races = []
    
    if horse_id =="-1":
        return last_n_races
    temp_list = horse_table[horse_id]
    curr_date = datetime.strptime(str(curr_date), "%Y-%m-%d")
    for race in reversed(temp_list):
        race_list = race.split(",")
        race_date = race_list[len(race_list)-5]
        race_date = datetime.strptime(str(race_date), "%Y-%m-%d")
        if race_date < curr_date:
            last_n_races.append(race)
            if len(last_n_races) == n:
                break

    return last_n_races


def return_last_race_of_horse(curr_date,horse_table,horse_id,n):
    last_n_races = []
    temp_list = horse_table[horse_id]
    curr_date = datetime.strptime(str(curr_date), "%Y-%m-%d")
    curr_date = curr_date + timedelta(days=1)
    for race in reversed(temp_list):
        race_list = race.split(",")
        race_date = race_list[len(race_list)-5]
        race_date = datetime.strptime(str(race_date), "%Y-%m-%d")
        if race_date < curr_date:
            last_n_races.append(race)
            if len(last_n_races) == n:
                break

    return last_n_races



def return_win_percentage(some_list):
    win_count = 0
    for a in some_list:
        b = a.split(",")
        rank = b[0]
        if rank == "1":
            win_count=win_count+1
    win_rate = win_count / len(some_list) 




    return win_rate


def decide_if_they_are_at_their_pref_cond(curr_date,horse_table,horse_id,curr_city,curr_distance,curr_mat):
    #1 if pref , 0 else
    last_races = return_last_n_races(curr_date,horse_table,horse_id,99)
    distance_bit = 0
    mat_bit = 0
    city_bit = 0
    for a in last_races:
        
        b = a.split(",")
        
        if b[0]=="1":
            distance_material = b[len(b)-9]
            distance = distance_material[:4]
            material = distance_material[4:]
            city  = b[len(b)- 7]
            if curr_city == city:
                city_bit=city_bit + 1
            if curr_distance == distance:
                distance_bit = distance_bit + 1
            if curr_mat == material:
                mat_bit = mat_bit + 1
    
    
    if len(last_races) !=0:
        city_bit = city_bit / len(last_races)
        distance_bit = distance_bit / len(last_races)
        mat_bit = mat_bit / len(last_races)




    return  city_bit , distance_bit , mat_bit

def finalize_the_data_set(horse_table,jokey_table,trainer_table,owner_table,in_file,out_file):
    fin = open(in_file,"r",encoding="utf-8")
    fout =  open(out_file,"w+",encoding="utf-8")
    fout.write("sıra,at_id,yaş,kilo,jokey,sahip,antrenör,horse_time,eid,starting_position,date,track_condition,city_name,distance,material,handikap,normalized_time_for_horse,lengths_behind_winner,normalized_time_for_comp,avg_position,new_dist,jokey_win_rate,owner_win_rate,trainer_win_rate,city_pref,distance_pref,mat_pref,days_since_last_race,ganyan,win_bit\n")
    #line = fin.readline()
    all_the_lines = fin.readlines()
    
    index = 0
    city_bit , distance_bit , mat_bit = 0 , 0 , 0
    for line in all_the_lines:
        if line !="\n":
            print(index / len(all_the_lines) )  #Progress
            
            list_of_fea = line.split(",") 

            ###real_input
            horse_id = list_of_fea[1]
            jokey_id = list_of_fea[4]
            owner_id = list_of_fea[5]
            trainer_id = list_of_fea[6]
            # add ganyan here for predictor ganyan = list_of_fea[?]
            date = list_of_fea[10] #?
            ###real_input_end

            
                
            #ganyan
            
            ganyan = list_of_fea[19].replace("\n","")
            del list_of_fea[19]
            
            
            n = 4
            last_races = return_last_n_races(date,horse_table,horse_id,n)

            
            
            
            normalized_time_for_horse = "NULL"
            lengths_behind_winner = "NULL"
            comp_strenght = "NULL"
            new_dist = 1
            time_since_last_race = 0

            #Jokey_Trainer_owner_win_percentage
            all_races_of_jokey   = return_last_n_races(date,jokey_table,jokey_id,999999)
            all_races_of_trainer = return_last_n_races(date,trainer_table,trainer_id,999999)
            all_races_of_owner = return_last_n_races(date,owner_table,owner_id,999999)
            
            if len(all_races_of_jokey)!=0:
                jokey_win_rate = return_win_percentage(all_races_of_jokey)
            else:
                jokey_win_rate = "NULL"
            

            if len(all_races_of_trainer)!=0:
                trainer_win_rate = return_win_percentage(all_races_of_trainer)
            else:
                trainer_win_rate = "NULL"
            
            if len(all_races_of_owner)!=0:
                owner_win_rate = return_win_percentage(all_races_of_owner)
            else:
                owner_win_rate = "NULL"
            ## end jokey_trainer_owner win percantage

            ## city distance material pref
            curr_city= list_of_fea[len(list_of_fea)-7]
            curr_distance = list_of_fea[len(list_of_fea)-6]
            curr_mat = list_of_fea[len(list_of_fea)-5]
                
                
            
            
            if len(last_races)!=0:
                count_1 = 0
                count_2 = 0
                count_3 = 0
                count_4 = 0
                a = last_races[0].split(",")
                date_from_last_races = a[len(a)-5]
                for a in last_races:
                    
                    a = a.split(",")
                    normalized_time_for_horse = float(a[len(a)-4])
                    lengths_behind_winner = float(a[len(a)-3])
                    comp_strenght = float(a[len(a)-2]) 
                    avg_position = float(a[0])
                    

                    count_1 = count_1 + normalized_time_for_horse
                    count_2 = count_2 + lengths_behind_winner
                    count_3 = count_3 + comp_strenght
                    count_4 = count_4 + (avg_position / int(a[len(a)-1].replace("\n","")) )
                  
                count_1 = count_1 / len(last_races)
                count_2 = count_2 / len(last_races)
                count_3 = count_3 / len(last_races)
                count_4 = count_4 / len(last_races)
                
                
                if len(last_races) == 4:
                    new_dist = 0
                else:
                    new_dist = 1
                
                line = line.split(",")
                # this is a problem since there wont be count in the first place
                line[len(line)-3] = count_1 
                line[len(line)-2] = count_2
                line[len(line)-1] = count_3
                line.append(count_4)
                line.append(new_dist)
                line.append(jokey_win_rate)
                line.append(owner_win_rate)
                line.append(trainer_win_rate)
                
                city_bit , distance_bit , mat_bit = decide_if_they_are_at_their_pref_cond(date,horse_table,horse_id,curr_city,curr_distance,curr_mat)
                line.append(city_bit)
                line.append(distance_bit)
                line.append(mat_bit)
                
                
                
                #Time since last race
                time_since_last_race = (datetime.strptime(str(date), "%Y-%m-%d") - datetime.strptime(str(date_from_last_races), "%Y-%m-%d")).days
                line.append(time_since_last_race)

                line.append(ganyan)
                
                #Win_bit
                win_bit = 0
                if list_of_fea[0]=="1":
                    win_bit = 1

                line.append(win_bit)
        
                for_bidden = ["[","]","'"," "]
                line = str(line)
                for char in for_bidden:
                    line = line.replace(char , "")
                
                all_the_lines[index] = line
                index = index + 1
            elif len(last_races)==0:
                
                #eğer yarışı yoksa bile düzgün bir şey çıkıyor diğer atların datası mundar olmuyor
                new_dist = 1
                trainer_win_rate,owner_win_rate,jokey_win_rate,city_bit , distance_bit , mat_bit = 0 , 0 , 0 , 0 , 0 , 0
                line = line.split(",")
                line[len(line)-3] = "NULL" 
                line[len(line)-2] = "NULL"
                line[len(line)-1] = "NULL"
                line.append("NULL") #for count4
                line.append(new_dist)
                line.append(jokey_win_rate)
                line.append(owner_win_rate)
                line.append(trainer_win_rate)
                line.append(city_bit)
                line.append(distance_bit)
                line.append(mat_bit)
                line.append("NULL") # for days since last race
                line.append(ganyan)
                #Win_bit
                win_bit = 0
                if list_of_fea[0]=="1":
                    win_bit = 1

                line.append(win_bit)

                for_bidden = ["[","]","'"," "]
                
                line = str(line)
                for char in for_bidden:
                    line = line.replace(char , "")
                
                all_the_lines[index] = line
                index = index + 1
        else:
            index = index + 1
    
    
    
    for line in all_the_lines:
        fout.write(line+"\n")
   
            


    fin.close()
    fout.close()
    return None

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
        
        if (line.count("pdfsonuçlar|özetpdfsonuçlar|") == 0  and line.count(city)>=1 and line.count(distance)>=1):
            
            # 2 \n  arka arkaya yazılamasın
           
            line = drop_columns(line,col_list)
            line_temp = line.split(",")
            
            if line_temp[0] =="1":
                fout.write("\n")
            
            fout.write(line.replace(",,",",").replace(",,",",0,"))
        prev_line  = line
    fin.close()
    fout.close()
    return None


def delete_unused_files(a_list):
    for name in a_list:
        os.remove(name)


def killem(infile):
    fin = open(infile,"r",encoding="utf-8")
    line = next(fin)
    line = next(fin)
    all_races = []
    temp_race = []
    for line in fin:
        if line!="\n":
            temp_race.append(line)
        else:
            all_races.append(temp_race) 
            temp_race = [] 
    all_races.append(temp_race)
    
    count = 1
    for a in all_races:
        text_name = str(count) + "_" + str(len(a)) + ".txt"
        fout = open(text_name,"w+",encoding="utf-8")
        single_line = ""
        for b in a:
            single_line = single_line + b[b.find(",")+1:].replace("\n",",")
            fout.write(b)
        
        fout.write("\n")
        fout.write(single_line.strip(","))
        
        count = count + 1
    return None


def main():
    the_directory = "C:\\Users\\AtakanPavilion\\Desktop\Atakan\\01.Work\\projects\\horse_racing\\data\\race_results_parsed\\"
    
    path_to_parsed_results3 = "C:\\Users\\AtakanPavilion\\Desktop\Atakan\\01.Work\\projects\\horse_racing\\data\\race_results_parsed\\dataset_of_initial_info3.txt"
    path_to_horse_table = "C:\\Users\\AtakanPavilion\\Desktop\Atakan\\01.Work\\projects\\horse_racing\\data\\race_results_parsed\\horse_base.txt"

    clear_other_then_race_results("day.txt","day2.txt")
    reparse("day2.txt","day3.txt")

      
    horse_table = create_horse_tables(path_to_parsed_results3,path_to_horse_table)
    jokey_table = create_jokey_tables(path_to_parsed_results3,the_directory+"jokey_base.txt")
    trainer_table = create_trainer_tables(path_to_parsed_results3,the_directory+"trainer_base.txt")
    owner_table = create_owner_tables(path_to_parsed_results3,the_directory+"owner_base.txt")
    


    finalize_the_data_set(horse_table,jokey_table,trainer_table,owner_table,"day3.txt","day4.txt")
    re_write_check_correct("day4.txt","day5.txt",",",",")
    killem("day5.txt")
    unused = ["day2.txt","day3.txt","day4.txt","day5.txt"]
    delete_unused_files(unused)
  
main()

