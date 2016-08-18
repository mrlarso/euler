import random
from euler15 import factorial

def get_lexicgraphic_perm(number_of_digits,n):
    digits = range(0,number_of_digits)
    print digits
    my_perm = ""
    while len(digits) > 0:
        print n
        each_digit_perms = factorial(len(digits)-1)
        print "(n-1)! = " + str(each_digit_perms)
        for i in range(1,len(digits)+1):
            print digits[i-1]
            print "first digit" + str((i)*each_digit_perms)
            print "second digit" + str((i+1)*each_digit_perms)
            raw_input()
            if i*each_digit_perms < n:
                if (i+1)*each_digit_perms > n:
                    digit = digits[i]
                    digits.remove(digit)
                    n = n - (i+1)*each_digit_perms
                    my_perm += str(digit)
                    break

    return my_perm


print get_lexicgraphic_perm(3,3)
