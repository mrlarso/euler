import math
import random

def is_prime(number):
    if number%2 == 0 and number > 2 :
        return False
    for divisor in range(3,int(math.sqrt(number))+ 1,2):
        if number%divisor == 0:
            return False
    return True

primes =[2]
for i in range(3,1000000,2):
    if is_prime(i):
        primes.append(i)
        print primes
        raw_input()

length = 1
for i in range(0,len(primes)):
	while i + length < len(primes):
		consec_sum = sum(primes[i:i+length])
