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

def check_existingCredentials(name):
    '''
    Function that checks if a credential exists with that name and return a boolean
    '''

    return Credential.credential_exist(name)

def displayCredentials():
    '''
    Function that returns all the saved credentials
    '''

    return Credential.displayCredentials()

def main():
    print("Hello welcome to Password locker.What is your name?")
            userName = input()
            password = input()

            print(f"Hello {userName}. what would you like to do?" )
            print('/n')

            while True:
                print("Us this short codes : cc - Create a new credential, dc -display credentials, fc a contact, ex -exit the credential list ")
                
                if short_code == 'cc':
                        print("New Credential")
                        print("-"*10)

                        print ("firstName ....")
                        fName = input()

                        print("lastName ...")
                        lName = input()

                        print("")




