def get_coin_combos(amount):
    combos = []
    for pennies in range(0,(amount+1)):
        count = pennies*1
        for twopence in range(0,(amount+1)/2):
            count = pennies*1 + twopence*2
            for fivepence in range(0,(amount+1)/5):
                count = pennies*1 + twopence*2 + fivepence*5
                for tenpence in range(0,(amount+1)/10):
                    count = pennies*1 + twopence*2 + fivepence*5 + tenpence*10
                    if count == amount:
                        combos.append([pennies,twopence,fivepence,tenpence,count])
    return combos

print get_coin_combos(10)
