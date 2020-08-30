# Control/Have control on stuff going on within the website while the flask-server is running!
import sqlite3

class BACKEND_PREVIEW:

    def __init__(self):
        self.DB = sqlite3.connect('ChatDb.db')
    
    def _run_(self): print('running')

BACK = BACKEND_PREVIEW()
BACK._run_()