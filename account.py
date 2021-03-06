class User:
    """
    Class that generates new intances of User
    """
    User_List = []

    def __init__(self,username,password):
        self.username = username
        self.password = password 

    def save_new_user(self):
        User.User_List.append(self)

    @classmethod
    def display_users(cls):
        """
        this is a method that returns all users in the User_List
        """
        return cls.User_List

    def delete_user(self):
        """
        delete_user method that deletes a saved user
        """
        User.User_List.remove(self)

class Account:
    """
    Class that generates new instances of contacts.
    """

    account_list = [] 

    def __init__(self,account_name,username,password):

        self.account_name = account_name
        self.username = username
        self.password = password
       
        
        
      
    def save_account(self):

        '''
        save_account method saves account objects into account_list
        '''

        Account.account_list.append(self)


    def delete_account(self):

        '''
        delete_account method deletes a saved account from the account_list
        '''

        Account.account_list.remove(self)

        

    @classmethod
    def display_account(cls):
        '''
        method that returns the account list
        '''
        return cls.account_list



    @classmethod
    def account_exist(cls,account_name):
        '''
        Method that checks if a account exists from the account list.
        Args:
            account_name: Account name to search if it exists
        Returns :
            Boolean: True or false depending if the account exists
        '''
        for account in cls.account_list:
            if account.account_name == account_name:
                    return True

        return False
