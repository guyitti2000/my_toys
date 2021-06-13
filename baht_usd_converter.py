#!/usr/bin/python

# 1baht = 0.032 usd
# 1usd = 31.09 baht
"""
My goal is to get from 5usd to 5*31.09
"""
amount = int(input("Amount of money: "))
currency = input("(B)AHT or (U)SD: ")
if currency.upper() == "B":
    converted = amount * 0.032
    print(str(converted) + " USD")
else:
    converted = amount * 31.09
    print(str(converted) + " BAHT")

#completed 6/13/21 12:02AM


