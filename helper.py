from operator import attrgetter
import os

def clearConsole():
    os.system('clear')

def printList(list):
    list.sort(key = attrgetter('name'))
    for i, fullPassword in enumerate(list):
        if(fullPassword.name != ''):
            print(f'{i+1}. {fullPassword.name}: {fullPassword.password}')
        else:
            print(f'{i+1}. {fullPassword.password}')

def findIndex(pMan, index):

    if(index.isdigit()):
        index = int(index) - 1
    else:
        for i in range(len(pMan.allPasswords)):
            if(pMan.allPasswords[i].name == index):
                index = int(i)
    return index    

def printMenu():
    print("i - set/change password parameters")
    print("p - generate password")
    print("s - save password")
    print("v - view list of saved passwords")
    print('n - save a password with a name')
    print("r - rename a password")
    print("c - change password")
    print("d - delete a password")
    print("vd - view deleted passwords")
    print("trsh - permanently erase deleted passwords")
    print("da - delete all passwords")
    print("va - view accounts")
    print('x - exit')