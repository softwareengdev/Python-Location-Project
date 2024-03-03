
# CASE 3 sum distance on same MATRICULA property in output JSON object each.

import json
import csv
from csv import reader
import string
from common.common_functions import Common_functions

# Open_with_sum_of_distances_output function to read file and json sum distance outup from each row ['Matricula'] 
def Open_with_sum_of_distances_output(path):
    
    try:
        
        listArray = []
        ms = []
        
        with open(path, "r") as my_csv_f:
        
            print(' - [ UPCOMING STEP ] - Summing distances ...')
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
                

            # Sum of distances of each l [] Matricula
            sum_distances = 0
            for v in ms:
                for row in listArray:
                    
                    j = json.dumps(row)
                    l = json.loads(j)
                    
                    if v == l['Matricula']:
                        f = float(l['Distance'])
                        sum_distances = sum_distances + f

                print(' -- [ MATRICULA  :  ', v ,' ] -- [ SUM of DISTANCES  :  ', sum_distances, ' ] --')
                print('-----------------------------------------------------------------------------------------------------------------------------------------------------')
                sum_distances = 0
            
            print(' ')
            print(' - [ STEP COMPLETED ] - Sum [ DISTANCE ] from each [ MATRICULA ] Completed! ')
            print(' ')
            print(' ')
    except:
        
        print(' ')
        print('##########################################################################################################################################################')
        print('#######################################################################. No such a file found! .##########################################################')
        print('##########################################################################################################################################################')
        print(' ')
        print(' ')