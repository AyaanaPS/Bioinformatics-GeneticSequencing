# This opens and properly formats the data in the file.
f = open('PS2_Q5_Sequence.txt', 'r')
read_data = f.read().replace('\n', '')
read_data = read_data.replace('\r', '')

# This function finds the exact sequence in the CASP1 gene using the algorithm
# defined. First it finds the middle 4mer of the sequence and finds all indices
# of it in the CASP1 gene. It then does an extend at each of the indices found
# to see if the full exact sequence is at that area. It returns a list
# of the exactMatch indices.

def findExact(sequence):
    indices = []
    exactMatches = []
    seqLength = len(sequence)
    merIndex = (len(sequence))/2 - 2
    midMer = sequence[merIndex:merIndex+4]

    for i in range(len(read_data) - 3):
        if read_data[i:i+4] == midMer:
            indices.append((i, i+3))

    valRange = (len(sequence) - 4)/2

    for i in indices:

        (x, y) = i
        flag = 0
        k = 0

        while(k <= valRange):
            if(read_data[x-k] != sequence[merIndex-k]):
                flag = 1
            if(read_data[y+k] != sequence[merIndex+3+k]):
                flag = 1
            k += 1

        if flag == 0:
            exactMatches.append((x-valRange, y+valRange))

    return exactMatches

print '\nQUESTION 6 Part A: \n'

seq = 'TCAGGTCACTCCATGCACAT'
seq1 = 'CAGTTCTGATTCTTTAATGG'
seq2 = 'AACTCAAG'
seq3 = 'CATTAATT'

print '\n' + seq + '\n'
print findExact(seq)

print '\n' + seq1 + '\n'
print findExact(seq1)

print '\n' + seq2 + '\n'
print findExact(seq2)

print '\n' + seq3 + '\n'
print findExact(seq3)

# This finds the 5 best alignments of the sequence in the CASP1 gene.
# First, the middle4mer of the sequence is found and all the indices of the
# 4mer in the gene are saved. The function then extends around the location of
# each 4mer and computes a score by adding one for a mismatch. It then saves
# the location of each possible alignment and a score for the alignment.
# It then finds the 5 minimum scoring alignments and returns them in a list.

def inExact(sequence):
    indices = []
    matches = []
    bestOnes = []

    seqLength = len(sequence)
    merIndex = (len(sequence))/2 - 2
    midMer = sequence[merIndex:merIndex+4]

    for i in range(len(read_data) - 3):
        if read_data[i:i+4] == midMer:
            indices.append((i, i+3))

    valRange = (len(sequence) - 4)/2

    # Computing a score for each index
    for i in indices:

        (x, y) = i
        flag = 0
        k = 0

        tempScore = 0
        score = 0/len(sequence) 

        while(k <= valRange):
            if(read_data[x-k] != sequence[merIndex-k]):
                tempScore += 1
            if(read_data[y+k] != sequence[merIndex+3+k]):
                tempScore += 1

            k += 1
            
        score = tempScore/float(4 + 2 * k)

        matches.append((x-valRange, y+valRange, score))

    # Finding the 5 best
    while(len(bestOnes) < 5):

        curIndex = matches[0]
        minVal = 10

        for x in matches:
            (a, b, c) = x
            if c < minVal:
                minVal = c
                curIndex = x

        matches.remove(curIndex)
        bestOnes.append(curIndex)

    return bestOnes

print '\nQUESTION 6 Part B\n'
seq = 'TTTATCCAATAATGGACACGTT'
seq1 = 'CATAAATTTCACAAAACATATG'

print'\n' + seq + '\n'
bestOnes = inExact(seq)
for i in bestOnes:
    (x, y, z) = i
    print read_data[x:y+1] + '\n\t' + str(x) + ' - ' + str(y)
    print '\tScore: ' + str(z) + '\n'

print '\n' + seq1 + '\n'
bestOnes = inExact(seq1)
for i in bestOnes:
    (x, y, z) = i
    print read_data[x:y+1] + '\n\t' + str(x) + ' - ' + str(y)
    print '\tScore: ' + str(z) + '\n'



