'''Class deep diving
1. ENCAPSULATION
2. INHERITENCE
3. POLIMORPHISM
'''
print("===ENCAPSULATION===")
#Python > public, __private, _protected

class Account():
    #state
    description ="The class makes bank account"
    #constructor
    def __init__(self, owner,amount):
        self.__owner = owner
        self.__amount = amount
    #method
    def get_balance(self):
        print(f"the owner {self.__owner} has {self.__amount}usd")

    def deposit(self,amount):
        print("Deposit executed")
        self.__amount += amount

    def withdraw(self,amount):
        print("withdraw executed")
        self.__amount -= amount

    @property
    def holder(self):
       return self.__owner
    
    @holder.setter
    def holder(self, new_owner):
        print("holder.setter", new_owner)
        self._owner = new_owner
    
    def change_ownership(self, new_owner):
        print("change_ownership:", new_owner)
        self.owner = new_owner


my_account = Account("Diana", 10000)
my_account.get_balance()

print("--------")
my_account.deposit(30000)
my_account.get_balance()
my_account.withdraw(40000)
my_account.get_balance()

print("----------")
# my_account.owner="Dina"
my_account.get_balance()
# my_account.amount = 10000
my_account.get_balance()

print("----")
try:
    result = my_account.amount
    print("result", result)
except Exception as err:
    print("No target state found:", err)


print("owner before:", my_account.holder)
my_account.holder = "Anna"
print("owner after", my_account.holder)
