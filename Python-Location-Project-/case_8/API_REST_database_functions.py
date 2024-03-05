
# CASE 8 max time position on MATRICULA property from GET API_REST_ FROM DATABASE.

from math import e
import os
import csv
import json
import pyodbc
import pymssql
from csv import reader
from datetime import datetime
from common.common_functions import Common_functions


# GET_Max_time_from_matricula_from_database function to read database and return max time position from ['Matricula'] on max_time.
def GET_Max_time_from_matricula_from_database(v):
    
    try:
        
        max_time = ''        
        
        print(' - [ UPCOMING STEP ] - Connecting Database ...')
        print(' ')
        print(' ')

        connection = pyodbc.connect(f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER=(localdb)\MSSQLLocalDB;DATABASE=PYTHON_PROJECT;UID=;PWD=')
        cursor = connection.cursor()

        sql_string = 'SELECT [Matricula] ,[Max_date] FROM [dbo].[MAX_TIMES] WHERE [Matricula] = \'' + str(v) + '\''

        # Execute a SELECT query
        cursor.execute(sql_string)
            
        
        # Fetch and print the results
        for row in cursor:
            print('GET RECORD FROM DATABASE OK: ', str(row[0]), str(row[1]))

            if row[0] == v:
                max_time = row[1]

            print(' ')
            print(' ')
            print(' - [ STEP COMPLETED ] - Retunr Max_time on [ MATRICULA ] Completed! ')
            print(' ')
            print(' ')
            print('-----------------------------------------------------------------------------------------------------------------------------------------------------')
            print('-----------------------------------------------------------------------------------------------------------------------------------------------------')
            
        connection.close()
        return max_time
    
    except Exception as e:
        
        print(e.message())
        print(' ')
        print('##########################################################################################################################################################')
        print('#######################################################################. No such a file found! .##########################################################')
        print('##########################################################################################################################################################')
        print(' ')
        print(' ')