
x = 999
palindromes = []
while x > 1:
    for y in list(reversed(range (100,1000))):
        product = str(x*y)
        half = len(product)/2
        if product[:half] == product[-half:][::-1]:
            product = int(product)
            palindromes.append(product)
    x -= 1

print palindromes
print max(palindromes)
