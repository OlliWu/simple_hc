from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import socket
import sys

class testHTTPServer_RequestHandler(BaseHTTPRequestHandler) :

        # GET
    def do_GET(self):
        
        # Send response status code
        if not self.get_connect(self.hc_host, self.hc_port):
            print('Could not connect to {}:{}'.format(self.hc_host, self.hc_port))
            #self.send_response(404, message='healthcheck failed')
            self.send_error(404,
                            message='Healthcheck failed', 
                            explain='Could not connect to {}:{}'.format(self.hc_host, self.hc_port))
        else:
            # Send message back to client
            message = 'connected to {}:{}'.format(self.hc_host, self.hc_port)
            self.send_response(200)
            # Send headers
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            # Write content as utf-8 data
            self.wfile.write(bytes(message, "utf8"))
            

        
        return

    def get_connect(self, host, port):
        get_connect_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       
        try:
            get_connect_sock.connect((host, port))
            print('connected')
        except socket.error:
            print(host, port)
            print('cant connect')
            sys.exit()
        finally:
            print('closing connection')
            get_connect_sock.close()
        
        return True



def get_lock(host, port):
    get_lock._lock_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        get_lock._lock_socket.bind((host, port))
        get_lock._lock_socket.listen(5)
        print('I got the lock')
    except socket.error:
        print('lock exists')
        sys.exit()

def run(my_srv_adress, my_port, hc_port):
    print("Starting Server...")
    server_address = (my_srv_adress, my_port)
    testHTTPServer_RequestHandler.hc_port = hc_port
    testHTTPServer_RequestHandler.hc_host = my_srv_adress
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    httpd.serve_forever()
    

    
    