from flask_restful import Resource
from random import randint

class RollTheDice(Resource):
    def rollADice(self, higherBound):
        return {
            'response' : randint(1, higherBound)
        }

    def get(self, faces):
        return self.rollADice(faces)
