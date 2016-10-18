import random

# User input designates the size of k-mer
k = input("Enter desired size of mer: ")
# User input designates the number of repetitions
numRuns = input("Enter desired repetitions: ")

# Opens the sequences.txt file and saves the data as a
# list of sequences.
f = open('sequences.txt', 'r')
lst_sequences = f.read().split('\r')

# This function generates the consensusString from the generated
# profile. This is done by finding the maximum value in each column
# of the profile (recall that each column represents an index of the 
# motif) and building a string from those. i.e. if the maxValue for 
# index 0 is in the 1st row, the first base in the consensus string 
# is a 'C'. This function takes in a profile and returns a string.

def getConsensusString(profile):
    base = 0
    cString = ''

    for i in range(k):
        maxVal = 0
        for j in range(4):
            if profile[j][i] > maxVal:
                maxVal = profile[j][i]
                base = j

        if base == 0:
            cString += 'A'
        elif base == 1:
            cString += 'C'
        elif base == 2:
            cString += 'G'
        elif base == 3:
            cString += 'T'

    return cString

# This function computes the score needed to select the motif in
# each sequence. It uses the profile previously created. The score
# is the product of the appropriate values in the profile divided
# by (k + 4)^k. This computation was taken from the lecture slides.
# Appropriate values refers to the values corresponding to the 
# bases in the sequence.
# This function takes in a sequence and a profile and outputs a score.

def computePWMscore(sequence, profile):
    product = 1
    for index in range(k):
        if sequence[index] == 'A':
            product *= profile[0][index]
        elif sequence[index] == 'C':
            product *= profile[1][index]
        elif sequence[index] == 'G':
            product *= profile[2][index]
        elif sequence[index] == 'T':
            product *= profile[3][index]
    return product

# This function chooses the kMer in each sequence by looking for
# the maximum PWMscore. It uses the above computePWMscore function
# to find the score for every possible kMer in the sequence, and
# then chooses the max scoring one.
# The function takes in a sequence and a profile and outputs a
# string.

def calculateMotifs(profile):
    motifs = []
    for sequence in lst_sequences:
        maxScore = 0
        currentMotif = ''

        for index in (range(len(sequence) - k + 1)):
            sub_seq = sequence[index:index + k]
            score = computePWMscore(sub_seq, profile)
            if score > maxScore:
                maxScore = score
                currentMotif = sub_seq

        motifs.append(currentMotif)

    return motifs

# This function chooses the KMers used using the random 
# selection method.

def getRandomMotifs():
    num_sequences = len(lst_sequences)
    x = 0
    motifs = []
    while(x < num_sequences):
        sequence = lst_sequences[x]
        sequence_size = len(sequence)
        rand_position = random.randint(0, sequence_size - k - 1)
        kMer = sequence[rand_position:rand_position + k]

        motifs.append(kMer)

        x += 1

    return motifs

# This function computes the hamming distance of the consensus
# string of the profile. This is used to score the profile.
# The hamming distance is computed by comparing the consensus
# string to every motif used to generate that PWM. 
# If elements at the same index are unequal, the score is increased.
# The best PWM will have the smallest hammingDist.
# This function takes in a list of motifsUsed and the consensus
# string, and outputs a score.

def hammingDist(kMerList, consensusString):
    score = 0
    for kMer in kMerList:
        for index in range(len(kMer)):
            if kMer[index] != consensusString[index]:
                score += 1

    return score

# This function generates a PWM based on the inputted motif.

def generatePWM(motifs):

    tempProfile = []
    for x in range(4):
        tempProfile.append([1] * k)

    for motif in motifs:
        for index in range(len(motif)):

            if motif[index] == 'A':
                tempProfile[0][index] += 1

            elif motif[index] == 'C':
                tempProfile[1][index] += 1

            elif motif[index] == 'G':
                tempProfile[2][index] += 1

            elif motif[index] == 'T':
                tempProfile[3][index] += 1

    return tempProfile

# This function merges two PWMs by combining their values.

def mergePWM(profile1, profile2):
    for row in range(4):
        for column in range(k):
            profile1[row][column] += profile2[row][column]

    return profile1

# This part of the code uses the above functions to compute
# the motif.

possibilities = []

for i in range(numRuns):

    curMotifs = getRandomMotifs()
    curProfile = generatePWM(curMotifs)
    cons = getConsensusString(curProfile)
    score = 0
    lastScore = hammingDist(curMotifs, cons)

    while score < lastScore:
        lastScore = hammingDist(curMotifs, cons)
        score = 0

        curMotifs = calculateMotifs(curProfile)
        curProfile = mergePWM(curProfile, generatePWM(curMotifs))
        cons = getConsensusString(curProfile)
        score = hammingDist(curMotifs, cons)

    possibilities.append((cons, lastScore))


#This returns the consensus string with the smallest score.

possibilities = sorted(possibilities, key=lambda x: x[1])
print possibilities[0][0]

