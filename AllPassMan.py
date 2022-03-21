import json
from operator import attrgetter
from Account import Account
import FullPassword as fs
import json


class AllPassMan():
    accounts = []

    def deleteAccount(self, index):
        pass

    def addAccount(self,_username, _userpassword):
        self.accounts.append(Account(_username, _userpassword))
    
    def updateJSON(self):
        li = list()
        for acnt in self.accounts: li.append(acnt)

        with open('accounts.json', 'w') as f:
                json.dump([a.dump() for a in li], f, indent =3)

    def loadJSON(self):
        self.accounts = []
        with open('accounts.json', 'r') as f:
            data = json.load(f)
            for item in data:
                self.accounts.append(Account(item.get('username'), item.get('password')))
    
    def printAccounts(self):
        self.accounts.sort(key = attrgetter('username'))
        for i, acnt in enumerate(self.accounts):
            if(acnt.username != ''):
                print(f'{i+1}. Username: {acnt.username}   Password:{acnt.userPassword}')
            else:
                print(f'{i+1}. {acnt.userPassword}')
    
    # def findAccount(self):
