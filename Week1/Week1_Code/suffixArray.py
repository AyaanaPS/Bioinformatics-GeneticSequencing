from operator import itemgetter
from bisect import bisect_left, bisect_right

# This function generates a suffix array of the inputted string.
# It does this by looping through every element and appending the
# sequence starting from that element. The suffix array contains
# tuples containing the index and the suffix. The array is then
# sorted by the suffix lexicographically.

def suffixArray(str):

    tempArr = []
    str_low = str.lower()

    for i in range(len(str) + 1):
        tempArr.append((i, (str_low[i:] + '$')))

    sufArr = sorted(tempArr, key=itemgetter(1))

    return sufArr

# This function queries for a particular prefix. It uses the
# bisect_left and bisect_right functions to figure out where
# the prefix could be added to maintain the sorted order.
# It then checks to see if the prefix is indeed a prefix of
# that suffix. 
# The function returns the indexes of the suffix in the 
# suffix array.

def query(prefix):

    suffixes = []
    indexes = []
    for i in sufArr:
        suffixes.append(i[1])

    prefixLength = len(prefix)

    x = 0
    while True: 
        st = bisect_left(suffixes, prefix)
        en = bisect_right(suffixes, prefix)
        
        if st >= len(suffixes):
            break

        if suffixes[st][0:prefixLength] != prefix:
            break

        indexes.append(st+x)

        suffixes.remove(suffixes[st])
        x += 1

    return indexes


# This function converts the indexes outputted by the query function
# into a list of indexes of the actual string. In other words,
# this founds the actual location of the substring in the sequence.
def getIndexes(indexes):
    actualPositions = []
    for x in indexes:
        (index, suffix) = sufArr[x]
        actualPositions.append(index)
    return actualPositions



# This part contains the code used to find the index of the desired
# sequences.

# For the purposes of this question, I converted the .fasta file into
# a .txt file.

file = open('chromosome.txt', 'r')
read_data = file.read()
fixed_data = read_data.replace('\n', '')

sufArr = suffixArray(fixed_data)

query1 = query('atattaacaaagccaaaagtttcaaacttt')
query2 = query('aaaattat')

print 'atattaacaaagccaaaagtttcaaacttt: '
print sorted(getIndexes(query1))
print ''
print 'aaaattat'
print sorted(getIndexes(query2))




