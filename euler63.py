import math

def is_nth_power(number, exp):
    for x in range (2,int(round(number**(1.0/exp)+1))):
        if x**exp == number:
            return True
    return False

weirds = []
for i in xrange (0,1000000000):
    if is_nth_power(i,len(str(i))):
        weirds.append(i)
        print i

print len(weirds)
