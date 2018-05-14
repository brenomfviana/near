from flask_restful import Resource
from flask import request
from random import randint

from src import db
from src import Quote

class RandomQuote(Resource):
    def get(self):
        quote = Quote.query.get(randint(1, Quote.query.count()))
        return {
            'response' : quote.username + ' once said: ' + quote.message
        }

    def post(self):
        username = request.json['username']
        message = request.json['message']

        quote = Quote(username, message)
        db.session.add(quote)
        db.session.commit()

        return {
            'response' : 'Quote successfully commited!'
        }
