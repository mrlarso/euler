import math

def is_prime(number):
	if (number%2 == 0 and number!=2) or number == 1:
		return False
	for divisor in range(3,int(math.sqrt(number))+1,2):
		if number%divisor == 0:
			return False
	return True

def get_truncations(number):
    numberstring = str(number)
    truncations = []
    for index in range(1,len(numberstring)):
        truncations.append(int(numberstring[:index]))
        truncations.append(int(numberstring[-index:]))
    return truncations

def all_truncations_prime(truncations):
    for i in truncations:
        if not is_prime(i):
            return False
    return True

print all_truncations_prime(get_truncations(3797))

truncatable_primes = []
x = 11
while len(truncatable_primes) < 11:
    if is_prime(x) and all_truncations_prime(get_truncations(x)):
        truncatable_primes.append(x)
        print x
    x += 2

print truncatable_primes
print sum(truncatable_primes)
