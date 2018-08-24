import unittest # Importing the unittest module
from user import User # Importing the user class
from credential import Credential # importing the credential class

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

    # def test_saveCredential(self):
    #     '''
    #     test_saveCredential test case to test if the credential object is saved into the credential_list
    #     '''

    #     self.newCredential.saveCredential() 
    #     self.assertEqual(len(Credential.credential_list),1)    

if __name__=='__main__': # provides a command line interface that collects all the tests methods and executes them
    unittest.main()

        


    