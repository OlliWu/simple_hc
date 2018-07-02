__author__ = 'Olli'
__version__ = '0.1.0'
__maintainer__ = 'Olli'
__email__ = 'olli@csow.de'
__status__ = 'Development'

import os
import sys
import socket
import schedule
import time
import threading
from modules import SimpleHCServer

my_port = 9001
host = ''
port = 50007

#Provide Simple Healthcheck as own thread
#threading.Thread(target=SimpleHCServer.run(my_port)).start()



def job():
    print("Still working...")
    print(threading.active_count())
    print(threading.enumerate())
#    print(bck.name)

#schedule.every().minutes.do(job)
# schedule.every().monday.at("23:37").do(job)
# schedule.every().wednesday.at("13:15").do(job)
schedule.every(2).seconds.do(job)

def dobackup():
    while True:
        schedule.run_pending()
        time.sleep(1)

def get_lock(backup):
    get_lock._lock_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        get_lock._lock_socket.bind((host, port))
        print('I got the lock')
    except socket.error:
        print('lock exists')
        sys.exit()

get_lock('running_test')


#do backup
bck = threading.Thread(target=dobackup(), name='Backup').start()




