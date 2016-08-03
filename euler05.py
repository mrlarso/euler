
def is_divisible(number):
    for divisor in [2520,20,19,18,17,16,14,13,11]:
        if number%divisor != 0:
            return False
    return True

def get_lowest():
    for testNumber in range(20,10000000000,20):
        if is_divisible(testNumber):
            return testNumber

get_lowest()
