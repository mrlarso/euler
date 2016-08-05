
def is_divisible(number):
    for divisor in range(11,21):
        if number%divisor != 0:
            return False
    return True

def get_lowest():
    testNumber = 20
    while True:
        if is_divisible(testNumber):
            print testNumber
            return testNumber
        testNumber +=20

print get_lowest()
