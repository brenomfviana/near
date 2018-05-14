from src import app
from flask_restful import Api

from api.rollthedice import RollTheDice
from api.chattranslator import ChatTranslator
from api.quoting.randomquote import RandomQuote
from api.quoting.singlequote import SingleQuote
from api.dadjoke import DadJoke

api = Api(app)

api.add_resource(RollTheDice, "/rtd/<int:faces>")
api.add_resource(ChatTranslator, "/translate")
api.add_resource(RandomQuote, "/quoting")
api.add_resource(SingleQuote, "/quoting/<string:user>")
api.add_resource(DadJoke, "/dadjoke")

app.run()
