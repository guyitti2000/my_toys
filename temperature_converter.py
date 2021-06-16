#!/usr/bin/python


"""
Formulas
(32°F − 32) × 5/9 = 0°C

(0°C × 9/5) + 32 = 32°F
"""
degrees = float(input("Degrees: "))
unit = input("(C)elsius or (F)ahrenheit: ")
if unit.upper() == "C":
    converted = (degrees * (9/5) + 32)
    print(str(converted) + " °F")
else:
    converted = (degrees - 32) * (5/9)
    print(str(converted) + " °C")

#completed 6/13/21 12:28AM (forgetting the parenthesis...costed an extra 10 min.)
