import random

paths = []
def factorial(number):
    product = 1
    for i in range(number,0,-1):
        product*=i
    return product

def combination(a,b):
    return (factorial(a))/(factorial(a-b)*factorial(b))

if __name__ == "__main__":
    print combination(40,20)
