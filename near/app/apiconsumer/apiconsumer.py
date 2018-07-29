import requests

class APIConsumer(object):
    def __init__(self, hostname='http://localhost', port='5000'):
        self.hostname = hostname
        self.port = port

    def callGet(self, path, fieldname='response'):
        response = requests.get(self.hostname + ':' + self.port + path)
        data = response.json()

        return data[fieldname]

    def callGetDict(self, path):
        response = requests.get(self.hostname + ':' + self.port + path)
        data = response.json()

        return data

    def callPost(self, path, parameters, fieldname='response'):
        response = requests.post(self.hostname + ':' + self.port + path, json=parameters)
        data = response.json()

        return data[fieldname]
