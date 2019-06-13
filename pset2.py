# -*- coding: utf-8 -*-
#"""
#Created on Thu Sep 13 19:47:51 2018
#
#@author: Tech
#"""
#
#"""part 1  just the minimum payment 
#
#balance
#annualInterestRate
#monthlyPaymentRate
#
#Monthly interest rate= (Annual interest rate) / 12.0
#Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
#Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
#Updated balance = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
#
#"""
##
##balance = 42
##annualInterestRate = 0.2
##monthlyPaymentRate = 0.04
##
#monthlyInterestRate = annualInterestRate / 12.0 
#unpaidBalance = balance 
#
#for month in range(12):
#    minPayment = unpaidBalance * monthlyPaymentRate
#    newUnpaidBalance = unpaidBalance - minPayment
#    unpaidBalance = newUnpaidBalance +  (newUnpaidBalance * monthlyInterestRate)
#print("Remaining balance: {0:.2f}".format(unpaidBalance) )
#
#
#""" part 2 Lowest monthlty payment mutiple of 10"""
#
#
##balance = 3926
##annualInterestRate = 0.2
#
#monthlyInterestRate = annualInterestRate / 12.0 
#payment = 10
#BALANCE = balance
#
#while True: 
#    unpaidBalance = BALANCE
#    for month in range(12):
#        newUnpaidBalance = unpaidBalance - payment
#        unpaidBalance = newUnpaidBalance +  (newUnpaidBalance * monthlyInterestRate)
#    if unpaidBalance <= 0: break
#    payment += 10
#
#print('Lowest Payment: {}'.format(payment))
#        

""" part 3 lowest payment to the penny using bi-section search """

balance = 999999
annualInterestRate = 0.18

monthlyInterestRate = annualInterestRate / 12.0
lowerBound = balance / 12
upperBound =  (balance * ((1 + monthlyInterestRate) **12)) / 12

while True:
    middleBound = (lowerBound + upperBound) / 2
    unpaidBalance = balance
    for month in range(12):
        newUnpaidBalance = unpaidBalance - middleBound
        unpaidBalance = newUnpaidBalance +  (newUnpaidBalance * monthlyInterestRate)
    if abs(unpaidBalance) < 0.005:
        print ("Lowest Payment: {0:.2f}".format(middleBound))
        break
        
    elif unpaidBalance > 0 : lowerBound = middleBound
    elif unpaidBalance < 0 : upperBound = middleBound 















balance = 3329
annualInterestRate = 0.2

"""
Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
"""
#
#monthlyInterestRate = (annualInterestRate / 12.0)
#
#for i in range(12):
#    balance = balance - (balance * monthlyPaymentRate)
#    interest = balance * monthlyInterestRate
#    balance += interest
#    
#print('Remaining balance: {}.'.format(round(balance,2)))

monthlyInterestRate = annualInterestRate / 12.0 
for payment in range(0,balance,10):
    
    unpaidBalance = balance
    for month in range(12):
        newUnpaidBalance = unpaidBalance - payment
        unpaidBalance = newUnpaidBalance +  (newUnpaidBalance * monthlyInterestRate)
    if unpaidBalance <= 0:
        break


print("Remaining balance: {0:.2f}".format(payment) )


balance = 999999
annualInterestRate = 0.18

monthlyInterestRate = annualInterestRate / 12
lower = balance / 12
upper =  (balance * ((1 + monthlyInterestRate) **12)) / 12
```````````\ 
+
#
while True:
    middle = (lower + upper) / 2 
    unpaidBalance = balance
    for month in range(12):
        newUnpaidBalance = unpaidBalance - middle
        unpaidBalance = newUnpaidBalance +  (newUnpaidBalance * monthlyInterestRate)
    if abs(unpaidBalance) < 0.005: 
        print("Remaining balance: {0:.2f}".format(middle))
        break
    if unpaidBalance > 0:
        lower = middle
    else:
        upper = middle


    
    









































































