from flask_restful import Resource
from flask import request

from src import Quote

class SingleQuote(Resource):
    def get(self, user):
        response = {}
        i = 1
        myList = list(Quote.query.filter_by(username=user).all())
        for quote in myList:
            response['quote' + str(i)] = quote.message
            i = i + 1

        return response
