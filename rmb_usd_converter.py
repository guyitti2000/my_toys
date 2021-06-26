#!/usr/bin/python



'''
rmb1 = 5000
rmb2 = 75
rmb3 = 35.60
'''

amount = float(input("Amount of RMB: "))

def convertandCompare(amount):
    usd = amount * .16
    return usd
print("We have converted {}rmb".format(amount) +  " to " + str(convertandCompare(amount)))



'''
print(str(convertandCompare(rmb1)))
print(convertandCompare(rmb2))
print(convertandCompare(rmb3))
'''
