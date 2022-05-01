import unittest
from credentials import Credentials

class Testclass(unittest.TestCase):
    def setUp(self):
        self.new_credentials = Credentials("Twitter", "themann", 12345)


    def tearDown(self):
        Credentials.app_details = []

    def test_init_credentials(self):
        self.assertEqual(self.new_credentials.appname, "Twitter")
        self.assertEqual(self.new_credentials.appusername, "themann")
        self.assertEqual(self.new_credentials.apppassword, 12345)    

    def test_save_Credentials(self):
        self.new_credentials.save_Credentials()
        self.assertEqual(len(Credentials.app_details), 1)    

    def test_delete_Credentials(self):
        self.new_credentials.save_Credentials()
        test_Credentials = Credentials("Facebook", "kairetu", 8899)
        test_Credentials.save_Credentials()
        test_Credentials.delete_Credentials("Facebook")
        self.assertTrue(len(Credentials.app_details)==1)
        
    def test_find_Credentials_by_appname(self):
        self.new_credentials.save_Credentials()
        test_Credentials = Credentials("Facebook", "kamware", 1010)
        test_Credentials.save_Credentials() 
        found_Credentials = Credentials.find_by_appname("Facebook") 
        self.assertTrue(found_Credentials)

    def test_credential_exists(self):
        self.new_credentials.save_Credentials()
        test_Credentials = Credentials("Facebook", "kamware", 1010)
        test_Credentials.save_Credentials() 
        credential_exist = Credentials.credentials_exists("Facebook") 
        self.assertTrue(credential_exist)

    def test_display_credentials(self):
        self.new_credentials.save_Credentials()
        test_Credentials = Credentials("Facebook", "kamware", 1010)
        test_Credentials.save_Credentials() 
        self.assertEqual(Credentials.display_credentials(), Credentials.app_details)
        
       





        




if __name__=="__main__":    
    unittest.main()
