digits = {"0":"","1":'one',"2":'two',"3":'three',"4":"four","5":"five","6":'six',"7":'seven',"8":'eight',"9":'nine'}
teens = {"10":'ten',"11":'eleven',"12":'twelve',"13":'thirteen',"14":'fourteen',"15":'fifteen',"16":'sixteen',"17":'seventeen',"18":"eighteen","19":'nineteen'}
tens = {'2':'twenty','3':'thirty','4':'forty','5':'fifty','6':'sixty','7':'seventy','8':'eighty','9':'ninety'}
def number_to_words(number):
    number = str(number)
    if len(number) == 1:
        return digits[number]
    if len(number) == 2:
        if number[0] == '1':
            return teens[number]
        return tens[number[0]]+digits[number[1]]
    if len(number) == 3:
        if number[-2:] == '00':
            return digits[number[0]]+'hundred'
        return digits[number[0]]+'hundredand'+number_to_words(int(number[-2:]))
    if number == '1000':
        return "onethousand"

total_letters = 0
for number in xrange(1,1001):
    total_letters += len(number_to_words(number))

print total_letters
