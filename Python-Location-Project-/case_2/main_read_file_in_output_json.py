

# ########## Read File with JSON output Case 2 #############
#  This file attempts to read existing file from C:/ Unit location and show his content as on CASE 1, on Json object each row file. 




from bg_colors import bg_colors
from common.common_functions import Common_functions
from case_2.in_output_json_functions import Open_with_read_file_and_json_output

class Read_file_case_json_Output_:


    # Main while when STEP is not completed 
    
    async def Main_case_2():
        
        print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')
        print('////////////////////////////////////////////////////////////////////////////// CASE 2 //////////////////////////////////////////////////////////////////////')
        print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')
        print(' ')
        print(' ')
    
        Y = False
        while True:
    
            C = 'C:/'
            x = C + input(' - [ KEY_1 ] - Enter a file name: ')
            print(' ')
            print(' ')

            Open_with_read_file_and_json_output(x)
            Y = Common_functions.is_key(Y)
    
            if Y == False:
                break

           
        # END STEP read file with Json output END CASE 2
        print(' ')
        print(' ')
        print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')
        print('////////////////////////////////////////////////////////////////////////////// END CASE 2 //////////////////////////////////////////////////////////////////')
        print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')
        print(' ')
        print(' ')