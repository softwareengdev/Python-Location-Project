
# CASE 2 in output JSON object each file row.

import json
import csv
from csv import reader
import string


def Convert_Csv_List_to_Json(listArray):
    
    jsonString = json.dumps(listArray, indent=4)

    print(jsonString)

    # j = json.loads(jsonString)
    
    # for item in j.items():
    #     print(item)

# Open_with_read_file function to read file 
def Open_with_read_file_and_json_output(path):
    
    try:
        
        listArray = []

        with open(path, "r") as my_csv_f:
        
            print(' - [ UPCOMING STEP ] - Reading input file...')
            print(' ')
            print(' ')
        
            file = csv.DictReader(my_csv_f)
            for i in file:
                
                listArray.append(i)
                
            Convert_Csv_List_to_Json(listArray)

            print(' ')
            print(' - [ STEP COMPLETED ] - File Read Completed! ')
            print(' ')
            print(' ')
    except:
        
        print(' ')
        print('##########################################################################################################################################################')
        print('#######################################################################. No such a file found! .##########################################################')
        print('##########################################################################################################################################################')
        print(' ')
        print(' ')