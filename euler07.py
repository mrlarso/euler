import math
def is_prime(number):
	if (number%2 == 0 and number!=2) or number == 1:
		return False
	for divisor in range(3,int(math.sqrt(number))+1,2):
		if number%divisor == 0:
			return False
	return True

n = 2
test = 5
while n < 10000:
    if is_prime(test):
        n +=1
        print n
        print test
    test += 2

print str(n)
print str(test)
