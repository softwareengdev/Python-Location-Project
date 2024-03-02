
# ########## Read File Case 1 #############
#  This file attempts to read existing file from C:/ Unit location and show his content. 


from bg_colors import bg_colors
from common.common_functions import Common_functions
from case_1.read_file_functions import Open_with_read_file

class Read_file_case_:


    # Main while when STEP is not completed 
    
    async def Main_case_1():
        
        print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')
        print('////////////////////////////////////////////////////////////////////////////// CASE 1 //////////////////////////////////////////////////////////////////////')
        print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')
        print(' ')
        print(' ')
    
        Y = False
        while True:
    
            C = 'C:/'
            x = C + input(' - [ KEY_1 ] - Enter a file name: ')
            print(' ')
            print(' ')

            Open_with_read_file(x)
            Y = Common_functions.is_key(Y)
    
            if Y == False:
                break

           
        # END STEP read file END CASE 1
        print(' ')
        print(' ')
        print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')
        print('////////////////////////////////////////////////////////////////////////////// END CASE 1 //////////////////////////////////////////////////////////////////')
        print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')
        print(' ')
        print(' ')