def get_coin_combos(amount):
    combos = []
    for pennies in range(0,(amount)+1):
        count = pennies*1
        for twopence in range(0,(amount-count)/2+1):
            count = pennies*1 + twopence*2
            for fivepence in range(0,(amount-count)/5+1):
                count = pennies*1 + twopence*2 + fivepence*5
                for tenpence in range(0,(amount-count)/10+1):
                    count = pennies*1 + twopence*2 + fivepence*5 + tenpence*10
                    for twentypence in range(0,(amount-count)/20+1):
                        count = pennies*1 + twopence*2 + fivepence*5 + tenpence*10 + twentypence*20
                        for fiftypence in range(0,(amount-count)/50+1):
                            count = pennies*1 + twopence*2 + fivepence*5 + tenpence*10 +fiftypence*50 + twentypence*20
                            for pound in range(0,(amount-count)/100+1):
                                count = pennies*1 + twopence*2 + fivepence*5 + tenpence*10 +fiftypence*50 + pound*100 + twentypence*20
                                for twopound in range(0,(amount-count)/200+1):
                                    count = pennies*1 + twopence*2 + fivepence*5 + tenpence*10 +fiftypence*50 + pound*100 + twopound*200 + twentypence*20
                                    if count == amount:
                                        combos.append([pennies,twopence,fivepence,tenpence,fiftypence,pound,twopound,count])
    return len(combos)

print get_coin_combos(200)
