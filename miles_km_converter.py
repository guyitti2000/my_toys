#!/usr/bin/python


distance = float(input('What is the distance?: '))
distance2 = 61.8  # San Clemente to LA
ask = (input('(K)M or (M)I: '))


def convert_distance(distance):
    if ask.lower() == "k":
        converted = distance * 0.621371
        converted = round(converted, 2)
        return ('Here is your converted amount: {}mi'.format(str(converted)))
    else:
        converted = distance * 1.60934
        converted = round(converted, 2)
        return ('Here is your converted amount: {}km'.format(str(converted)))


print(convert_distance(distance))
#print(convert_distance(distance2))
