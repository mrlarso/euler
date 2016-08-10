
def get_reverse(number):
    new_number = ""
    for i in range(len(str(number))-1,-1,-1):
        new_number += str(number)[i]
    return int(new_number)

def is_palindrome(number):
    if number == get_reverse(number):
        return True
    return False

numbers_to_test = range(11,10000)
Lychrels = []

while len(numbers_to_test) != 0:
    iterations = 0
    number = numbers_to_test[0]
    tested_numbers = []
    while iterations <= 50:
        tested_numbers.append(number)
        tested_numbers.append(get_reverse(number))
        number = number + get_reverse(number)
        iterations += 1

        if is_palindrome(number):
            for a in tested_numbers:
                if a in numbers_to_test:
                    numbers_to_test.remove(a)
            break
    if not is_palindrome(number):
        Lychrels.append(number)
        numbers_to_test.remove(numbers_to_test[0])

print len(Lychrels)
