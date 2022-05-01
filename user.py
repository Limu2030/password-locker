
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
    def find_by_username(cls, username):
        for User in cls.user_menu:
            if User.username == username:
                return True
        return False        






