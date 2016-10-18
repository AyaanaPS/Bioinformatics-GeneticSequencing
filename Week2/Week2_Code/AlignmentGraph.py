
# Opens and properly formats the data from the txt file.
f = open('PS2_Q5_Sequence.txt', 'r')
read_data = f.read()
read_data = read_data.replace('\n', '')
read_data = read_data.replace('\r', '')

sequence = 'ATCTCAAACACATGCGGGACCCCAGATA'

# num columns and num rows must be the length of the large sequence and the
# small sequence respectively, +1 because of the gap column and gap row
numColumns = len(read_data) + 1
numRows = len(sequence) + 1

# this initializes the local alignment table
table = []

# this initializes the different scores
gapS = -1
mismatchS = -1
matchS = 1

# this function computes the value at the x and y location of the table
# inputted. It finds the max of 0, the upleft diagonal + match/mismatch score,
# the directly left + gap score and the directly up + gap score.
def computeScore(x, y):
    match = 0
    mismatch = 1

    if(read_data[y-1] == sequence[x-1]):
        match = 1
        mismatch = 0

    val1 = table[x-1][y-1] + (match * matchS) + (mismatch * mismatchS)
    val2 = table[x][y-1] + gapS
    val3 = table[x-1][y] + gapS

    maximum = max(0, val1)
    maximum = max(maximum, val2)
    maximum = max(maximum, val3)

    return maximum

# This appends 0's to every value in the table
for i in range(numRows):
    table.append([0] * numColumns)

# For every row and column except the 1st of each, this calls the computeScore
# method. After this, the table is appropriately filled.
for row in range(1, numRows):
    for col in range(1, numColumns):
        table[row][col] = computeScore(row, col)

# This function finds the last index of a row and column inputted.
# It first checks if the inputted row, col are terminating ones (i.e. they
# lead to the 0th row or 0th column.) It then determines if there is a match
# or mismatch the value it is looking for in the surrounding cells is the value
# in the current - 1 (if match) or +1 (if mismatch).
# It then returns the cell whose value corresponds.

def findLastIndex(x, y):
    if(x - 1 == 0 or y - 1 == 0):
        return (0, 0)

    match = 0

    if(read_data[y-1] == sequence[x-1]):
        match = 1
        val = table[x][y] - 1
    else:
        val = table[x][y] + 1

    if(table[x-1][y-1] == val):
        return(x-1, y-1)

    elif(table[x-1][y] == val):
        return(x-1, y)

    elif(table[x][y-1] == val):
        return(x, y-1)

# This function builds the string. It first finds the max value in the 
# scoring matrix. It then uses the findLastIndex function to get the
# last index and add it to the path.
# Once it gets to an index of (0, 0), the path list is reversed since it starts
# from the end and builds to the beginning. Each string is then created using
# the indices in the path list. The two strings and the beginning index is 
# returned.

def buildString():
    indices = []
    maxVal = 0
    curIndex = (0, 0)
    for row in range(numRows):
        for col in range(numColumns):
            if table[row][col] > maxVal:
                maxVal = table[row][col]
                curIndex = (row, col)

    indices.append(curIndex)
    while (curIndex != (0, 0)):
        (x, y) = curIndex
        curIndex = findLastIndex(x, y)
        indices.append(curIndex)

    str1 = ''
    str2 = ''

    indices.pop()
    indices.reverse()

    for i in indices:
        (x, y) = i
        str1 += read_data[y-1]
        str2 += sequence[x-1]

    return (str1, str2, indices[0])



# This prints the result of the scoring matrix.

(str1, str2, index) = buildString()
(x, y) = index
print str1 + ' found at index: ' + str(y-1) + ' in CASP1 gene.'
print str2 + ' found at index: ' + str(x-1) + ' in sequence.'


