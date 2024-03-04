# README 
#   This is a PYTHON PROJECT THAT I MADE WITH 7 CASES.
#   You can see as this Project full as is done 
#   Thanks!
#   
#   On Commits is each STEP on project .
#   
#   # - STEP 1 - CASE 1 - READ CSV FILE AND SHOW IT CONTENT
#   # - STEP 2 - CASE 2 - READ CSV FILE AND SHOW IT CONTENT ON JSON FORMAT
#   # - STEP 3 - CASE 3 - READ CSV FILE ON JSON FORMAT AND SHOW SUMMING OF DISTANCES ON EACH MATRICULA
#   # - STEP 4 - CASE 4 - READ CSV FILE AND SHOW SUM OF DISTANCES ON EACH MATRICULA
#   # - STEP 5 - CASE 5 - WRITE NEW TXT FILE WITH MAX TIME ON EACH MATRICULA
#   # - STEP 6 - CASE 6 - START SERVER ON LOCALHOST:8080 AND RETURN FROM FILE MAX TIME FOR EACH MATRICULA
#    


from case_1.main_read_file import Read_file_case_
from case_2.main_read_file_in_output_json import Read_file_case_json_Output_
from case_3.main_sum_distances_ import Read_file_case_sum_distances_
from case_4.main_sum_cordinates_ import Read_file_case_sum_distances_of_cordinates_
from case_5.main_max_time_position_ import Write_file_with_max_time_position_
from case_6.main_API_REST_ import API_REST_Get_max_time_
from case_8.main_API_REST_database import API_REST_database_Get_max_time_

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

# CASE 3
asyncio.run(Read_file_case_sum_distances_.Main_case_3())

# CASE 4
asyncio.run(Read_file_case_sum_distances_of_cordinates_.Main_case_4())

# CASE 5
asyncio.run(Write_file_with_max_time_position_.Main_case_5())

# CASE 6
try:
    asyncio.run(API_REST_Get_max_time_.Main_case_6())
except:
    pass

# CASE 7
#asyncio.run(.Main_case_7())

# CASE 6
try:
    asyncio.run(API_REST_database_Get_max_time_.Main_case_8())
except:
    pass

# END PROGRAM 
asyncio.run(End_program())
