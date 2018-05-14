from apiconsumer.apiconsumer import APIConsumer
from domain.user import User

class CommandInterpreter(object):
    def interpretCommand(self, user, command):
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
            if parameter == '':
                return
            return str(user.username + ' has rolled a 1d') + str(parameter) + ' dice and got ' + str(apiConsumer.callGet('/rtd/' + parameter)) + '.'
        elif theCommand == 'dadjoke':
            return str(user.username + ' has called for a dad joke.\n') + str(apiConsumer.callGet('/dadjoke'))
        elif theCommand == 'quote':
            if command == theCommand:
                return str(user.username + ' has called for a random quote.\n') + apiConsumer.callGet('/quoting')
            else:
                parameter = command[i:]
                text = str(user.username + ' has called for quotes from ' + parameter + ': \n')
                response = apiConsumer.callGetDict('/quoting/' + parameter)
                for value in response.values():
                    text += '* ' + str(value) + '\n'
                return text
        elif theCommand == 'newquote':
            j = i
            param1 = ''
            for c in command[i:]:
                j = j + 1
                if c == ' ':
                    break
                param1 += c

            param2 = command[j:]

            parameters = { 'username' : str(param1), 'message' : str(param2) }
            return str(user.username + ' commited a new quote: ') + apiConsumer.callPost('/quoting', parameters, 'response')
