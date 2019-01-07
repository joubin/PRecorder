from flask import request
from flask_restful import Resource, reqparse
import json
import sqlite3
from PRecorder.Server import application


class Input(Resource):
    def __init__(self):
        self.conn = sqlite3.connect(__name__ + ".db")
        self.reqparser = reqparse.RequestParser()
        for argument in ['table', 'computer', 'content', 'user']:
            self.reqparser.add_argument(argument)

    def get(self, name):
        return "Server is up", 200

    application.route("/input")
    def post(self, name):
        try:
            table: str = request.form.get('table')
            # todo: add token field
            user: str = request.form.get('user')
            computer: str = request.form.get('computer')
            content: str = request.form.get('content')
            self.conn.cursor().execute("CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY AUTOINCREMENT, data_name "
                                       "STRING, computer STRING, user STRING,  content STRING);")
            self.conn.cursor().executemany('INSERT INTO data (data_name, computer,  user ,  content ) VALUES (?,?,?,?)',
                                           ([table, computer, user, content],))
            self.conn.commit()
            return "OK", 200
        except:
            return "Something went wrong", 500

    def put(self, name):
        pass

    def delete(self, name):
        pass
