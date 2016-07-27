sum_of_squares = 0
sum = 0
for i in range(1,101):
    sum_of_squares += i*i
    sum +=i

print sum_of_squares
print sum**2

print "difference-" + str(sum**2-sum_of_squares)

