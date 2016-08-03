def is_pandigital(number):
    stringNumber = str(number)
    mylist = []
    for i in stringNumber:
        mylist.append(int(i))
    mylist.sort()
    return mylist == [1, 2, 3, 4, 5, 6, 7, 8, 9]

def largest_pandigital():
    number = 1
    while len(str(number*1)+str(number*2)) <=9:
        chain = ""
        n = 1
        while len(str(chain)) < 9:
            chain += str(number*n)
            n += 1
        if len(chain) == 9 and is_pandigital(int(chain)):
            print chain
            print number
            print str(n)
            print "\n"
        number += 1

largest_pandigital()
