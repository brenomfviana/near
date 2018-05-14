from apiconsumer.apiconsumer import APIConsumer

class CommandInterpreter(object):
    def interpretCommand(self, command):
        apiConsumer = APIConsumer()
        theCommand = ''
        i = 0
        for c in command:
            if c != ' ':
                theCommand += c
                i = i + 1
            else:
                i = i + 1
                break

        if theCommand == 'rtd':
            parameter = command[i:]
            print(apiConsumer.callGet('/rtd/' + parameter))
        elif theCommand == 'dadjoke':
            print(apiConsumer.callGet('/dadjoke'))
        elif theCommand == 'quote':
            print('TODO')
