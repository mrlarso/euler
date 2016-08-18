from euler11box import numbers

def clean_data(number_box):
    allnumbers = numbers.replace('\n',' ').split()
    matrix  = {}
    for row in range(1,21):
        numbers_in_row = []
        for index in range (0,20):
            numbers_in_row.append(int(allnumbers[index]))
        allnumbers = allnumbers[20:]
        matrix[row] = numbers_in_row
    return matrix

def max_horizontal_product(row):
    maxproduct = 1
    for i in range(0,len(row)-3):
        product = row[i]*row[i+1]*row[i+2]*row[i+3]
        if product > maxproduct:
            maxproduct = product
    return maxproduct

def max_vertical_product(matrix, column):
    maxproduct = 1
    for i in range(1,18):
        product = matrix[i][column] * matrix[i+1][column] * matrix[i+2][column] * matrix[i+3][column]
        if product > maxproduct:
            maxproduct = product
    return product

def left_right_diag(matrix):
    maxproduct = 1
    for index in range(0,17):
        for row in range(1,18):
            product = matrix[row][index]*matrix[row+1][index+1]*matrix[row+2][index+2]*matrix[row +3][index+3]
            if product > maxproduct:
                maxproduct = product
    return maxproduct

def right_left_diag(matrix):
    maxproduct = 1
    for index in range(19,3,-1):
        for row in range(1,18):
            product = matrix[row][index]*matrix[row+1][index-1]*matrix[row+2][index-2]*matrix[row +3][index-3]
            if product > maxproduct:
                maxproduct = product
    return maxproduct

if __name__ == "__main__":
    mynumbers = clean_data(numbers)
    maxhor, maxvert, maxldiag, maxrdiag = 0, 0, 0, 0
    for row in range(1,21):
        product = max_horizontal_product(mynumbers[row])
        if product > maxhor:
            maxhor = product
    print "max horizontal - " + str(maxhor)
    for column in range(0,20):
        product = max_vertical_product(mynumbers,column)
        if product > maxvert:
            maxvert = product
    print "max vertical - " + str(maxvert)
    print "max leftdiag - " + str(left_right_diag(mynumbers))
    print "max rightdiag - " + str(right_left_diag(mynumbers))
