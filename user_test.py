import unittest
from user import User


class Testclass(unittest.TestCase):
    def setUp(self):
        self.new_user = User("John", 1234)
        


    def tearDown(self):
        User.user_menu = []
        

    def test_init_user(self):
        self.assertEqual(self.new_user.username, "John")
        self.assertEqual(self.new_user.password, 1234) 

    def test_init_credentials(self):
        self.assertEqual(self.new_credentials.appname, "Twitter")
        self.assertEqual(self.new_credentials.appusername, "themann")
        self.assertEqual(self.new_credentials.apppassword, 12345)    

    def test_save_user(self):
        self.new_user.save_User()
        self.assertEqual(len(User.user_menu), 1)    

    def test_delete_user(self):
        self.new_user.save_User()
        test_user = User("Mary", 8888)
        test_user.save_User()
        self.new_user.delete_User()
        self.assertTrue(len(User.user_menu)==1)
        
    def test_find_user_by_username(self):
        self.new_user.save_User()
        test_user = User("Mary", 8888)
        test_user.save_User() 
        found_user = User.find_by_username("Mary") 
        self.assertTrue(found_user)


        




if __name__=="__main__":    
    unittest.main()

