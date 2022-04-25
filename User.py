from argparse import _AppendConstAction

from requests import delete


class User:
    user_menu=[]
    def __init__(self, firstname, lastname, username, password):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password

    def save_User(self):
        User.user_menu.append(self)

    