# Control/Have control on stuff going on within the website while the flask-server is running!
import sqlite3

class BACKEND_PREVIEW:

    def __init__(self):
        self.DB = sqlite3.connect('ChatDb.db')
        self.DB = self.DB.cursor()
        self.is_running = True
    
    def _run_(self): 
        self.DB.execute('SELECT * FROM ChatDatabase')

        information = self.DB.fetchall()
        print(information)
        self.is_running = False
    
    def _is_running_(self): return self.is_running
    
    def _END_(self): return False

BACK = BACKEND_PREVIEW()

while BACK._is_running_():
    BACK._run_()