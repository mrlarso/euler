def factorial(number):
    product =1
    for n in range(number,1, -1):
        product *= n
    return product

mysum = 0
for i in str(factorial(100)):
    mysum += int(i)

print str(mysum)
