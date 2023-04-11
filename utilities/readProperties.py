import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:
    
    #static methods are used so that we dont need to pass any parameter
    @staticmethod
    def getAppURL():
        url = config.get('login info', 'baseURL')
        return url

    @staticmethod
    def getUsername():
        username = config.get('login info', 'username')
        return username
    
    @staticmethod
    def getUserPassword():
        password = config.get('login info', 'password')
        return password