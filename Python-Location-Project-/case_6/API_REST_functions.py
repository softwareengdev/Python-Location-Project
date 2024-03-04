
# CASE 6 max time position on MATRICULA property from GET API_REST.

import os
import csv
import json
from csv import reader
from datetime import datetime
from common.common_functions import Common_functions


# GET_Max_time_from_matricula function to read file and return max time position from ['Matricula'] on max_times.txt
def GET_Max_time_from_matricula(v):
    
    try:

        W = 'max_times.txt' 
        
        my_lines = []
        max_time = ''
        
        with open(W, "r") as my_csv_f:
        
            print(' - [ UPCOMING STEP ] - Reading file ...')
            print(' ')
            print(' ')
            
            t = my_csv_f.readlines()[2:]
            for s in t:
                
                string = '{' + s.rstrip('\n') + '}'
                line = json.loads(string)
                my_lines.append(line)
            
            for r in my_lines:
                
                if r['Matricula'] == v:
                    max_time = r['Max_date']

            print(' ')
            print(' ')
            print(' - [ STEP COMPLETED ] - Retunr Max_time on [ MATRICULA ] Completed! ')
            print(' ')
            print(' ')
            print('-----------------------------------------------------------------------------------------------------------------------------------------------------')
            print('-----------------------------------------------------------------------------------------------------------------------------------------------------')
            
            return max_time
    except:
        
        print(' ')
        print('##########################################################################################################################################################')
        print('#######################################################################. No such a file found! .##########################################################')
        print('##########################################################################################################################################################')
        print(' ')
        print(' ')