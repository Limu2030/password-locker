class Credentials: 
    app_details = []
    def __init__(self, appname,appusername, apppassword):
        self.appname = appname
        self.appusername = appusername
        self.apppassword = apppassword

    def save_Credentials(self):
        Credentials.app_details.append(self) 

    def delete_Credentials(self):
        Credentials.app_details.remove(self)
        