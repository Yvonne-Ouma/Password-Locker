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

def delCredential(credential):
    '''
    Function to delete a credential
    '''

    credential.deleteCredential()

def findCredential(name):
    '''
    Function that finds a credential by name returns the credential
    '''

    return Credential.find_by_name(name)

def check_existingCredentials(number):
    '''
    Function that checks if a credential exists with that name and return a boolean
    '''

    return Credential.credential_exist(name)

def displayCredentials():
    '''
    Function that returns all the saved credentials
    '''

    return Credential.displayCredentials()





