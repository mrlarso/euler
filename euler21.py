def sum_of_divisors(number):
    divisors = []
    for divisor in xrange(1,number):
        if number%divisor == 0:
            divisors.append(divisor)
    return sum(divisors)

pairs = {}
for number in range(1,10000):
    divisor_sum = sum_of_divisors(number)
    if (number == sum_of_divisors(divisor_sum)) and (number != divisor_sum) and (divisor_sum not in pairs):
        pairs[number]=divisor_sum

total_amicables = 0
for i in pairs:
    total_amicables += i + pairs[i]
print total_amicables
