def is_palindrome(number):
    number_string = str(number)
    backward_number = ""
    for index in range(len(number_string)-1,-1,-1):
        backward_number += number_string[index]
    if backward_number == number_string:
        return True
    else:
        return False

def convert_to_binary(number):
    unit = 1
    while unit*2 <= number:
        unit *= 2
    binary_string = ""
    while unit > 0:
        if number >= unit:
            binary_string += '1'
            number -= unit
            unit = unit/2
        else:
            binary_string += "0"
            unit = unit/2
    return int(binary_string)

def sum_of_double_pals(number):
    double_pals = []
    for i in range(1,number):
        if is_palindrome(i) and is_palindrome(convert_to_binary(i)):
            double_pals.append(i)
    return sum(double_pals)

print str(sum_of_double_pals(1000000))
