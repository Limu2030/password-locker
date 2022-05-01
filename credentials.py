

class Credentials: 
    app_details = []
    def __init__(self, appname, appusername, apppassword):
        self.appname = appname
        self.appusername = appusername
        self.apppassword = apppassword

    def save_Credentials(self):
        Credentials.app_details.append(self) 

    @classmethod
    def delete_Credentials(cls, platform):
        for credential in cls.app_details:
            if credential.appname == platform:
                Credentials.app_details.remove(credential)
                return         


    @classmethod
    def find_by_appname(cls, appname):
        for Credentials in cls.app_details:
            if Credentials.appname == appname:
                return Credentials

    @classmethod
    def credentials_exists(cls, platform):
        for credential in cls.app_details:
            if credential.appname == platform:
                return True
        return False

    @classmethod 
    def display_credentials(cls):
        return cls.app_details                    
