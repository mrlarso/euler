def is_pandigital(number):
    stringNumber = str(number)
    mylist = []
    for i in stringNumber:
        mylist.append(int(i))
    mylist.sort()
    return mylist == [1, 2, 3, 4, 5, 6, 7, 8, 9]
