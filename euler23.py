def get_divisors(number):
    divisors = [1]
    for i in range(2,number):
        if number%i == 0:
            divisors.append(i)
    return divisors

def is_abundant(number):
    elif sum(get_divisors(number)) > number:
        return True
    return False

def two_abundant(number):
    for i in range(1,(number/2)+1):
        if is_abundant(i) and is_abundant(number-i)
