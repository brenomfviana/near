from apiconsumer import APIConsumer

apiConsumer = APIConsumer()
parameters = { 'message' : 'Oi, tudo bem?', 'dstLanguage' : 'en', 'srcLanguage' : 'pt' }
print(apiConsumer.callPost('/translate', parameters, 'translatedTo'))
print(apiConsumer.callGet('/dadjoke'))
print(apiConsumer.callGetDict('/rtd/6'))
