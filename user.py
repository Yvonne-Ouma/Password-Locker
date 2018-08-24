class User :
    """
    class that generates new instances for a user to login
    """
    
    user_list = [] # an empty array where the propertis are ogoing ito be stored
    def __init__(self, userName, password):
        # '''
        # __init__ method that helps us define the properties of our user
        # Args:
        #     userName: New user userName
        #     password: New user password
        # '''    
            self.userName = userName
            self.password = password
    def saveUser(self):
        '''
        saveUser method saves contact objects into user_list
        '''

        User.user_list.append(self)        
 