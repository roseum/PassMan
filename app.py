import getpass
from AllPassMan import AllPassMan
import helper as h
import pgen
from Account import Account as a
import FullPassword as fs
import os.path
#hello

def main():
    allAccounts = AllPassMan() #Initializes a password manager
    file_exists = os.path.exists('accounts.json')
    if(file_exists == False):allAccounts.updateJSON()
    allAccounts.loadJSON()

    password = ''
    print("Welcome to your personal password manager!")
    hasAccount = input("Do you already have an account? [Y/N] ")
    if(hasAccount.lower() == 'y'):
        global userIndex
        global userValid
        inputUser = input("Please enter your username: ")
        pwd = getpass.getpass(prompt="Enter your password", stream=None)
        userValid = False
        userIndex = 0

        for i, acnt in enumerate(allAccounts.accounts):
            if inputUser.lower() == acnt.username:
                userValid = True
                userIndex = i
                break
        if(userValid == False):
            print(
                "The username you entered does not exist. You may create a new account.")
            return
        elif(pwd == allAccounts.accounts[userIndex].userPassword):
            account = allAccounts.accounts[userIndex]
            print("You're in!")

        else:
            print("The password you entered is incorrect...")
            return

    else:
        newUsername = input("Please select a username: ")
        for acnt in allAccounts.accounts:
            if (acnt.username == newUsername):
                print("This username is already taken. Please choose a different one.")
                return
        newuserPassword = getpass.getpass(prompt="Enter your password ", stream=None)
        #adds account to list of accounts
        allAccounts.addAccount(newUsername, newuserPassword)
        #sets current account to the new account in the list of accounts
        account = allAccounts.accounts[len(allAccounts.accounts)-1]
        allAccounts.updateJSON()
        #generates first password
        pgen.getUserInput()
        h.clearConsole()
        print("Here is your password: ")
        password = pgen.createPassword()
        print(password)
        print('tap s to save it or n to save it with a name')

    while(True):
        #creates JSON file for saved passwords if needed
        file_exists = os.path.exists(f'{account.username}_savedPasswords.json')
        if(file_exists == False):account.updateJSON()
        
        #creates JSON file for deleted passwords if needed
        file_exists = os.path.exists(f'{account.username}_deletedPasswords.json')
        if(file_exists == False):account.updateDelJSON()

        #Load/update JSON files
        account.loadJSON()
        account.updateJSON()
        account.loadDelJSON()
        account.updateDelJSON()
        allAccounts.loadJSON()

        print("press . for menu")
        userSelection = input("Please input a command: ")
        h.clearConsole()

        #exit
        if (userSelection == 'x'):return

        #view menu
        if(userSelection == '.'):h.printMenu()

        #initialize/change passworf parameters
        if(userSelection == 'i'):
            pgen.getUserInput()
            print("Here is your password: ")
            password = pgen.createPassword()
            print(password)

        #generate a new password
        if(userSelection == 'p'):
            print("Here is your password: (Press p for a new password)")
            password = pgen.createPassword()
            print(password)

        #save a password
        if(userSelection == 's'):
            account.addPassword('', password)
            print("Password saved")
            account.printPasswords()
            account.updateJSON()

        #view saved passwords
        if(userSelection == 'v'):account.printPasswords()

        # save a password with a name
        if(userSelection == 'n'):
            passName = input("What is this password for? ")
            account.addPassword(passName, password)
            h.clearConsole()
            print(f"Password saved as {passName} ")
            account.updateJSON()

        # rename a password
        if(userSelection == 'r'):
            h.printList(account.allPasswords)
            index = input(
                "Enter the index or name of the password you wish to change: ")
            
            try:
                name = input("Please enter the name for the password: ")
                account.allPasswords[h.findIndex(account, index)].name = name
                h.clearConsole()
                print(f"Password renamed as {name}")
                account.printPasswords()
                account.updateJSON()
            except:
                h.clearConsole()
                print("Error: Please enter the correct index or an existing name")

        # change a password
        if(userSelection == 'c'):
            account.printPasswords()
            index = input(
                "Enter the index or name of the password you wish to change: ")
            try:
                editedPassword = input("Please enter the edited password: ")
                account.allPasswords[h.findIndex(account, index)].password = editedPassword
                h.clearConsole()
                print(f"Password updated as {editedPassword}")
                account.printPasswords()
                account.updateJSON()
            except: 
                h.clearConsole()
                print("Error: Please enter the correct index or an existing name")

        #delete a password
        if(userSelection == 'd'):
            account.printPasswords()
            index = input(
                "Enter the index or name of the password you wish to delete: ")
            a.deletePassword(account, index)
            h.clearConsole()
            print("Password deleted")
            print("Trash:")
            account.printDeletedPassword()
            print("")
            print("Passwords:")
            account.printPasswords()
            print("")
            account.updateJSON()
            account.updateDelJSON()
        
        #view deleted passwords
        if(userSelection == 'vd'):account.printDeletedPassword()

        #permanently erase deleted passwords
        if(userSelection == 'trsh'):
            account.takeOutTrash()
            print("Trash emptied")
            account.updateDelJSON()

        #delete all saved passwords
        if(userSelection == 'da'):
            shouldDelete = input(
                "Are you sure you want to delete all your passwords? [Y/N] ")
            if (shouldDelete.lower() == 'y'):
                account.deleteAll()
                account.updateDelJSON()
                account.updateJSON()

            else:
                print("Nevermind, then")
        
        #view accounts
        if(userSelection == 'va'):
            allAccounts.loadJSON()
            allAccounts.printAccounts()
            allAccounts.updateJSON()


if __name__ == "__main__":
    main()
