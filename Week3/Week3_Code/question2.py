# This function returns a list of all possible permutations of
# the inputted string
def makePerm(seq):
	permutations = []
	for i in range(len(seq)):
		permutations.append(seq[i:] + seq[:i])
	return permutations

# This gets the first and last column in the list of permutations.
def getFL(perms):
	size = len(perms[0])
	firstCol = ""
	lastCol = ""
	for i in perms:
		firstCol += (i[0])
		lastCol += (i[size-1])
	return firstCol, lastCol

# This opens the data file and prepares the sequence.
f = open('GFP.fasta', 'r')
tempSeq = f.readlines()[1:]
sequences = [i.replace("\n", "") for i in tempSeq]
sequence = "".join(sequences)

permutations = makePerm(sequence + "$")
# This lexicographically sorts the list of permutations.
permutations.sort()
result1, result2 = getFL(permutations)
print "First"
print result1
print "\n"
print "Last"
print result2
