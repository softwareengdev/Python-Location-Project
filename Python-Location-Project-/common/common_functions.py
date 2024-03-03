

# Common functions on the project cases .

import json

class Common_functions:

    # Is_Key function to renew read file STEP
    def is_key(Y):
        renew = input(' - [ KEY_2 ] - Do you want to read a new file? Press KEY - Yes [ Y ] - : ')
        if renew == 'y' or renew == 'Y':
            Y = True
        else:
            Y = False
        return Y
        

    #   -----------------------------------------------------------------------------------------------------
        # Is_Key function to renew read file STEP
    def is_key_Start(Y, S):
        renew = input(S)
        if renew == '':
            Y = True
        else:
            Y = False
        return Y
        
    #   -----------------------------------------------------------------------------------------------------