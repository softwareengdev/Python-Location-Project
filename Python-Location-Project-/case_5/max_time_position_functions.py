
# CASE 5 max time position on same MATRICULA property.

import os
import csv
import json
from csv import reader
from datetime import datetime
from common.common_functions import Common_functions


# Class Max_times.
class Max_times():

    def __init__(self):
        self.Matricula = None
        self.Max_date = None    

# Sort from datetime
def Sort_Max_times(max_times):
    sorted_max_times = sorted(max_times,key=lambda x: x.Max_date ,reverse=True)
    
    return sorted_max_times

# Format the timestamp object as desired (YYYYMMDD HH:mm:ss)
def POSIX_TimeStamp_to_format(pos_date):
    time = pos_date / 1000
    date_time_string = datetime.utcfromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')
    
    return date_time_string

# Delete file if exist and write new file with max time positions
def Write_with_max_position_time_file(max_times_f):
    

    print(' - [ UPCOMING STEP ] - Write new file ...')
    print(' ')
    print(' ')
    
    W = 'max_times.txt' 
    if os.path.exists(W):
        os.remove(W)
        
    my_new_f = open(W, 'w')
    my_new_f.write('    ------------------- NEW FILE WITH MAX TIMES POSITIONS -------------------\n')
    my_new_f.write(' ------------------- ------------------- -------------------  -------------------\n')
    
    for line in max_times_f:
        
        v = vars(line)
        my_new_f.write(', '.join(f"\"{key}\": \"{value}\"" for key, value in v.items()))
        my_new_f.write('\n')
        
    my_new_f.close()
    
# Write_with_max_position_time_ function to read file and write file max time position from each same row ['Matricula'] 
def Open_with_max_position_time_(path):
    
    try:
        
        listArray = []
        max_times = []
        ms = []
        
        with open(path, "r") as my_csv_f:
        
            print(' - [ UPCOMING STEP ] - Reading file ...')
            print(' ')
            print(' ')
            print('-----------------------------------------------------------------------------------------------------------------------------------------------------')
            print('-----------------------------------------------------------------------------------------------------------------------------------------------------')
            file = csv.DictReader(my_csv_f)
            for i in file:
                
                listArray.append(i)
                s = i['Matricula']
                
                if s not in ms:
                    ms.append(s)
                

            # max time position of each l [] Matricula
            max_time = 0
            time = 0
            for v in ms:
                for row in listArray:

                    j = json.dumps(row)
                    l = json.loads(j)
                    
                    if v == l['Matricula']:
                        
                        time = int(l['Pos_date'])
                            
                        if time > max_time or max_time == 0:
                            max_time = time
                print(' -- [ MATRICULA  :  ', v ,' ] -- [ MAX_TIME  :  DONE  ] --')
                print('-------------------------------------------------------------------------------------------------------------------------------')
                
                maximun = Max_times()
                maximun.Matricula = v
                maximun.Max_date = POSIX_TimeStamp_to_format(max_time)
                
                max_times.append(maximun)
                
                max_time = 0
                time = 0

            s = Sort_Max_times(max_times)
            Write_with_max_position_time_file(s)
            
            print(' ')
            print(' - [ STEP COMPLETED ] - Write max time posistion file from each reto.csv [ MATRICULA ] Completed! ')
            print(' ')
            print(' ')
    except:
        
        print(' ')
        print('##########################################################################################################################################################')
        print('#######################################################################. No such a file found! .##########################################################')
        print('##########################################################################################################################################################')
        print(' ')
        print(' ')