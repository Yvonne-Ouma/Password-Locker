#!/usr/bin/env python3.6
from user import User

def createUser(userName,password):
    '''
    Function to create a new user
    '''

    newUser = User(userName,password)
    return newUser

def saveUsers(user):
    '''
    Function to save users
    '''

    user.saveUser() 

def delCredential(credential):
    '''
    Function to delete a credential
    '''

    credential.deleteCredential()