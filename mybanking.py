#Problem statement : Provide a banking system and allow user to deposit and withdraw money

from abc import ABC, abstractmethod
from random import randint

class Account(ABC):
    __accountNumber__ = 0
    _firstName_ = ""
    _lastName_ = ""
    _balance_ = 0.0
    @abstractmethod
    def deposit(self, amount):
        pass
    @abstractmethod
    def withdraw(self, amount):
        pass
    @abstractmethod
    def getBalance(self):
        pass
    def getAccountNumber(self):
        return self.__accountNumber__
    def setAccountNumber(self,number):
        self.__accountNumber__ = number

class SavingsAccount(Account):
    def __init__(self, firstName, lastName):
        super().setAccountNumber(randint(1000, 9999))
        self._firstName_ = firstName
        self._lastName_ = lastName
    def deposit(self, amount):
        self._balance_ += amount
    def withdraw(self, amount):
        if self._balance_ >= amount:
            self._balance_ -= amount
        else:
            print("Insufficient balance")
    def getBalance(self):
        return self._balance_


savings = SavingsAccount("John", "Doe")
print("Account Number={}".format(savings.getAccountNumber()))
print("Balance={}".format(savings.getBalance()))
savings.deposit(1000)
print("Balance={}".format(savings.getBalance()))
savings.withdraw(500)
print("Balance={}".format(savings.getBalance()))
savings.withdraw(5001)
