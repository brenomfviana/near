from flask_restful import Resource
from flask import request

import requests

class DadJoke(Resource):
    def get(self):
        headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        response = requests.get("https://icanhazdadjoke.com/", None, headers=headers)

        data = response.json()

        return{
            'response' : data['joke']
        }
