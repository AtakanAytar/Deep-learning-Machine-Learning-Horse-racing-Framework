from datetime import datetime , date, timedelta



def force_check_data_format(infile):
    #Counts Commas and returns number of diffrent commas
    f = open(infile,"r",encoding="utf-8")
    no_of_commas = []    
    
    for line in f:
        count = line.count(",")
        if count ==20:
            print(line)
        
        if count not in no_of_commas:
            no_of_commas.append(count)
    print(len(no_of_commas))
    f.close()
    return None

def specific_format_force(infile,outfile):
    fin = open(infile,"r",encoding="utf-8")
    fout = open(outfile,"w+",encoding="utf-8")

    for line in fin:
        temp = line.split(",")
        speeds = []
        
        for a in temp:
            if a.count(".")==2:
                speeds.append(a)
        
        if line.count("),")==0:
            line=line.replace(")","),")

        if line.count("kg") !=1:
            no_temp = line.count("kg") - 1
            for a in range (no_temp):
                line = line.replace("kg,","+",1)

        
        
        
        
        if len(speeds)==2 or line=="\n":
            fout.write(line)

    fin.close()
    fout.close()
    return None


def create_competionStrength_NormalizedSpeedForTheHorse_LenghtsBehindWinner(path_to_parsed_results,path_to_new_parsed_results):
    infile = open(path_to_parsed_results,"r",encoding="utf-8")
    outfile = open(path_to_new_parsed_results,"w+",encoding="utf-8")

    for_the_horses = []
    lengths_behind_winner = []
    line_list =[]
    best_speed_for_the_race = 0
    for line in infile:
        
        if line.count("derecesiz") == 1:
            line ="\n"
        
        if line !="\n":
           
            line_list.append(line) # so we can write them later to new file
            
            temp = line.split(",")
            speeds = []
            for a in temp:
                if a.count(".")==2 and a.count("kg")==0:
                    speeds.append(a)

                        
            if int(temp[0]) == 1: # might not work if it is the first horse it is the best speed which will be used later
                temp1= speeds[0].split(".")
                best_speed_for_the_race =  3600 * int(temp1[0]) + 60 * int(temp1[1]) + int(temp1[2])
            
            temp1=speeds[0].split(".")
            horse_speed= 3600 * int(temp1[0]) + 60 * int(temp1[1]) + int(temp1[2])
            
            temp1=speeds[1].split(".")
            eid =  3600 * int(temp1[0]) + 60 * int(temp1[1]) + int(temp1[2])
            
            length_behind = (best_speed_for_the_race - horse_speed) / eid # normalized ?
            normalized_horse_speed = eid / horse_speed / eid
            
            for_the_horses.append(normalized_horse_speed) # later will also be used to calculate the compettion strenght
            
            lengths_behind_winner.append(length_behind)

        else : #used to be else
            # will calculate compettion strength by we wil get the avg of list deducy normalized horse speed and divide to standart error and len of the list minus 1 ?
            #will write lines with apended info
            opponent_str = []
            total_time  = 0
            for a in for_the_horses:
                total_time = total_time + a 
            
            for a in for_the_horses:
                x12 = (len(for_the_horses) - 1)
                if x12 ==0:
                    x12 =1
                compstr = (total_time - a) / x12
                opponent_str.append(compstr)
                
            index = 0
            for line in line_list:
                line = line.replace("\n","") + "," +  str(for_the_horses[index]) + "," + str(lengths_behind_winner[index]) + ","+ str(opponent_str[index])+"," + str(len(for_the_horses))+"\n"
                outfile.write(line)
                index = index + 1

            line_list.clear()
            for_the_horses.clear()
            lengths_behind_winner.clear()
            outfile.write("\n")

        
    infile.close()
    outfile.close()
    return None

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

def extract_columns(in_file,out_file):

    
    fin = open(in_file,"r",encoding="utf-8")
    fout = open(out_file,"w+",encoding="utf-8")
    fout.write("sıra,at_id,yaş,kilo,jokey,sahip,antrenör,horse_time,eid,starting_position,date,track_condition,city_name,distance,material,handikap,normalized_time_for_horse,lengths_behind_winner,normalized_time_for_horse\n")
    track_condition = []
    for line in fin:
        if line !="\n":
            temp = line.split(",")
            speeds = []
            for a in temp:
                if a.count(".")==2 and a.count("kg")==0:
                    speeds.append(a)
          
            sıra = temp[0]
            at_id = temp[1]
            yaş = temp[2]
            kilo = temp[4]
            jokey = temp[5]
            sahip = temp[6]
            antrenör = temp[7]
            horse_time = speeds[0]
            eid = speeds[1]
            starting_position = temp[11]
            date = temp[len(temp)-5]
            track_condition = temp[len(temp)-6]
            city_name = temp[len(temp)-7]
            distancematerial = temp[len(temp)-9]
            handikap = temp[len(temp)-10]
            normalized_time_for_horse = temp[len(temp)- 4 ]
            lengths_behind_winner = temp[len(temp)-3]
            normalized_time_for_opponents = temp[len(temp)-2]
            line = sıra + "," + at_id + "," + yaş + "," +kilo + "," + jokey + "," + sahip + "," + antrenör + "," + horse_time + ","+ eid + "," + starting_position + ","  + date + ","  + track_condition + "," + city_name + "," + distancematerial[:4] + ","+distancematerial[4:]+","+ handikap+","+normalized_time_for_horse+","+lengths_behind_winner+","+normalized_time_for_opponents+"\n"  
            fout.write(line)
        else:
            
            fout.write("\n")
    
    return None


def return_last_n_races(curr_date,horse_table,horse_id,n):
    last_n_races = []
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
    line = fin.readline()
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
            # add 1 to date so todays race ganyan returns this needs to go for predictor
            ganyan_temp_list = return_last_race_of_horse(date,horse_table,horse_id,1)
            ganyan_temp_list = ganyan_temp_list[0].split(",")
            ganyan = ganyan_temp_list[9]
            
            
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

def main():
    the_directory = "C:\\Users\\AtakanPavilion\\Desktop\Atakan\\01.Work\\projects\\horse_racing\\data\\race_results_parsed\\"
    path_to_parsed_results = "C:\\Users\\AtakanPavilion\\Desktop\Atakan\\01.Work\\projects\\horse_racing\\data\\race_results_parsed\\dataset_of_initial_info.txt"
    path_to_parsed_results2 = "C:\\Users\\AtakanPavilion\\Desktop\Atakan\\01.Work\\projects\\horse_racing\\data\\race_results_parsed\\dataset_of_initial_info2.txt"
    path_to_parsed_results3 = "C:\\Users\\AtakanPavilion\\Desktop\Atakan\\01.Work\\projects\\horse_racing\\data\\race_results_parsed\\dataset_of_initial_info3.txt"
    path_to_horse_table = "C:\\Users\\AtakanPavilion\\Desktop\Atakan\\01.Work\\projects\\horse_racing\\data\\race_results_parsed\\horse_base.txt"
    path_to_parsed_results4 = "C:\\Users\\AtakanPavilion\\Desktop\Atakan\\01.Work\\projects\\horse_racing\\data\\race_results_parsed\\dataset_of_initial_info4.txt"
    path_to_parsed_results5 = "C:\\Users\\AtakanPavilion\\Desktop\Atakan\\01.Work\\projects\\horse_racing\\data\\race_results_parsed\\final_dataset.txt"
    specific_format_force(path_to_parsed_results,path_to_parsed_results2)
    
    create_competionStrength_NormalizedSpeedForTheHorse_LenghtsBehindWinner(path_to_parsed_results2,path_to_parsed_results3)
    
    horse_table = create_horse_tables(path_to_parsed_results3,path_to_horse_table)
    jokey_table = create_jokey_tables(path_to_parsed_results3,the_directory+"jokey_base.txt")
    trainer_table = create_trainer_tables(path_to_parsed_results3,the_directory+"trainer_base.txt")
    owner_table = create_owner_tables(path_to_parsed_results3,the_directory+"owner_base.txt")
    extract_columns(path_to_parsed_results3,path_to_parsed_results4)

    finalize_the_data_set(horse_table,jokey_table,trainer_table,owner_table,path_to_parsed_results4,path_to_parsed_results5)
    #force_check_data_format(path_to_parsed_results)
main()