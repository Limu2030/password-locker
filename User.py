from argparse import _AppendConstAction


class User:
    user_menu=[]
    def __init__(self, firstname, lastname, username, password):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password
