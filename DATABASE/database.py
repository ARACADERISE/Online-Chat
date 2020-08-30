import sqlite3, os, json

class _DATABASE_:

    def __init__(self):
        self.Database = sqlite3.connect('ChatDb.db')

        if not os.path.isfile('db_info.json'):
            self.HasCreatedTable = False
            self.DbInfo = {'TableCreated':self.HasCreatedTable}
        else:
            self.DbInfo = json.loads(open(os.path.abspath('db_info.json'),'r').read())
            self.HasCreatedTable = True
    
    def CreateTable(self):

        if self.HasCreatedTable:

            try:
                self.Database.execute('''SELECT SENT_CHAT FROM ChatDatabase''')
            except:
                # The file was erased internally
                self.HasCreatedTable = False

        if not self.HasCreatedTable:
            self.Database.execute('''
            CREATE TABLE ChatDatabase (
                SENT_CHAT TEXT,
                RECIEVED_CHAT TEXT,
                CHATS_TOTAL INT PRIMARY KEY NOT NULL
            );
            ''')

            self.DbInfo['TableCreated'] = True

            with open('db_info.json','w') as file:
                file.write(json.dumps(
                    self.DbInfo,
                    indent=2,
                    sort_keys=False
                ))
                file.flush()
                file.close()
    
    def _INSERT_(self, insertion_information):

        self.Database.execute(insertion_information)
        self.Database.commit()

    def _RETURN_DB_(self): return self.Database