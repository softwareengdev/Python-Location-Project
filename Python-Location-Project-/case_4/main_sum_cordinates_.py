


#



# ########## Read File with json sum of LATITUD LONGITUD cordinates of each MATRICULA property output Case 4 #############
#  This file attempts to read existing file from C:/ Unit location and show his content from json as sum of cordinates. 


from bg_colors import bg_colors
from common.common_functions import Common_functions
from case_4.sum_cordinates_functions import Open_with_sum_distances_of_cordinates_output

class Read_file_case_sum_distances_of_cordinates_:


    # Main while when STEP is not completed or not Start. 
    
    async def Main_case_4():
        
        print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')
        print('////////////////////////////////////////////////////////////////////////////// CASE 4 //////////////////////////////////////////////////////////////////////')
        print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')
        print(' ')
        print(' ')
    
        Y = False
        while True:
    
            C = 'C:/reto.csv'
            S = ' - [ KEY_START ] - Do you want to start sum of cordinates on reto.csv file? Press Key - Yes [ Enter ] - : '
            
            Y = Common_functions.is_key_Start(Y, S)
            if Y == False:
                break
            
            Open_with_sum_distances_of_cordinates_output(C)

           
        # END STEP read file with sum of cordinates output END CASE 4
        print(' ')
        print(' ')
        print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')
        print('////////////////////////////////////////////////////////////////////////////// END CASE 4 //////////////////////////////////////////////////////////////////')
        print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')
        print(' ')
        print(' ')