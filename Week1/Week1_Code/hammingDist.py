import math

#This opens the sequences file and saves the sequences
#in a list.
f = open('sequences.txt', 'r')
lst_sequences = f.read().split('\r')

#This function computes the hamming distance. This is done
#by computing a difference score between the pattern and
#every possible kmer in a sequence. It then saves the minimum
#score for the sequence. At the end of the function, the sum
#of the minimum scores for each sequence is computed and 
#returned. The function also saves the kmers that were used 
#in each sequence to later generate a PWM.
def hammingDist(pattern):
    patternSize = len(pattern)
    
    totalDist = 0
    usedSequences = []

    for sequence in lst_sequences:

        minSum = 100000
        usedSequence = ''

        for i in range(len(sequence) - patternSize + 1):
            
            str_seq = sequence[i:i+patternSize]

            sumNew = 0

            for j in range(len(str_seq)):
                if str_seq[j] != pattern[j]:
                    sumNew += 1

            if sumNew < minSum:
                minSum = sumNew
                usedSequence = str_seq

        usedSequences.append(usedSequence)

        totalDist += minSum

    return totalDist, usedSequences

#This function generates the PWM using the list of kMers
#used while computing the hamming distance. This PWM
#is used to calculate the entropy.

def generatePWM(used_sequences):
    tempProfile = []
    for x in range(4):
        tempProfile.append([0] * 7)

    numSequences = len(used_sequences)
    x = 0

    while(x < numSequences):
        sequence = used_sequences[x]
        for index in range(len(sequence)):
            if sequence[index] == 'A':
                tempProfile[0][index] += 1

            elif sequence[index] == 'C':
                tempProfile[1][index] += 1

            elif sequence[index] == 'G':
                tempProfile[2][index] += 1

            elif sequence[index] == 'T':
                tempProfile[3][index] += 1

        x += 1

    return tempProfile

#This function calculates the entropy using the PWM 
#generated and the formula: - Summation P(x)logP(x)
#where P(x) is the appropriate value from the profile/25.0.
def calcEntropy(pattern, profile):
    entropy = 0
    value = 0
    for index in range(len(pattern)):
        if pattern[index] == 'A':
            value = (profile[0][index])

        elif pattern[index] == 'C':
            value = (profile[1][index])

        elif pattern[index] == 'G':
            value = (profile[2][index])

        elif pattern[index] == 'T':
            value = (profile[3][index])
    
        realVal = value/25.0
        
        entropy += realVal * math.log(realVal, 2)

    return 0 - entropy

#Answers for the sequences desired:

print 'TTGTAGG'
hamming, usedSequences = hammingDist('TTGTAGG')
print hamming
print ''

print 'GAGGACC'
hamming, usedSequences = hammingDist('GAGGACC')
print hamming
print ''

print 'TATACGG'
hamming, usedSequences = hammingDist('TATACGG')
print hamming
print ''

print 'CCGCAGG'
hamming, usedSequences = hammingDist('CCGCAGG')
print hamming
print ''

print 'CAGCAGG'
hamming, usedSequences = hammingDist('CAGCAGG')
print hamming
profile = generatePWM(usedSequences)
entropy = calcEntropy('CAGCAGG', profile)
print entropy
print ''
