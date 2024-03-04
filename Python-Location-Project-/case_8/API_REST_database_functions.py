
# CASE 6 max time position on MATRICULA property from GET API_REST.

from math import e
import os
import csv
import json
import pyodbc
from csv import reader
from datetime import datetime
from common.common_functions import Common_functions


# GET_Max_time_from_matricula function to read database and return max time position from ['Matricula'] on max_times.txt
def GET_Max_time_from_matricula_from_database(v):
    
    try:
        
        my_lines = []
        max_time = ''        
        
        print(' - [ UPCOMING STEP ] - Connecting Database ...')
        print(' ')
        print(' ')

        server_name = '(localdb)\MSSQLLocalDB'
        db_name = 'PYTHON_PROJECT'
        
        SERVER = '(localdb)\MSSQLLocalDB'
        DATABASE = 'PYTHON_PROJECT'
        USERNAME = '<username>'
        PASSWORD = '<password>'


        conn = pymssql.connect(server, user, password, "tempdb")
        cursor = conn.cursor(as_dict=True)

        cursor.execute('SELECT * FROM [MAX_TIMES] WHERE [MAX_TIMES].[Matricula] = ' + str(v))
        for row in cursor:
            print("ID=%d, Name=%s" % (row['id'], row['name']))

        conn.close()

        # Example: Execute a SELECT query
        cursor.execute('SELECT * FROM [MAX_TIMES] WHERE [MAX_TIMES].[Matricula] = ' + str(v))

        # Fetch and print the results
        for r in cursor:
                 
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
    except Exception as e:
        
        print(e.message)
        print(' ')
        print('##########################################################################################################################################################')
        print('#######################################################################. No such a file found! .##########################################################')
        print('##########################################################################################################################################################')
        print(' ')
        print(' ')