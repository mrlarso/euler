alphabet = "abcdefghijklmnopqrstuvwxyz"

with open('p022_names.txt', 'r') as myfile:
    names = sorted(myfile.read().replace('"','').split(","))

total = 0
for index in range(0,len(names)):
    lettersum = 0
    for letter in names[index]:
        lettersum += alphabet.index(letter.lower()) + 1
    total += lettersum * (index+1)

print total
