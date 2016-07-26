chain_winner = [13,10]
for origin_number in range(1,1000000,2):
    x = 1
    number = origin_number
    while number != 1:
        if number%2 == 0:
            number = number/2
            x += 1
        else:
            number = 3*number + 1
            x +=1
    if x > chain_winner[1]:
        chain_winner = [origin_number, x]

print chain_winner
