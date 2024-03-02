# README 
#   This is a PYTHON PROJECT THAT I MADE WITH 7 CASES.
#   You can see as this Project full as id done 
#   Thanks!
#   
#   On Commits is each STEP on project .
#   
#   # - STEP 1 - CASE 1 - READ CSV FILE AND SHOW IT CONTENT
#    


from case_1.main_read_file import Read_file_case_
from case_2.main_read_file_in_output_json import Read_file_case_json_Output_
import asyncio

async def Start_program():
    
    print(' ')
    print(' ')
    print('############################################################################################################################################################')
    print('#######################################################################. HELLO TO THIS PYTHON APP .#########################################################')
    print('############################################################################################################################################################')
    print(' ')
    print(' ')    

async def End_program():
    
    print(' ')
    print(' ')
    print('############################################################################################################################################################')
    print('#######################################################################. END FROM FROM THIS PYTHON APP .####################################################')
    print('############################################################################################################################################################')
    print(' ')
    print(' ')
    
# START PRORGAM 
asyncio.run(Start_program())

# CASE 1
asyncio.run(Read_file_case_.Main_case_1())

# CASE 2
asyncio.run(Read_file_case_json_Output_.Main_case_2())

# END PROGRAM 
asyncio.run(End_program())
