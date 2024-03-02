
# CASE 2 in output JSON object each file row.

import json
import csv
from csv import reader
import string

# Convert Dictionary to Json String and print
def Convert_Dictionary_to_Json(listArray):
    
    jsonString = json.dumps(listArray, indent=4)
    print(jsonString)


# Open_with_read_file_and_json_output function to read file and json Output 
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
                
            Convert_Dictionary_to_Json(listArray)

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