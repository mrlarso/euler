import math
import random
def is_prime(number):
	if (number%2 == 0 and number!=2) or number == 1:
		return False
	for divisor in range(3,int(math.sqrt(number))+1,2):
		if number%divisor == 0:
			return False
	return True

primes = [2]

for i in range(3,1000000,2):
    if is_prime(i):
        primes.append(i)


length = 1
for i in range(0,len(primes)):
    for x in range(i,len(primes),length):
        if sum(primes[i:x]) in primes and len(primes[i:x]) > length:
            length = len(primes[i:x])
            print len(primes[i:x])
            print primes[i:x]
            print sum(primes[i:x])
