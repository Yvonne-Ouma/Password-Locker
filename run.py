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

def createCredential(firstName,lastName,accountName,password):
    newCredential = Credential(firstName,lastName,accountName,password)
    return newCredential     

def saveCredential(credential):
    '''
    Function to save a new credential
    '''

    Credential.saveCredential(credential)

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
    print("Hello Welcome to password locker.\n Login:")
    userName = input("What is your name?")
    password = input("Enter your password :")
            

    print(f"Hello {userName}. what would you like to do??\n Create an acount First!!" )
    print("-"* 15)

    while True:
        print("Us this short codes : cc - Create a new credential, dc -display credentials, fc -to search a credential, dl -to delete credential, ex -exit the credential list ")
        short_code = input()

        if short_code == 'cc':
                print("New Credential")
                print("-"*10)

                print ("firstName ....")
                firstName = input()

                print("lastName ...")
                lastName = input()

                print("accountName ...")
                accountName = input()

                print("password ...")
                password = input()


                saveCredential(createCredential(firstName,lastName,accountName,password)) # create and save new credential.

                print('\n')
                # print (f'New Credential {firstName} {lastName} {accountName} created')
                print('\n')

        elif short_code == 'dc':
                if displayCredentials():
                        print("Here is a list of all your credentials")
                        print('\n')

                        for  credential in displayCredentials():
                                print(f"{credential.firstName} {credential.lastName} ....{credential.accountName}")

                        print('\n')
                else:
                        print('\n')
                        print("You dont seem to have any credentials saved yet")
                        print('\n') 

        elif short_code =='dl':
                print("Are your sure you want to delete this credential\n Please insert the name of the credential:")
                searchName = input()
                deleteCredential = Credential.deleteCredential(searchName)



                


        elif short_code == 'fc':

                print("Enter the name you want to search for") 

                searchName = input() 
                searchCredential = findCredential(searchName)
                print(f" {searchCredential.lastName}")
                print('-' * 20)
                print(f"accountName........{searchCredential.accountName}")


        elif short_code == "ex":
                print("Bye ......")   
                break
        else:
                print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':
     
        main()
                        

