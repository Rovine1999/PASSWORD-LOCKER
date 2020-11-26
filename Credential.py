#!/usr/bin/env python3.9
from account import Account

def create_account(account_name,username,password):
    '''
    Function to create a new account
    '''
    new_account = Account(account_name,username,password)
    return new_account

def save_accounts(account):
    '''
    Function to save account
    '''
    account.save_account()

def del_account(account):
    '''
    Function to delete an account
    '''
    account.delete_account()


def find_account(account_name):
    '''
    Function that finds an account by account_name and returns the account
    '''
    return Account.find_by_account(account_name)

def check_existing_accounts(account_name):
    '''
    Function that check if an account exists with that account_name and return a Boolean
    '''
    return Account.account_exist(account_name)

def display_account():
    '''
    Function that returns all the saved account
    '''
    return Account.display_account()



def main():
        print("Hello Welcome to your account list. What is the name of your account?")
        account_name = input()

        print(f"Hello {account_name}. what would you like to do?")
        print('\n')

        while True:
                print("Use these short codes : ca - create a new account, da - display accounts, fa -find an account, ex -exit the account list ")

                short_code = input().lower()

                if short_code == 'ca':
                        print("New Account")
                        print("-"*10)

                        print ("Account name")
                        account_name = input()

                        print("Username ...")
                        username= input()

                        print("Password ...")
                        password = input()

                        


                        save_accounts(create_account(account_name,username,password)) 
                        print ('\n')
                        print(f"New Account {account_name} {username} created")
                        print ('\n')

                elif short_code == 'da':

                        if display_account():
                            print("Here is a list of all your accounts")
                            print('\n')

                        for account in display_account():
                            print(f"{account_name} {username} .....{password}")

                            print('\n')
                        else:
                            print('\n')
                            print("You dont seem to have any accounts saved yet")
                            print('\n')

                elif short_code == 'fc':

                        print("Enter the account_name you want to search for")

                        search_account_name = input()
                        if check_existing_accounts(search_account_name):
                                search_account = find_account(search_account_name)
                                print(f"{search_account_name} ")
                                print('-' * 20)

                                print(f"Account_name.......{search_account_name}")
                                
                        else:
                                print("That account does not exist")

                elif short_code == "ex":
                        print("Bye .......")
                        break
                else:
                        print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':
    main()