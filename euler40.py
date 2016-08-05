
d_1 = 0
d_10 = 0
d_100 = 0
d_1000 = 0
d_10000 = 0
d_100000 = 0
d_1000000 = 0

my_string = ""
x = 1
while len(my_string) < 1000000:
    my_string += str(x)
    x += 1

product = 1
for i in [1,10,100,1000,10000,100000,1000000]:
    product*=int(my_string[i-1])
    
print product
