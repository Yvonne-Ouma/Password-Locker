#!/usr/bin/env python3.6
from user import User
from credential import Credential

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

def saveCredentials(credential):
    '''
    Function to save a new credential
    '''

    credential.saveCredential()

    