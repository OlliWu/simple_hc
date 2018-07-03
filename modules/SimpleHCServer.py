__author__ = 'Olli'
__version__ = '0.1.0'
__maintainer__ = 'Olli'
__email__ = 'olli@csow.de'
__status__ = 'Development'

from http.server import BaseHTTPRequestHandler, HTTPServer
import threading


class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

    # GET
    def do_GET(self):
        
        # Send response status code
        if not threading.main_thread().is_alive():
            print('MainThread seems to be down. Terminate.')
            # self.send_response(404, message='healthcheck failed')
            self.send_error(404,
                            message='Healthcheck failed', 
                            explain='MainThread down')
        else:
            # Send message back to client
            message = str(threading.main_thread().is_alive())
            self.send_response(200)
            # Send headers
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            # Write content as utf-8 data
            self.wfile.write(bytes(message, "utf8"))
            
        return


def run_web(my_srv_adress, my_port):
    print("Starting Server...")
    server_address = (my_srv_adress, my_port)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    
    server_thread = threading.Thread(target=httpd.serve_forever)
    server_thread.daemon = False
    server_thread.start()


