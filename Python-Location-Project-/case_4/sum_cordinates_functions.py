
# CASE 4 sum distance on same MATRICULA property of each CORDINATES latitud longitud JSON object.

import json
import csv
from csv import reader
import string
from asyncio.windows_events import NULL
from vincenty import vincenty
from common.common_functions import Common_functions

# Open_with_sum_distances_of_cordinates_output function to read file and json sum distance of points cordinates from each same row ['Matricula'] 
def Open_with_sum_distances_of_cordinates_output(path):
    
    try:
        
        listArray = []
        ms = []
        
        with open(path, "r") as my_csv_f:
        
            print(' - [ UPCOMING STEP ] - Summing cordinates ...')
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
                

            # Sum of distances of cordinates of each l [] Matricula
            sum_cordinates = 0
            distance = 0
            for v in ms:
                for row in listArray:

                    j = json.dumps(row)
                    l = json.loads(j)
                    
                    if v == l['Matricula']:
                        
                        lat = float(l['Latitud'])
                        lon = float(l['Longitud'])

                        c = (lat,lon)
                        
                        if not sum_cordinates == 0:
                            
                            # Vincenty function to sum distances from two cordinates points 
                            distance = distance + vincenty(sum_cordinates, c)
                            sum_cordinates = c
                        else:
                            sum_cordinates = c    

                print(' -- [ MATRICULA  :  ', v ,' ] -- [ SUM of CORDINATES  :  ', distance, ' ] --')
                print('-----------------------------------------------------------------------------------------------------------------------------------------------------')
                sum_cordinates = 0
                distance = 0
            
            print(' ')
            print(' - [ STEP COMPLETED ] - Sum [ CORDINATES ] from each [ MATRICULA ] Completed! ')
            print(' ')
            print(' ')
    except:
        
        print(' ')
        print('##########################################################################################################################################################')
        print('#######################################################################. No such a file found! .##########################################################')
        print('##########################################################################################################################################################')
        print(' ')
        print(' ')