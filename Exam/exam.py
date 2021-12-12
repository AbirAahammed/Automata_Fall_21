from re import escape
import sqlite3
from flask import Flask, request
import json

class DBService():
    def __init__(self, db_file = 'exam.db') -> None:
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
    
    def getAll(self, tableName):
        self.cursor.execute('SELECT * FROM {}'.format(tableName))
        r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()]
        self.cursor.connection.close()
        return (r if r else None)

    def getByID(self, tableName, id):
        self.cursor.execute('SELECT * FROM {} WHERE id = {}'.format(tableName, id))
        r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()]
        self.cursor.connection.close()
        return (r[0] if r else None)

        
class Language_Service(object):
    def __init__(self) -> None:
        super().__init__()
    def get():
        return(DBService().getAll('Language'))

    def getLanguageByID(id):
        return(DBService().getByID('Language', id))
    
    def getLanguageByName(name):
        db = DBService()
        db.cursor.execute('''SELECT * FROM "Language" WHERE "language" = '{}' '''.format(name))
        r = [dict((db.cursor.description[i][0], value) for i, value in enumerate(row)) for row in db.cursor.fetchall()]
        db.cursor.connection.close()
        return (r[0] if r else None) 
    def insertLanguage(language_name, recognizable, decidable):
        db = DBService()
        db.cursor.execute('''INSERT INTO "Language"
                    ("language", recognizable, decidable)
                    VALUES('{}', {}, {});

'''.format(language_name, recognizable, decidable))
        db.connection.commit()
        db.connection.commit()

# res = Language.getLanguageByID(1)
# print(res)



app = Flask(__name__)

@app.route("/language", methods=['GET ', 'POST'])
def language():
    if request.method == 'GET':
        return json.dumps( Language_Service.get())
    elif request.method == 'POST':
        print(request.json)
        return "201"
@app.route("/language/<int:id>")
def get_language_by_id(id):
    return json.dumps(Language_Service.getLanguageByID(id))

@app.route("/language/<name>")
def get_language_by_name(name):
    return json.dumps(Language_Service.getLanguageByName(name))

app.run(port=8000)