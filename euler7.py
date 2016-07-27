def check_if_prime(x):
    y = 2
    while y < x:
        if x % y == 0:
            prime = False
            break
        else:
            prime = True
            y += 1
    return prime

primes_list = [2,3]
x = 4
while len(primes_list) < 10001:
    if check_if_prime(x) == True:
        primes_list.append(x)
    x += 1

print primes_list[-1]
