import math

number = 0
exponent = 1
while True:
    x = 1
    while len(str(x**exponent)) <= exponent:
        if len(str(x**exponent)) == exponent:
            print exponent
            number += 1
            print number
        x +=1
    exponent+= 1
