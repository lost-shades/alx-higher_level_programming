#!/usr/bin/python3
def uppercase(str):
    result = " "
    for i in str:
        if ord('a') <= ord(i) <= ord('z'):
            upper = chr(ord(i) - (ord('a') - ord('A')))
            result += upper
        else:
            result += i
    print("{}".format(result), end="\n")

