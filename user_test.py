import unittest # Importing the unittest module
import pyperclip,sys
from user import User
from credential import Credential# Importing the user and credential class


class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours

    Args:
    unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self): # setUp helps us to define instructions that will be executed before each test method

        '''
        set up method to run before each test cases
        '''
        self.newUser = User("Yvonne","yvonneojijo")
# create an object for the user
    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.newUser.userName,"Yvonne") # the seif.assertEqual() method checks for the expected results.
        self.assertEqual(self.newUser.password,"yvonneojijo")


    def test_save_user(self): # this calls the saveUser()method
        '''
        test_save_user test case to test if the user object is saved into thee user list
        '''
        self.newUser.saveUser() # saving the new user input
        self.assertEqual(len(User.user_list),1)

    def tearDown(self):
        '''
        tearDown method that does clean up each test case has run
        '''
        User.user_list = []

    def test_save_multipleUser(self):
        '''
        test_save_mutipleUser to check if we can save multiple user objects to our user_list
        '''
        self.newUser.saveUser()
        testUser = User("Yvonne","yvonneojijo") # this is a new credential
        testUser.saveUser()
        self.assertEqual(len(User.user_list),2)     

class TestCredential(unittest.TestCase):
    '''
    Test class that defines test cases for the creddential class behaviours

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases
        '''
        self.newCredential = Credential("Diana","Oliver","facebook","pwd222") 
    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.newCredential.firstName,"Diana") # the self-assertEqual() method checks for an expected result
        self.assertEqual(self.newCredential.lastName,"Oliver")
        self.assertEqual(self.newCredential.accountName,"facebook")
        self.assertEqual(self.newCredential.password,"pwd222")

    def test_saveCredential(self):
        '''
        test_saveCredential test case to test if the credential object is saved into the credential_list
        '''

        self.newCredential.saveCredential() 
        self.assertEqual(len(Credential.credential_list),1) 

    def tearDown(self):
        '''
        tearDown method that does clean up each test case has run
        '''
        Credential.credential_list = []

    def test_save_multipleCredential(self):
        '''
        test_save_mutipleCredential to check if we can save multiple credential objects to our credential_list
        '''
        self.newCredential.saveCredential()
        testCredential = Credential("MaryLucky","Haron","twitter","12pass") # this is a new credential
        testCredential.saveCredential()
        self.assertEqual(len(Credential.credential_list),2)

    def test_deleteCredential(self):
        '''
        test_deleteCredential to test if we can remove a credential from our credential_list

        '''
        self.newCredential.saveCredential()
        testCredential = Credential("MaryLucky","Haron","twitter","12pass")
        testCredential.saveCredential()
        self.newCredential.deleteCredential() # Deleting a credential object 
        self.assertEqual(len(Credential.credential_list),1) 

    def test_findCredential_by_name(self):
        '''
        test to check if we can find a credential by lastName and display information 
        '''

        self.newCredential.saveCredential()
        testCredential = Credential("MaryLucky","Haron","twitter","12pass")
        testCredential.saveCredential()
        foundCredential = Credential.find_by_name("MaryLucky")
        self.assertEqual(foundCredential.accountName, testCredential.accountName)  

    def testCredential_exists(self):
        '''
        test to check if we can return a boolean if we cannot find the credential
        '''

        self.newCredential.saveCredential()
        testCredential = Credential("MaryLucky","Haron","twitter","12pass")
        testCredential.saveCredential()
        credential_exists = Credential.credential_exist("Haron")
        self.assertTrue(credential_exists)

    def test_displayAllCredentials(self):
        '''
        method that returns a list of all contacts saved
        '''

        self.assertEqual(Credential.displayCredentials(), Credential.credential_list) 

    def test_copy_accountName(self):
        '''
        test to confirm that we are copying the account from a found credential
        '''

        self.newCredential.saveCredential()
        Credential.copy_accountName("Diana")

        self.assertEqual(self.newCredential.accountName, pyperclip.paste())
          

           

if __name__=='__main__': # provides a command line interface that collects all the tests methods and executes them
    unittest.main()

        


    