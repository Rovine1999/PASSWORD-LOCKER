import unittest 
from account import  User
from account import Account 


class TestAccount(unittest.TestCase):

    '''
    Test class that defines test cases for the account class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):

        '''
        Set up method to run before each test cases.
        '''
        self.new_account = Account("facebook", "SygelSydney", "rovine1999") 


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_account.account_name,"facebook")
        self.assertEqual(self.new_username,"SygelSydney")
        self.assertEqual(self.new_password,"rovine1999")
       


    def test_save_account(self):
        '''
        test_save_account test case to test if the account object is saved into
         the account list
        '''
        self.new_account.save_account() 
        self.assertEqual(len(Account.account_list),1)

        
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Account.account_list = []

       
    def test_save_multiple_account(self):
            '''
            test_save_multiple_account to check if we can save multiple account
            objects to our account_list
            '''
            self.new_account.save_account()
            test_contact = Contact("Test","username","account_name","password") 
            test_contact.save_contact()
            self.assertEqual(len(Account.account_list),2)

        
    def test_save_multiple_account(self):
            '''
            test_save_multiple_account to check if we can save multiple account
            objects to our account_list
            '''
            self.new_account.save_account()
            test_account = Account("Test","username","account_name","password") 
            test_contact.save_contact()
            self.assertEqual(len(Account.account_list),2)

            
    def test_delete_account(self):

        '''
        test_delete_account to test if we can remove an account from our account list
        '''
        self.new_account.save.account()
        test_account = Account("Test","username","account_name","password") 
        test_account.save_account()

        self.new_contact.test_delete_account()
        self.assertEqual(len(Account.account_list),1)



    def test_find_account_by_account_name(self):

        '''
        test to check if we can find an account by account_name and display information
        '''

        self.new_account.save_account()
        test_account = Account("Test","username","account_name","password") 
        test_account.save_account()

        found_account = Account.find_by_account_name("facebook")

        




   

    def test_account_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the account.
        '''

        self.new_account.save_account()
        test_account = Account("Test","username","account_name","password") # new contact
        test_account.save_account()

        account_exists = Account.account_exist("account_name")

        self.assertTrue(account_exists)


    


    def test_display_all_accounts(self):

        '''
        method that returns a list of all contacts saved
        '''

        self.assertEqual(Contact.display_account(),Account.account_list)





    

if __name__ == '__main__':
    unittest.main()