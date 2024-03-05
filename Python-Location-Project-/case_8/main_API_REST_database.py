


#



# ########## API_REST GET with Matricula parameter to show max time position property on format yyy/mm/dd HH:MM:SS output from DATBASE Case 8 #############
#  This file attempts to read existing database Unit location and return on GET max time position for each Matricula in API_REST from DATABASE. 


from bg_colors import bg_colors
from common.common_functions import Common_functions
from case_8.API_REST_database_functions import GET_Max_time_from_matricula_from_database

    
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

            
class MyRequestHandler(BaseHTTPRequestHandler):
    
    def _set_headers(self):
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):

        url = urlparse(self.path)
        resp = ''
        if url.path == '/':
            
            resp = f"<html><body><h1> Do GET Http Request with localhost:8088/'Matricula' . WHERE ' Matricula is number to identify Max_time' </h1></body></html>"
        elif not url.path == '/favicon.ico':
            
            v = url.path[1:]
            resp = GET_Max_time_from_matricula_from_database(v)
            if resp == '':
                resp = f"<html><body><h1> Matricula : {v} : [ NOT FOUND ] </h1></body></html>"
            else:
                resp = f"<html><body><h1> - Max_Time </h1><h1>[ Matricula : {v} ]</h1><h1>[ MAX_TIME : {resp} ] </h1></body></html>"
        
        self._set_headers()
        self.wfile.write(resp.encode())

class API_REST_database_Get_max_time_:

    # Main while when STEP is not completed or not Start. 
    
    async def Main_case_8():
        
        print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')
        print('////////////////////////////////////////////////////////////////////////////// CASE 8 //////////////////////////////////////////////////////////////////////')
        print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')
        print(' ')
        print(' ')

        Y = False
        while True:
    
            C = 'C:/reto.csv'
            print('-----------------------------------------------------------------------------------------------------------------------------------------------------')
            print('-----------------------------------------------------------------------------------------------------------------------------------------------------')
            S = ' - [ KEY_START ] - Do you want to start API_REST from Database? Press Key - Yes [ Enter ] - : '
            
            Y = Common_functions.is_key_Start(Y, S)
            if Y == False:
                break
            
            if __name__ == 'case_8.main_API_REST_database':
                try:
                    
                    server_address = ('localhost', 8088)
                    httpd = HTTPServer(server_address, MyRequestHandler)
            
                    print('Server is running on http://localhost:8088/ ...')
                    httpd.serve_forever()
            
                except KeyboardInterrupt:
            
                    print('Server stopped...')
                    httpd.server_close()
                    pass


        # END STEP read database with max position time output END CASE 8
        print(' ')
        print(' ')
        print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')
        print('////////////////////////////////////////////////////////////////////////////// END CASE 8 //////////////////////////////////////////////////////////////////')
        print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')
        print(' ')
        print(' ')