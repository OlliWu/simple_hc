__author__ = 'Olli'
__version__ = '0.1.0'
__maintainer__ = 'Olli'
__email__ = 'olli@csow.de'
__status__ = 'Development'


import time
from modules import SimpleHCServer


my_port = 9001
host = '127.0.0.1'

# Provide Simple Healthcheck as own thread
SimpleHCServer.run_web(host, my_port)

# Do whatever you like... or just sleep
time.sleep(10)
