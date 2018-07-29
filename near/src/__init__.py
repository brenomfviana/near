from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/mourilo/Documentos/ufrn/pd/omegarest/src/database.db'
db = SQLAlchemy(app)

class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=False)
    message = db.Column(db.String(200), unique=True)

    def __init__(self, username, message):
        self.username = username
        self.message = message

    def __repr__(self):
        return '' + self.username + ': ' + self.message
