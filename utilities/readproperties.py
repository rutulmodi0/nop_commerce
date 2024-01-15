import configparser

config = configparser.RawConfigParser()
config.read("D:/nop_commerce/configurations/config.ini")


class ReadProperties:

    @staticmethod
    def getApplicationURL():
        url = config.get("common_cred", 'baseURL')
        return url

    @staticmethod
    def getuseremail():
        email = config.get("common_cred", 'useremail')
        return email

    @staticmethod
    def getpassword():
        password = config.get("common_cred", 'password')
        return password
