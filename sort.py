import pgen
print('   ')

password = pgen.createPassword()
print(password)
print('   ')
sortedPassword = ''
def sort(password):
    global sortedPassword
    sortedPassword = ''
    for i in pgen.special:
        for j in password:
            if i == j:
                sortedPassword += j
    for i in pgen.upLetters:
        for j in password:
            if i == j:
                sortedPassword += j

    for i in pgen.lowLetters:
        for j in password:
            if i == j:
                sortedPassword += j

    for i in pgen.nums:
        for j in password:
            if i == j:
                sortedPassword += j
    return sortedPassword

print(sort(password))