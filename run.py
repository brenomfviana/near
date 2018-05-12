from flask import Flask
from flask_restful import Api

from api.rollthedice import RollTheDice
from api.chattranslator import ChatTranslator

app = Flask(__name__)
api = Api(app)

api.add_resource(RollTheDice, "/rtd/<int:faces>")
api.add_resource(ChatTranslator, "/translate")

app.run()
