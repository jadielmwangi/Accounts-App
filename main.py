import pyperclip
import random
import string

class User:
    '''
    Class that generates new instances of users
    '''

    user_list = [] # Empty User List

    def __init__(self,first_name,second_name,phone_number,email,user_name,password):
        '''
        __init__ method that helps us define properties for our objects
        '''
        self.first_name = first_name
        self.second_name = second_name
        self.phone_number = phone_number
        self.email = email
        self.user_name = user_name
        self.password = password
    
    def save_user(self):
        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)

    def delete_user(self):
        '''
        Method deletes a user from the user_list
        '''

        User.user_list.remove(self)


class Credentials:
    '''
    class that generates credentials for the user
    '''

    credential_list = [] #Empty Credential list
    user_credentials_list = []

    @classmethod
    def check_user(cls,user_name,password):
        '''
        Method that checks if the name and password entered match entries
        in the user_list
        '''
        current_user = ''
        for user in  User.user_list:
            if (user.user_name == user_name and user.password == password):
                current_user = user_name
                return current_user


    def __init__(self,user_name,platform_name,password):
        '''
        Method where we define properties for our objects
        '''

        self.user_name = user_name
        self.platform_name = platform_name
        self.password = password

    def save_credentials(self):
        '''
        function for saving user credentials
        '''
        Credentials.credential_list.append(self)

    def delete_credentials(self):
        '''
        function for checking whether we can delete the credentials
        '''
        Credentials.credential_list.remove(self)


    @classmethod
    def rand_pass(cls,size):
        '''
        Takes in random password from digits and letters
        '''
        generate_pass = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(size)])

        return generate_pass


    @classmethod
    def find_by_platform_name(cls, platform_name):
        '''
        A method to search credentials for a given account name
        '''

        for credential in cls.credential_list:
            if credential.platform_name == platform_name:

                return credential


    @classmethod
    def display_credentials(cls,user_name):
        '''
        Class method to display the list of credentials saved
        '''
        user_credentials_list = []
        for credential in cls.credential_list:
            if credential.user_name == user_name:
                user_credentials_list.append(credential)
        return user_credentials_list

    @classmethod
    def copy_credentials(cls,platform_name):
        '''
        method that copies the credentials .
        '''
        found_credential = cls.find_by_platform_name(platform_name)
        return pyperclip.copy(found_credential.password)
