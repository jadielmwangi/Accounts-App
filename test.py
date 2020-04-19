import unittest 
from main import User
from main import Credentials
import pyperclip

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Jadiel","Muriithi","0727867684","jedielmwangi@gmail.com","sirmwas","101010")
        # create user object

    def test_init(self):
        '''
        test_init to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.first_name,"Jadiel")
        self.assertEqual(self.new_user.second_name,"Muriithi")
        self.assertEqual(self.new_user.phone_number,"0727867684")
        self.assertEqual(self.new_user.email,"jedielmwangi@gmail.com")
        self.assertEqual (self.new_user.user_name,"sirmwas")
        self.assertEqual(self.new_user.password,"101010")

    def test_save_user(self):
        '''
        To test if the user object is saved into the user list
        '''

        self.new_user.save_user() #saving the new user
        self.assertEqual(len(User.user_list),1)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run
        '''

        User.user_list = []

    def test_delete_user(self):
        '''
        Method to test whether we can delete a user from our user's list
        '''

        self.new_user.save_user()
        test_user = User("Jadiel","Muriithi","0727867684","jedielmwangi@gmail.com","sirmwas","101010") #new user
        test_user.save_user()

        self.new_user.delete_user() #Deleting a user
        self.assertEqual(len(User.user_list),1)


class TestCredential(unittest.TestCase):

    '''
    Test Class that defines test cases for the credential class behaviours
    '''

    def setUp(self):
        '''
        setup method to run before each test cases
        '''
        self.new_credential = Credentials("sirmwas","twitter","101010") #Create Credential object

    def test_init(self):
        '''
        To test if the object is initialized properly
        '''
        self.assertEqual(self.new_credential.user_name,"sirmwas")
        self.assertEqual(self.new_credential.platform_name,"twitter")
        self.assertEqual(self.new_credential.password,"101010")

    def tearDown(self):
        Credentials.credential_list = []
        User.users_list = []

    def test_save_credentials(self):
        '''
        Test case that tests if the credentials have been saved
        '''

        self.new_credential.save_credentials() # Saving the new credentials
        twitter = Credentials('sirmwas','twitter','101010')
        twitter.save_credentials()
        self.assertEqual(len(Credentials.credential_list),2)

    def test_delete_credentials(self):
        '''
        Test Case that tests if the user can delete the credentials
        '''

        self.new_credential.save_credentials()
        twitter = Credentials('sirmwas','twitter','101010')
        twitter.save_credentials()
        twitter.delete_credentials()
        self.assertEqual(len(Credentials.credential_list),1)

    def test_find_by_platform_name(self):
        '''
        Test to check if the find by account type method returns the correct credential
        '''

        self.new_credential.save_credentials()
        twitter = Credentials('sirmwas','twitter','101010')
        twitter.save_credentials()
        credential_found = Credentials.find_by_platform_name('twitter')
        self.assertEqual(credential_found.platform_name,'twitter')

    def test_display_all_credentials(self):
        '''
        Method where the user can view various account credentials
        '''
        self.assertEqual(Credentials.display_all_credentials(),Credentials.credential_list)

    def test_copy_credentials(self):
        '''
        A test method to see if the user can copy credentials to the clipboard
        '''

        self.new_credential.save_credentials()
        twitter = Credentials('sirmwas','twitter','101010')
        twitter.save_credentials()
        found_credential = None
        for credential in Credentials.credential_list:
            found_credential = Credentials.find_by_platform_name(
                credential.platform_name
            )
            return pyperclip.copy(found_credential.password)
        Credentials.copy_credentials(self.new_credential.platform_name)
        self.assertEqual('101010',pyperclip.paste())
        print(pyperclip.paste())



if __name__=='__main__':
    unittest.main()