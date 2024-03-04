


#



# ########## API_REST GET with Matricula parameter to show max time position property on format yyy/mm/dd HH:MM:SS output Case 6 #############
#  This file attempts to read existing file from Project Unit location and return on GET max position time for each Matricula in API_REST. 


from bg_colors import bg_colors
from common.common_functions import Common_functions
from case_6.API_REST_functions import GET_Max_time_from_matricula

    
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
            
            resp = f"<html><body><h1> Do GET Http Request with localhost:8080/'Matricula' . WHERE ' Matricula is number to identify Max_time' </h1></body></html>"
        elif not url.path == '/favicon.ico':
            
            v = url.path[1:]
            resp = GET_Max_time_from_matricula(v)
            if resp == '':
                resp = f"<html><body><h1> Matricula : {v} : [ NOT FOUND ] </h1></body></html>"
            else:
                resp = f"<html><body><h1> - Max_Time </h1><h1>[ Matricula : {v} ]</h1><h1>[ MAX_TIME : {resp} ] </h1></body></html>"
        
        self._set_headers()
        self.wfile.write(resp.encode())
        

class API_REST_Get_max_time_:

    # Main while when STEP is not completed or not Start. 
    
    async def Main_case_6():
        
        print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')
        print('////////////////////////////////////////////////////////////////////////////// CASE 6 //////////////////////////////////////////////////////////////////////')
        print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')
        print(' ')
        print(' ')

        Y = False
        while True:
    
            C = 'C:/reto.csv'
            print('-----------------------------------------------------------------------------------------------------------------------------------------------------')
            print('-----------------------------------------------------------------------------------------------------------------------------------------------------')
            S = ' - [ KEY_START ] - Do you want to start API_REST? Press Key - Yes [ Enter ] - : '
            
            Y = Common_functions.is_key_Start(Y, S)
            if Y == False:
                break
            
            if __name__ == 'case_6.main_API_REST_':
                try:
                    
                    server_address = ('localhost', 8080)
                    httpd = HTTPServer(server_address, MyRequestHandler)
            
                    print('Server is running on http://localhost:8080/ ...')
                    httpd.serve_forever()
            
                except KeyboardInterrupt:
            
                    print('Server stopped...')
                    httpd.server_close()
                    pass


        # END STEP read file with max position time output END CASE 6
        print(' ')
        print(' ')
        print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')
        print('////////////////////////////////////////////////////////////////////////////// END CASE 6 //////////////////////////////////////////////////////////////////')
        print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')
        print(' ')
        print(' ')