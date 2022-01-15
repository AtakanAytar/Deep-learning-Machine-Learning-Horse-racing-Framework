from datetime import date, timedelta
import os


def make_dir_at_given_path(path,dirname):
    path = path + "\\"+ str(dirname)
    if not os.path.isdir(path):
        os.makedirs(path)
        for a in range(4):
            temp_path = path + "\\"+str(a)+".txt"
            temp_file = open(temp_path, "w+")
            temp_file.close()
    return None


def create_dirs_for_each_date_at_given_location(path,date_S,date_E):
    day = date_S
    while day != date_E:
        make_dir_at_given_path(path,day)
        day = day + timedelta(days=1)
        
    
    return None






def take_the_city_name_and_race_day_number(line_to_be_extracted):
    end_point=line_to_be_extracted.find("(")
    city_name = line_to_be_extracted[0:end_point].replace(" ","")
    race_day_number = line_to_be_extracted[end_point+1]
    

    return city_name , race_day_number

def get_weather_conditions(line_to_be_extracted):
    track_material = "-"
    track_condition = "-"
    line_to_be_extracted = line_to_be_extracted.lower()
    line_to_be_extracted=line_to_be_extracted.replace("pdf sonuçlar | özet pdf sonuçlar | csv sonuçlar | komiser raporları | kronometrik sonuçlar | agf tablosu\n","")
    line_to_be_extracted = line_to_be_extracted.replace("hava",",")
    line_to_be_extracted = line_to_be_extracted.replace("nem",",")
    line_to_be_extracted = line_to_be_extracted.replace(","," ")
    line_to_be_extracted = line_to_be_extracted.replace(":"," ")
    line_to_be_extracted = line_to_be_extracted.replace("%","")
    list_of_conditions = line_to_be_extracted.split()
    if len(list_of_conditions) > 1:
        track_material = list_of_conditions[0]
        track_condition = list_of_conditions[1]
   

    return track_condition 

def read_file_and_extract_info(file_name,day):
    f = open(file_name,"r",encoding="utf-8")
    to_be_added=""
    line_count=0
    race_array=[]
    koşu_bilgisi = ""
    for line in f:
        if line =="S\tAt İsmi\tYaş\tOrijin(Baba - Anne)\tKilo\tJokey\tSahip\tAntrenörü\tDerece\tGny\tAGF\tSt\tFark\tG. Çık.\tHP\n":
            temp_race=[]
            line = next(f)
            test_digit=line[0]
            while test_digit.isdigit()==True or test_digit=="%" : # garip % li olaylar olabiliyor onu çöz
                line = line.replace(",",".")
                line = line.replace("\t",",")
                line = line.replace("\n","")
                for a in range(12):
                    line = line.replace(",,",",-,")
                if test_digit!="%":
                    
                    temp_race.append(line.replace("\n","") + "," + koşu_bilgisi +"," + to_be_added + "," + str(day) + "\n")
                line = next(f)
                test_digit=line[0]
            race_array.append(temp_race)
        elif line_count==0:
            city_name , race_day_number = take_the_city_name_and_race_day_number(line)
        elif line_count==1:
            track_condition  = get_weather_conditions(line)
            line = f.readline()
            line_count = line_count + 1 
            to_be_added = city_name +  "," +track_condition
        elif line[3:8]=="Koşu:":
            koşu_bilgisi = line[13:].replace("\n","")
            koşu_bilgisi = koşu_bilgisi.replace(" ","")
            koşu_bilgisi = koşu_bilgisi.split(",")
            indexx  = len(koşu_bilgisi)
            koşu_bilgisi = koşu_bilgisi[indexx-2]+","+koşu_bilgisi[indexx-1]

        line_count = line_count + 1


    f.close()
    return race_array 




def read_all_the_files_and_extract_all_the_info(path , date_S , date_E):
    day = date_S
    all_the_races=[]
    while day != date_E:
        for a in range(4):
            path_to_the_file = path + "\\"+ str(day) +"\\" + str(a) + ".txt"
            race_array = read_file_and_extract_info(path_to_the_file,day)
            if len(race_array)!=0:
                all_the_races.append(race_array)
        day = day + timedelta(days=1)
    
    
    
 
    
    return all_the_races



def write_results_to_the_file(file_name,all_the_races,date_S,date_E):
    day = date_S
    f = open(file_name,"w+",encoding="utf-8")
    
   
    count = 0
    for a in all_the_races:
        for b in a:
            count = count+1
        
            for c in b:
                f.write(str(c).replace(" ","").lower().replace("protestovideosui̇çintıklayınız",""))
            f.write("\n") 
        day = day + timedelta(days=1)
    print(count)
    f.close()
    return None



def parse_the_main_file(infile,outfile):
    in_file = open(infile , "r" ,encoding="utf-8")
    out_file = open(outfile,"w+",encoding="utf-8")
    
    drop_list = [3] # any column number here will be dropped
    
    
    special_column_list = [1,2,4]
    
    for line in in_file:
        if line[0]!="-" or line !="\n" :
            temp_list = line.split(",")
            column_no = 0
            out_line = ""
            for a in temp_list:
                if column_no not in drop_list:
                    if column_no not in special_column_list:
                        out_line = out_line + str(a) +","
                    else:
                        if a.find("+") != -1: #To add kgs which might appear by as addiiton
                            a = a.split("+")
                            a = float(a[0]) + float(a[1])
                            out_line = out_line + str(a) +","
                        elif a.find("(") != -1: #horse id separation
                            index1 = a.find("(")
                            index2 = a.find(")")
                            horse_name = a[:index1]
                            horse_best_race_ranking = a[index1+1:index2]
                            out_line = out_line + str(horse_name) +"," + str(horse_best_race_ranking) + ","
                        elif column_no == 2: #age of horse
                            age = a[0]
                            out_line = out_line + str(age) +","
                        else:
                            out_line = out_line + str(a) +","
                        
                column_no = column_no + 1
            
            
            out_file.write(out_line[:-1].replace("e.i̇.d.:",""))

                


    in_file.close()
    out_file.close()
    return None



def assing_ids_to_horses_jokeys_owners_trainers(in_file,horses_file,jokeys_file,owners_file,trainers_file):
    horses = [] # 1
    jokeys = [] # 5
    owners = [] # 6 
    trainers = [] # 7 
    f = open(in_file ,"r",encoding="utf-8")
    
    for line in f:
        if line != "\n" and  line[1]!="-":
         
            temp_list = line.split(",")
            horse_name = temp_list[1]
            jokey = temp_list[5]
            owner = temp_list[6]
            trainer = temp_list[7]
            if horse_name not in horses:
                horses.append(horse_name)
            if jokey not in jokeys: 
                jokeys.append(jokey)
            if owners not in owners:
                owners.append(owner)
            if trainer not in trainers:
                trainers.append(trainer)
    out_horses = open(horses_file,"w+",encoding="utf-8")
    out_jokeys = open(jokeys_file,"w+",encoding="utf-8")
    out_owners = open(owners_file,"w+",encoding="utf-8")
    out_trainers =  open(trainers_file,"w+",encoding="utf-8")
    
    count = 0
    for a in horses:
        out_horses.write(str(count) + "," + a + "\n")
        count = count + 1
    
    count = 0
    for a in jokeys:
        out_jokeys.write(str(count) + "," + a + "\n")
        count = count + 1
    
    count = 0
    for a in owners:
        out_owners.write(str(count) + "," + a + "\n")
        count = count + 1
    
    count = 0
    for a in trainers:
        out_trainers.write(str(count) + "," + a + "\n")
        count = count + 1

    f.close()
    out_horses.close() 
    out_jokeys.close()
    out_owners.close() 
    out_trainers.close()
    return horses , jokeys , owners , trainers


def substitute_names(in_file , out_file,horses ,jokeys , owners , trainers):
    inFile=open(in_file,"r",encoding="utf-8")
    outFile=open(out_file,"w+",encoding="utf-8")
    outFile.write("rank_for_the_race,horse_id,no_for_the_race ,kg_for_the_horse , jokey_id , owner_id ,trainer_id , finishing_time , ganyan_ratio , agf , starting_position , diffrence_by_body_part(needs_to_be_parsed) , delay(atStart) , handikap_point , run_kg ,length_and_trackmaterial,best_time_to_date,city,race_day_no,track_condition,date_of_the_race\n")
    temp_list=[]
    for line in inFile:
        if line != "\n" and  line[1]!="-" :
            temp_list = line.split(",")
            horse_name = temp_list[1]
            jokey = temp_list[5]
            owner = temp_list[6]
            trainer = temp_list[7]

            index_horse= horses.index(horse_name)
            index_jokey= jokeys.index(jokey)
            index_owner= owners.index(owner)
            index_trainer= trainers.index(trainer)
            temp_list[1] = index_horse
            temp_list[5] = index_jokey
            temp_list[6] = index_owner
            temp_list[7] = index_trainer
            line = ""
            for a in temp_list:
                line = line +","+str(a)
            line = line[1:]
        
        line =line.replace("boy","")
        line =line.replace("boyun","0.33")
        line = line.replace("atbaşı","0.22")
        line = line.replace("baş","0.22")
        line = line.replace("burun","0.07")
        line = line.replace("yarımboy","0.5")
        
       


        outFile.write(line.replace(",,",",0,"))
    return 

def main():
    
    
    
   

    # datasette problem var
    path_to_the_raw_results = "C:\\Users\\AtakanPavilion\\Desktop\Atakan\\01.Work\\projects\\horse_racing\\data\\race_results_raw"
    date_S = date(2018,10,1)
    date_E = date(2021,3,1)
    create_dirs_for_each_date_at_given_location(path_to_the_raw_results,date_S,date_E)

    path_to_parsed_results = "C:\\Users\\AtakanPavilion\\Desktop\Atakan\\01.Work\\projects\\horse_racing\\data\\race_results_parsed\\"
    
   
   
    results = read_all_the_files_and_extract_all_the_info(path_to_the_raw_results,date_S,date_E)
    write_results_to_the_file(path_to_parsed_results+"read_raw_results.txt",results,date_S,date_E)
    parse_the_main_file(path_to_parsed_results+"read_raw_results.txt",path_to_parsed_results+"temp1.txt")
    horses , jokeys , owners , trainers = assing_ids_to_horses_jokeys_owners_trainers(path_to_parsed_results+"temp1.txt",path_to_parsed_results+"horse_ids.txt",path_to_parsed_results+"jokey_ids.txt",path_to_parsed_results+"owner_ids.txt",path_to_parsed_results+"trainer_ids.txt")
    substitute_names(path_to_parsed_results+"temp1.txt",path_to_parsed_results+"dataset_of_initial_info.txt",horses , jokeys , owners , trainers)
    return None





main()