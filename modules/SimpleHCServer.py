from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

class testHTTPServer_RequestHandler(BaseHTTPRequestHandler) :

        # GET
    def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Send message back to client
        message = str(threading.active_count()) + str(threading.enumerate()) + str(threading.current_thread()) + str(threading.main_thread())
        
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        print(threading.active_count())

        return

def run(my_port):
    print("Starting Server...")
    server_address = ('', my_port)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    httpd.serve_forever()
        