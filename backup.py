import os
import schedule
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading


BCK_TIME = os.environ.get('BCKTIME', '18:34')
BCK_DIR = os.environ.get('BCKDIR', '/tmp')


class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

    # GET
    def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Send message back to client
        message = "OK"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return

def run():
    print("Starting Server...")
    server_address = ('', 8001)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    httpd.serve_forever()

threading.Thread(target=run).start()



print("Server still running...")


def job():
    print("I'm working...")
    print("Still working...")
    #app.logger.info('logger still working...')
    #app.logger.debug('logger debug working...')
    #sys.stdout.flush()
    #sys.stderr.flush()

schedule.every().minutes.do(job)
schedule.every().monday.at("23:37").do(job)
schedule.every().wednesday.at("13:15").do(job)

schedule.every(2).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)


