
def same_digits(number1, number2):
    num1 = list(str(number1))
    num2 = list(str(number2))

    if len(num1) != len(num2):
        return False

    for i in num1:
        if i in num2:
            num1.remove(i)
            num2.remove(i)
        else:
            return False
    return True


def check_six(number):
    for i in range(2,7):
        if not same_digits(number,i*number):
            return False
    return True

x = 100
while True:
    if check_six(x):
        print x
        break
    x +=1
