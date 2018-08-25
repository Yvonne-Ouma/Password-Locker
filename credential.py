class Credential:
    '''
    Class that generates new instances of credentials
    '''

    credential_list = []
    def __init__(self,firstName,lastName,accountName,password):

        self.firstName = firstName
        self.lastName = lastName
        self.accountName = accountName
        self.password = password

    def saveCredential(self):

        '''
        saveCredential method saves contacts objects into credential_list
        '''

        Credential.credential_list.append(self)   

    def deleteCredential(self):
        '''
        deleteCredential method deletes a saved credential from the credential_list
        '''

        Credential.credential_list.remove(self)
    @classmethod
    def find_by_name(cls,name):
        '''
        Method that takes in a lastName and returns a credentil that matches that number
        
        Args:
            lastName: lastName to search for
        Returns :
        Credential of person that matches the number
        '''   
        for credential in cls.credential_list:
            if credential.lastName == name:
                return credential

    @classmethod
    def credential_exist(cls,name):
        '''
        Method that checks if a credential exists from the credential list
        Args:
            number: lastName to search if it exists
        Returns:
            Boolean: True of false depending if the credential exists
        '''
        for contact in cls.credential_list:
            if contact.lastName == name:
                return True 

        return False        

    @classmethod 
    def displayCredentials(cls):
        '''
        method that returns the credential list
        '''
        return cls.credential_list    
