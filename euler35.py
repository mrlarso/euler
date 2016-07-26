import math

def is_prime(number):
    if number%2 == 0 and number > 2 :
        return False
    for divisor in range(3,int(math.sqrt(number))+ 1,2):
        if number%divisor == 0:
            return False
    return True


def get_rotations(number):
    string = str(number)
    if len(string) == 1:
        return [number]
    rotations = [number]
    rotation = string[1:]+string[0]
    while rotation != string:
        rotations.append(int(rotation))
        rotation = rotation[1:]+rotation[0]
    return rotations

def is_circular_prime(number):
    if is_prime(number):
        for rotation in get_rotations(number):
            if not is_prime(rotation):
                return False
        return True

count = 0
for i in xrange(2,1000000):
    if is_circular_prime(i):
        count += 1

print count
