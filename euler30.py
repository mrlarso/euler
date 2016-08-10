numbers = []
number = 2
while True:
    mysum = 0
    for i in str(number):
        mysum += int(i)**5
    if mysum == number:
        print number
        numbers.append(number)
        print str(sum(numbers))
    number += 1
