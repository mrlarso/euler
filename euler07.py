import math
def is_prime(number):
	if number%2 == 0:
		return False
	for divisor in range(3,int(math.sqrt(number))+1,2):
		if number%divisor == 0:
			return False
	return True

n = 2
test = 3
while n < 1001:
    if is_prime(test):
        n +=1
    test += 2

print str(n)
print str(test)
