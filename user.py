
class User:
    user_menu=[]
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_User(self):
        User.user_menu.append(self)
        

    def delete_User(self):
        User.user_menu.remove(self)

    @classmethod
    def find_by_password(cls, password):
        for User in cls.user_menu:
            if User.password == password:
                return True
        return False        






