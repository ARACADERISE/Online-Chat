from DATABASE.database import _DATABASE_
from FLASK.website import FlaskWebApp

DATABASE = _DATABASE_()
DATABASE.CreateTable()

WEBSITE = FlaskWebApp()
WEBSITE.RUN()
WEBSITE._Show_Homepage_()