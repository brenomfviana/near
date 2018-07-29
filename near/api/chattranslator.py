from flask_restful import Resource
from flask import request

from googletrans import Translator

class ChatTranslator(Resource):
    def post(self):
        message = request.json['message']
        dstLanguage = request.json['dstLanguage']
        srcLanguage = request.json['srcLanguage']

        translator = Translator()
        translatedMessage = translator.translate(message, dstLanguage, srcLanguage)
        return {
            'translatedTo' : translatedMessage.text
        }
