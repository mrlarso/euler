a = 1
b = 2
allsum = 2
while a < 4000000 and b < 4000000:
    total = a + b
    if total > 4000000:
        break
    a = b
    b = total
    if b % 2 == 0:
        allsum += b
    print b
print allsum

