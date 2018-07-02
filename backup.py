__author__ = 'Olli'
__version__ = '0.1.0'
__maintainer__ = 'Olli'
__email__ = 'olli@csow.de'
__status__ = 'Development'

import os
import schedule
import time

def job():
    print("Still working...")
    
#schedule.every().minutes.do(job)
# schedule.every().monday.at("23:37").do(job)
# schedule.every().wednesday.at("13:15").do(job)
schedule.every(2).seconds.do(job)

while True:
     schedule.run_pending()
     time.sleep(1)


