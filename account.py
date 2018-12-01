# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 21:40:04 2018

@author: Urchaug
"""

class BankAccount:
    def _init_(self, number, ssn, name, balance):
        self._account_number = number  # account number
        self._ssn = ssn               #  social security number
        self._name = name             #  customer name
        self._balance = balance       #  funds available in the account
        self._min_balance = 100       #  balance cannot fall below this amount
        self._active = True           #  account is active or inactive
        
    def deposit (self,  amount):
        if self.is_active():
            self._balance += amount
            return True
        return False
    def withdraw(self, amount):
        result = False;
        if self.is_active():   
             self._balance - amount >= self._min_balance 
             self._balance -= amount;
             result = True;
        return result
    def set_active(self, act):
        self._active = act
        
    bool is_active():
       return self._active
   