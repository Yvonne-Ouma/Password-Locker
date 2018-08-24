import unittest # Importing the unittest module
from user import User # Importing the user class

class TestUser(unittest.TestCase):
    '''
    Test class that defines ntest cases for the user class behaviours

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

if __name__=='__main__': # provides a command line interface that collects all the tests methods and executes them
    unittest.main()

        


    