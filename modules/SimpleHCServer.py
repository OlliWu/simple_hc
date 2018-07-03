from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import socket
import sys
from filelock import Timeout, FileLock

class testHTTPServer_RequestHandler(BaseHTTPRequestHandler) :

        # GET
    def do_GET(self):
        
        # Send response status code
        # if not mainlock.is_locked:
        #     print('{} seems to be unlocked. terminate.'.format(mainlock.lock_file))
        #     #self.send_response(404, message='healthcheck failed')
        #     self.send_error(404,
        #                     message='Healthcheck failed', 
        #                     explain='{} seems to be unlocked. terminate.'.format(mainlock.lock_file))
        # else:
        #Send message back to client
        message = str(threading.main_thread().is_alive())
        self.send_response(200)
        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
            
        return


def run(my_srv_adress, my_port):
    print("Starting Server...")
    print(threading.main_thread)
    print(threading.main_thread().is_alive())
    server_address = (my_srv_adress, my_port)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    httpd.serve_forever(poll_interval=5)
    

    

    
    