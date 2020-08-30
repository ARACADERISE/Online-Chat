# Control/Have control on stuff going on within the website while the flask-server is running!
from database import _DATABASE_

class BACKEND_PREVIEW:

    def __init__(self):
        self.DB = _DATABASE_._RETURN_DB_(self)
    
    def _run_(self): print('running')

BACK = BACKEND_PREVIEW()
BACK._run_()