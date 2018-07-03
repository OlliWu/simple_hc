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
#from filelock import Timeout, FileLock


my_port = 9001
host = '127.0.0.1'
hc_port = 50007

#Provide Simple Healthcheck as own thread
#SimpleHCServer.get_lock(host, hc_port)

SimpleHCServer.run_web(host, my_port)


# hc_server = threading.Thread(target=SimpleHCServer.run_web(host, my_port))
# hc_server.setDaemon(True)
# hc_server.start()



time.sleep(10)



#get_lock(my_srv_adress, hc_port)

# def job():
#     print("Still working...")
#    print(bck.name)

#schedule.every().minutes.do(job)
# schedule.every().monday.at("23:37").do(job)
# schedule.every().wednesday.at("13:15").do(job)
#schedule.every(2).seconds.do(job)

# def dobackup():
#     while True:
#         schedule.run_pending()
#         time.sleep(1)

#dobackup()









#do backup
#bck = threading.Thread(target=dobackup(), name='Backup').start()




