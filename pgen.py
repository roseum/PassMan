import random
import os
from FullPassword import FullPassword

os.system('clear')
    
lowLetters = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
              "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
upLetters = []
for i in range(len(lowLetters)):
     upLetters.append(lowLetters[i].upper())
nums = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
special = ("!", '@', '$', '%', '^', '&', '*', '#')

incSpcl = False
incNum = False
incUp = False
incLow = False
desiredLength = 0



def getUserInput():
    global incSpcl, incNum, incUp, incLow, desiredLength

    desiredLength = int(input("How long would you like the password to be? "))

    specialYN = input("Would you like special characters? (Y/N) ")
    if(specialYN.upper() == 'Y'):
        incSpcl = True

    lowYN = input("Would you like lower-case characters? (Y/N) ")
    if(lowYN.upper() == 'Y'):
        incLow = True

    upYN = input("Would you like upper-case characters? (Y/N) ")
    if(upYN.upper() == 'Y'):
        incUp = True

    numYN = input("Would you like numbers? (Y/N) ")
    if(numYN.upper() == 'Y'):
        incNum = True
        
def addLow():
    if(incLow):
        return random.choice(lowLetters)
    else:
        return ''

def addUp():
    if(incUp):
        return random.choice(upLetters)
    else:
        return ''

def addSpcl():
    if(incSpcl):
        return random.choice(special)
    else:
        return ''

def addNum():
    if(incNum):
        return random.choice(nums)
    else:
        return ''

def createPassword():
    password = ''
    password += addSpcl()
    password += addNum()
    password += addUp()
    password += addLow()

    while(len(password) < desiredLength):
        all = (addSpcl(), addNum(), addLow(), addUp())
        password += random.choice(all)

    l = list(password)
    random.shuffle(l)
    password = ''.join(l)
    return password

def sort(password):
    global sortedPassword
    sortedPassword = ''
    for i in special:
        for j in password:
            if i == j: sortedPassword += j
    for i in upLetters:
        for j in password:
            if i == j: sortedPassword += j

    for i in lowLetters:
        for j in password:
            if i == j: sortedPassword += j

    for i in nums:
        for j in password:
            if i == j: sortedPassword += j
    return sortedPassword

# print(sort(createPassword()))