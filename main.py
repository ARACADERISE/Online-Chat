from DATABASE.database import _DATABASE_
from FLASK.website import FlaskWebApp

DATABASE = _DATABASE_()
DATABASE.CreateTable()
DATABASE._INSERT_('INSERT INTO ChatDatabase(SENT_CHAT,CHATS_TOTAL) VALUES("SEN!",1);')

WEBSITE = FlaskWebApp()
WEBSITE.RUN()
WEBSITE._Show_Homepage_()