import math

def get_factors(number):
    factors = []
    for x in range(1,int(math.sqrt(number))+1):
        if number%x == 0:
            factors.append(x)
            if number/x not in factors:
                factors.append(number/x)
    return factors

number = 1
addition = 2
factors = []
while len(factors) < 500:
    factors = get_factors(number)
    print number
    print factors
    number += addition
    addition += 1
