class User(object):
    def __init__(self, username, language):
        self.username = username
        if language == 'English':
            self.language = 'en'
        elif language == 'Português Brasileiro':
            self.language = 'pt'
        elif language == 'Français':
            self.language = 'fr'
        elif language == 'Español':
            self.language = 'es'
        elif language == 'Italiano':
            self.language = 'it'
        elif language == 'Deutsch':
            self.language = 'de'
        elif language == 'Nederlands':
            self.language = 'nl'
        else:
            self.language = 'pt'
