#!/usr/bin/python

def convertandCompare(amount):
    usd = amount * .16
    return usd

rmb = []
while True:
    print("Enter your desired amount to be converted" + str(len(rmb) + 1) + 'or enter nothing to stop')
    amount = input("Amount of RMB: ")
    if amount == '':
        break
    rmb += [amount]
    #rmb = (list(map(float, rmb)))
    #print(rmb)
    #rmb = convertandCompare(rmb)
print('The conversion are:')
for amount in rmb:
    print(' ' + str(rmb))


'''
print("We have converted {}rmb".format(amount) +  " to " + str(convertandCompare(amount)))
'''


'''
print(str(convertandCompare(rmb1)))
print(convertandCompare(rmb2))
print(convertandCompare(rmb3))
'''
