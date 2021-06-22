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

#supposed to look something like that below
'''
catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) +
      ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]  # list concatenation
print('The cat names are:')
for name in catNames:
    print('  ' + name)

When you run this program, the output will look something like this:

Enter the name of cat 1 (Or enter nothing to stop.):
Zophie
Enter the name of cat 2 (Or enter nothing to stop.):
Pooka
Enter the name of cat 3 (Or enter nothing to stop.):
Simon
Enter the name of cat 4 (Or enter nothing to stop.):
Lady Macbeth
Enter the name of cat 5 (Or enter nothing to stop.):
Fat-tail
Enter the name of cat 6 (Or enter nothing to stop.):
Miss Cleo
Enter the nameof cat 7 (Or enter nothing to stop.):

The cat names are:
  Zophie
  Pooka
  Simon
  Lady Macbeth
  Fat-tail
  Miss Cleo 

'''
