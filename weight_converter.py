#!/usr/bin/python



amount = float(input("Amount of weight: "))
unit = input("(K)g or (L)bs: ")

if unit.upper() == "K":
    converted = amount * 2.20462
    print(str(converted) + " lbs")
else:
    converted = amount * 0.454
    print(str(converted) + " kg")



