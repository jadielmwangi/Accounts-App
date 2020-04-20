#!/usr/bin/env python3.6
import pyperclip
from main import User
from main import Credentials

def create_user(first_name,second_name,phone_number,email,user_name,password):
    '''
    function to create new user account
    '''
    new_user = User(first_name,second_name,phone_number,email,user_name,password)
    return new_user

def create_credential(user_name,platform_name,password):
    '''
    function to create a new platform account
    '''
    new_credential = Credentials(user_name,platform_name,password)
    return new_credential

def save_user(user):
    '''
    function to save a new user
    '''
    return User.save_user(user)

def save_credentials(credential):
    '''
    function to save a new user account
    '''
    return Credentials.save_credentials(credential)

def authenticate_user(user_name,password):
    '''
    Function that verifies the existence of the user before creating credentials
    '''
    user_existance = Credentials.check_user(user_name,password)
    return  user_existance 

def rand_pass(size):
    '''
    Function to generate password combining random letters and digits.
    '''
    return Credentials.rand_pass(size)


def display_credentials(user_name):
    '''
    Method that displays all the passwords of a username
    '''
    return Credentials.display_credentials(user_name)

def delete_credential(credentials):
    '''
    funtion to delete credentials from the credential_list
    '''
    Credentials.delete_credentials()

def copy_credentials(platform_name):
    '''
    method that enable us to copy credentials to the clipboard.
    '''
    return Credentials.copy_credentials(platform_name)

def find_by_platform_name(platform_name):
    '''
    function that helps us to find credentials for a certain account
    '''
    return Credentials.find_by_platform_name(platform_name)



def main():
    print("Hello, Welcome to your password account locker. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
        print ('\n')
        print (r"*"*30)
        print ('\n')
        print("="*60)
        print("Use these short codes to make selection in Password_Locker:\n lgn to log in \n cna : to create a new account. \n ex to exit")
        print("="*60) 
        print('\n')

        short_code = input().lower()
        if short_code == 'cna':
            print("Enter First Name ")
            first_name = input()

            print("Enter second Name ")
            second_name = input()

            print("Enter Phone Number ")
            phone_number = input()

            print(" Enter Email Address ")
            email = input()

            print(" Enter Username ")
            username = input()

            

            print("Input your own password or generate it using this app? Use the following short codes\n'gyp\' :to generate password.\n \'eyp\' :to enter your own password \n \'ex\' :to exit... ")
            password_choosen = input()
            password = ''

            if password_choosen == 'eyp':
                password = password.join(
                    input("Enter a password of your choice"))
                

            elif password_choosen == 'gyp':
                print("Enter the length of the password you wish to generate eg 5")
                pass_len = int(input())
                password = rand_pass(pass_len)
                

            elif password_choosen == 'ex':
                print('Thankyou')
                break

            else:
                print("Invalid entry,Please try again using short code")

                
                
            # Create and save new user
            save_user(create_user(first_name, second_name, phone_number,email,user_name,  password))
            print('\n')
            print(f"New Account for {first_name} {second_name} created.")
            print('\n')
            print(
                f"Your password is {password} :-Use it to log in using short code lgn")

            print('\n')

        elif short_code == 'lgn':
            print('\n')
            print("Enter your password-locker account  username")
            username = input()
            print("Enter your password-locker account  password")
            password = input()
            account_exist = authenticate_user(user_name, password)
            if account_exist == user_name:
                print('\n')
                print(
                    f"Welcome to your Password locker account {first_name}: \n Choose an option to continue")
                print('\n')
                while True:
                    print('\n')
                    print("using the following short codes: \n cnc to create new credentials: \n dc to display credentials: \n sc to search credentials: \n rm to remove or delete credentials: \n copy to copy credentials: \n ex to exit")
                    print('\n')
                    short_code = input().lower()
                    if short_code == 'cnc':
                        print('\n')
                        print("Enter your credential details")
                        print("Enter name of platform account eg \'twitter\'")
                        platform_name = input()
                        print(f"Enter username ")
                        user_name = input()
                        

                        while True:
                            print("Input your own password or have one generated for you? Use the following short codes\n'gyp\' to generate password.\n \'eyp\' to choose your own password \n \'ex\' to exit ")
                            password_choosen = input()
                            if password_choosen == 'eyp':
                                password = input(
                                    "Enter a password that  you prefer")
                                break

                            elif password_choosen == 'gyp':
                                print(
                                    "Indicate length of the password to be generate eg 6 ")
                                pass_len = int(input())
                                password = rand_pass(pass_len)
                                break

                            elif password_choosen == 'ex':
                                print('Thankyou')
                                break

                            else:
                                print("Invalid entry,Please try again")

                        

                        save_credentials(create_credential(username, platform_name, password))
                        print(' \n')
                        print(
                            f'Credential Created:\n Account type: {platform_name}  \n Account Username: {user_name} \n Account Password: {password}')
                        print('\n ')

                    elif short_code == 'dc':
                        if display_credentials(user_name):
                            print("Your list of credentials is as follows:")
                            print('\n')
                            for credential in display_credentials(user_name):
                                print(f"Credential Created:\n Account platform name: {platform_name} \n Account Username: {user_name} \n Account Password: {password}")

                        else:
                            print("You don\'t have any credentials yet")
                    elif short_code == "sc":
                        print("Enter the platform account name you want to search for")
                        platform_name = input().lower()
                        if find_by_platform_name(platform_name):
                            search_credential = find_by_platform_name(platform_name)
                            print(f"Account Name : {search_credential.platform_name}")
                            print('-' * 50)
                            print(f"User Name: {search_credential.username} Password :{search_credential.password}")
                            print('-' * 50)
                        else:
                            print("That Credential does not exist")
                            print('\n')            
                    elif short_code == 'rm':
                        print("Enter the account type of the credential you wish to delete")
                        platform_name = input()
                        if find_by_platform_name(platform_name):
                            credential_to_delete = find_by_platform_name(platform_name)
                            print("_"*50)
                            credential_to_delete.delete_credentials()
                            print('\n')
                            print("Credential successfully deleted!")
                        else:
                            print(" We couldin\'t find the credentials associated with the account name you typed.")

                    elif short_code == "copy":
                        print(' \n')
                        platform_name = input(
                            'Enter the site name for the credential password to copy: ')
                        if find_by_platform_name(platform_name):
                            credential_to_copy = find_by_platform_name(platform_name)
                            print("_"*50)
                            credential_to_copy.copy_credentials(platform_name)    
                            
                            print('\n')
                            print("Credential successfully copied")    
                    elif short_code == "ex":
                         print('Thankyou')
                         break
                    else:
                        print("Invalid entry,please try again")

            else:
                print(
                    f"Sorry,no account under the name {user_name}")
                print('\n')
        elif short_code == 'ex':
            print('Thankyou')
            break

        else:
            print("Invalid entry, please use the short code ")

print('\n')

if __name__ == '__main__':

    main()