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