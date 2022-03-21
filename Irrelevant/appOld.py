import helper as h
import pgen
import sort


def main():
    passList = []
    password = ''
    delPasswords = []
    print("Welcome to your personal password manager!")
    pgen.getUserInput()
    h.clearConsole()
    print("Here is your password: ")
    password = pgen.createPassword()
    print(password)

    while(True):
        print("press . for menu")
        userSelection = input("Please input a command: ")
        h.clearConsole()
        
        if (userSelection == 'x'):
            return
        
        if(userSelection == '.'):
            h.printMenu()
            
        if(userSelection == 'i'):
            pgen.getUserInput()
            print("Here is your password: ")
            password = pgen.createPassword()
            print(password)
        
        if(userSelection == 'p'):
            print("Here is your password: (Press p for a new password)")
            password = pgen.createPassword()
            print(password)
        
        if(userSelection == 'srt'):
            print("Here is your sorted password: ")
            password = sort.sort(password)
            print(password)
        
        if(userSelection == 's'):
            fullPass = list(['', password])
            passList.append(fullPass)
            print("Password saved")
            h.printList(passList)

        if(userSelection == 'v'):
            h.printList(passList)
        #saves a password with a name
        if(userSelection == 'n'):
            passName = input("What is this password for? ")
            fullPass = list([passName, password])
            passList.append(fullPass)
            h.clearConsole()
            print(f"Password saved as {fullPass[0]} ")
        #renames a password
        if(userSelection == 'r'):
            h.printList(passList)
            index = input(
                "Enter the index or name of the password you wish to change: ")
            if(index.isdigit()):
                index = int(index) - 1
            else:
                for i in range(len(passList)):
                    if(passList[i][0] == index):
                        index = int(i)
            name = input("Please enter the name for the password: ")
            passList[index][0] = name
            h.clearConsole()
            print(f"Password renamed as {name}")
            h.printList(passList)
        #changes a password
        if(userSelection == 'c'):
            h.printList(passList)
            index = input(
                "Enter the index or name of the password you wish to change: ")
            if(index.isdigit()):
                index = int(index) - 1
            else:
                for i in range(len(passList)):
                    if(passList[i][0] == index):
                        index = int(i)
            editedPassword = input("Please enter the edited password: ")
            passList[index][1] = editedPassword
            h.clearConsole()
            print(f"Password updated as {editedPassword}")
            h.printList(passList)

        if(userSelection == 'd'):
            h.printList(passList)
            index = input(
                "Enter the index or name of the password you wish to delete: ")
            if(index.isdigit()):
                index = int(index) - 1
            else:
                for i in range(len(passList)):
                    if(passList[i][0] == index):
                        index = int(i)
            delPasswords.append(passList[index])
            del passList[index]
            h.clearConsole()
            print("Password deleted")
            print("Trash:")
            h.printList(delPasswords)
            print("Passwords:")
            h.printList(passList)

        if(userSelection == 'vd'):
            if(len(delPasswords) < 1):
                print("The trash is empty.")
            else:
                h.printList(delPasswords)
        
        if(userSelection == 'trsh'):
            print("Trash emptied")
            delPasswords.clear()


if __name__ == "__main__":
    main()
