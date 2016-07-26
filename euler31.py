a = 1
b = 2
c = 5
d = 10
e = 20
f = 50
g = 100
h = 200

def get_permutations(amount):
    permutations =[]
    for pound in range(0,amount+1,100):
        running_tally = pound
        for fiftypence in range(0,amount+1-running_tally,50):
            running_tally += fiftypence
            for twentypence in range(0,amount+1-running_tally,20):
                running_tally += twentypence
                for tenpence in range(0,amount+1-running_tally,10):
                    running_tally += tenpence
                    for fivepence in range(0,amount+1-running_tally,5):
                        running_tally+= fivepence
                        for twopence in range(0,amount+1-running_tally,2):
                            running_tally+= twopence
                            for pennies in range(0,amount+1-running_tally,1):
                                running_tally += pennies
                                if running_tally == amount:
                                    permutations.append([pennies,twopence,fivepence,tenpence,twentypence,fiftypence,pound])
                                    running_tally-=pennies
    return permutations

print get_permutations(10)
