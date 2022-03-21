from FullPassword import FullPassword as fs
import json
import helper as h


class Account():
    allPasswords = []
    delPasswords = []
    username= ''
    userPassword = ''

    def __init__(self, _username, _password):
        self.username = _username
        self.userPassword = _password

    def addPassword(self, _name, _password):
        self.allPasswords.append(fs(_name, _password))
    
    def updateJSON(self):
        li = list()
        for fs in self.allPasswords:
            li.append(fs)

        with open(f'{self.username}_savedPasswords.json', 'w') as f:
            json.dump([o.dump() for o in li], f, indent =3)
    
    def loadJSON(self):
        self.allPasswords = []
        with open(f'{self.username}_savedPasswords.json', 'r') as f:
            data = json.load(f)
            for item in data:
                self.allPasswords.append(fs(item.get('name'), item.get('password')))
    
    def updateDelJSON(self):
        li = list()
        for fs in self.delPasswords: li.append(fs)

        with open(f'{self.username}_deletedPasswords.json', 'w') as f:
            json.dump([o.dump() for o in li], f, indent =3)
    
    def loadDelJSON(self):
        self.delPasswords = []
        with open(f'{self.username}_deletedPasswords.json', 'r') as f:
            data = json.load(f)
            for item in data:
                self.delPasswords.append(fs(item.get('name'), item.get('password')))
    
    def deletePassword(self, _index):
        self.delPasswords.append(self.allPasswords[h.findIndex(self, _index)])
        del self.allPasswords[h.findIndex(self, _index)]

    def printPasswords(self):
        if(len(self.allPasswords) < 1):
            print("There are no saved passwords.")
        else:
            h.printList(self.allPasswords)

    def printDeletedPassword(self):
        if(len(self.delPasswords) < 1):
            print("The trash is empty.")
        else:
            h.printList(self.delPasswords)
    
    def takeOutTrash(self):
        self.delPasswords.clear()
    
    def deleteAll(self):
        self.delPasswords = self.delPasswords + self.allPasswords
        self.allPasswords.clear()
    
    def dump(self):
        return {'username': self.username,
                'password': self.userPassword}