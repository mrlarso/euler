import math

def is_prime(number):
    if number%2 == 0 and number > 2 :
        return False
    for divisor in range(3,int(math.sqrt(number))+ 1,2):
        if number%divisor == 0:
            return False
    return True

primes = [2]
for number in range(3,2000000,2):
    if is_prime(number):
        primes.append(number)

print str(sum(primes))
