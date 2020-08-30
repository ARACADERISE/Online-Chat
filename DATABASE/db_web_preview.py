# Control/Have control on stuff going on within the website while the flask-server is running!
import sqlite3

class BACKEND_PREVIEW:

    def __init__(self):
        self.DB = sqlite3.connect('ChatDb.db')
    
    def _run_(self): 
        information = self.DB.execute('SELECT SENT_CHAT FROM ChatDatabase')
        print('running %s ' % information)

BACK = BACKEND_PREVIEW()
BACK._run_()