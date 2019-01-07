from flask import Flask


from flask import request
from flask_restful import reqparse
import sqlite3

application = Flask(__name__)

reqparser = reqparse.RequestParser()
for argument in ['table', 'computer', 'content', 'user']:
    reqparser.add_argument(argument)

@application.route("/")
def get():
    return "Server is up", 200

@application.route('/')
def index():
    return 'Index Page'

@application.route("/input/", methods=['POST'])
def post():
    print("asd")
    try:
        table: str = request.form.get('table')
        # todo: add token field
        user: str = request.form.get('user')
        computer: str = request.form.get('computer')
        content: str = request.form.get('content')
        with sqlite3.connect(__name__ + ".db") as conn:
            conn.cursor().execute("CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY AUTOINCREMENT, data_name "
                                       "STRING, computer STRING, user STRING,  content STRING);")
            conn.cursor().executemany('INSERT INTO data (data_name, computer,  user ,  content ) VALUES (?,?,?,?)',
                                           ([table, computer, user, content],))
            conn.commit()
        return "OK", 200
    except Exception as e:
        print(e)
        return "Something went wrong", 500


def put(self, name):
    pass


def delete(self, name):
    pass


if __name__ == '__main__':
    application.run()
