import math

def is_prime(number):
	if number%2 == 0:
		return False
	for divisor in range(3,int(math.sqrt(number))+1,2):
		if number%divisor == 0:
			return False
	return True

def get_intlist(number):
    numberstring = str(number)
    digitlist = []
    for digit in numberstring:
        digitlist.append(int(digit))
    return digitlist

def get_prime_perms(number):
    perms = []
    for x in range(number, 10000,2):
        if (sorted(get_intlist(number)) == sorted(get_intlist(x))) and is_prime(x):
            perms.append(x)
    return sorted(perms)

def get_differences(numberlist):
    differences = {}
    for index in range(0,len(numberlist)):
        for otherindex in range(index+1,len(numberlist)):
            difference = numberlist[otherindex] - numberlist[index]
            if difference in differences:
                differences[difference] += 1
            else:
                differences[difference] = 1
    return differences

for i in range(1001,10000,2):
    if is_prime(i) and len(get_prime_perms(i)) > 2:
        differences = get_differences(get_prime_perms(i))
        for item in differences:
            if differences[item] >= 2:
                print i
                print get_prime_perms(i)
                print differences
                raw_input()
