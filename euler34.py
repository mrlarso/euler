from math import factorial

def is_curious(number):
    total = 0
    for i in list(str(number)):
        total += factorial(int(i))
    if total == number:
        return True
    return False

x = 3
mysum = 0
while x < 9999999:
    if is_curious(x):
        print x
        mysum+=x
        print mysum
    x+=1
