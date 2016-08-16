def get_divisors(number):
    divisors = [1]
    for i in range(2,number):
        if number%i == 0:
            divisors.append(i)
    return divisors

def is_abundant(number):
    if sum(get_divisors(number)) > number:
        return True
    return False

def two_abundant(number):
    for i in range(1,(number/2)+1):
        if is_abundant(i):
            if is_abundant(number-i):
                return True
    return False

numberslist = range(1,28123)
abundant_numbers_list = []
for i in range (1,28123/2+1):
    if i%1000 == 0:
        print str(i)
    if is_abundant(i):
        for x in abundant_numbers_list:
            if x+ i in numberslist:
                numberslist.remove(x+i)
        abundant_numbers_list.append(i)


print two_abundant_list
