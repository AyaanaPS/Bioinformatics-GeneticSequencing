import itertools

matchS = 1
mismatchS = -1
gapOpen = -1
gapExt = -0.1

gapHorizontal = 0
gapVertical = 0

table = []

# The following comments show how the sequences changed in each run through.
# 2 of the 4 sequences were paired each time to result in the next block of 4.
# They were then padded with gaps to make sure they were all the same length.

seq1 = "ACCCCCAGGCCCTGGCCAAAGCCGTGCAGGTTCACCAGGATACTCTGCGCACCATGTACTTCGCTTGAAGGCAGAACGCTGTTACCTCACTGGATAGAAGAAAGCTTTCCAAGCCCCAGGAGCTGTGCCACCCAAATCCAGAGGAAGCAAGGAGGAGGGAGGTGGGGTAGGGAGGAGTGTAGGATGCCTTGTTTC"
seq2 = "GAGCCACATATCAGGGCAAAGCAATGGGCGAGACCCCCAGGCCCTGGCCAAAGCTGTGCAGGTTCACCAGGATACTCTACGCACCATGTACTTCGCTTGAAGGCAGAACGCTGTTACCTCACTGGATAGAAGAAAGCTTTCCAAGCCCTGGGAGCTGTACCACCCAAATCCAGAGGAAGCAAGGCAGAGGGAGGTGGGGTCGGAAGGAGTATAGGAGG"
# seq3 = "GCAATGGTCGAGATCCTCAAGCGTTGGCCAAAGCGGTGCAGATTCACCACGACTCCCTGAGGACCATGTATTTTGCCTGAATAACAAAAAGCGCACGTCTCCGGACACCTCGAGCCAGAACCCCTGGGTGCTAAACCAGTCCAATGAAGCCCACA"
# seq4 = "GGCAGAGCAATGGGCGGGACCCCCAGGCCCTGGCCAAAGCCGTGCAGGTTCACCAGGATACTCTGCGCACCATGTACTTCGCTTGAAGGCAGAACGCTGTTACCTCACTGGATAGAAGAAAGCTTTCCAAGCCCCAAGAGCTGTGCCGCCCAAATCCAGAGGAAGCAGGGAGGAGGGAGGTGGGGTAGGGAGGAATGC"

# seq1 = "ACCCCCAGGCCCTGGCCAAAGCCGTGCAGGTTCACCAGGATACTCTGCGCACCATGTACTTCGCTTGAAGGCAGAACGCTGTTACCTCACTGGATAGAAGAAAGCTTTCCAAGCCCCAGGAGCTGTGCCACCCAAATCCAGAGGAAGCAAGGAGGAGGGAGGTGGGGTAGGGAGGAGTGTAGGATGCCTTGTTTC"
# seq2 = "GAGCCACATATCAGGGCA-AAGCAATGGGCG-AGACCCCCAGGCCCTGGCCAAAGCTGTGCAGGTTCACCAGGATACTCT-ACGCACCATGTACTTCGCTTGAAGGCAGAACGCTGTTACCTCACTGGATAGAAGAAAGCTTTCCAAG-CCC--TGGGAGCTGTACC-ACCCAAATCCAGAGGAAGCA-AGGCAG-AGGGAGGTGGGGT-CGGAAGGAGTATAG-GAGG"
# seq3 = "GCAATGGTCGAGATCCTCAAGCGTTGGCCAAAGCGGTGCAGATTCACCACGACTCCCTGAGGACCATGTATTTTGCCTGAATAACAAAAAGCGCACGTCTCCGGACACCTCGAGCCAGAACCCCTGGGTGCTAAACCAGTCCAATGAAGCCCACA"
# seq4 = "--------------GGCAG-AGCAATGGGCGG-GACCCCCAGGCCCTGGCCAAAGCCGTGCAGGTTCACCAGGATACTCTG-CGCACCATGTACTTCGCTTGAAGGCAGAACGCTGTTACCTCACTGGATAGAAGAAAGCTTTCCAAGCCCCAA---GAGCTGTGCCG-CCCAAATCCAGAGGAAGCAG-GG-AGGAGGGAGGTGGGGTA-GGGAGGA--AT-GC----"

# seq1 = "--------------GAGCCACATATCAGGGCA--AAGCAATGGGCG--AGACCCCCAGGCCCTGGCCAAAGCT-GTGCAGGTTCACCAGGATACTCT--A-CGCACCATGTACTTCGCTTGAAGGCAGAACGCTGTTACCTCACTGGATAGAAGAAAGCTTTCCAAG--CCC----TG--GGAGCTGTA-CC--ACCCAAATCCAGAGGAAGCA--AGG-CAG---AGGGAGGTGGGGT-C-GGA--AGGAG-TA-TAG-GA--G-----G----"
# seq2 = "--------------G--------------GCAG--AGCAATGGGCGG--GACCCCCAGGCCCTGGCCAAAGC-CGTGCAGGTTCACCAGGATACTCTG---CGCACCATGTACTTCGCTTGAAGGCAGAACGCTGTTACCTCACTGGATAGAAGAAAGCTTTCCAAGC-CCCAA-------GAGCTGT-GCCG--CCCAAATCCAGAGGAAGCAG--GG--AGG--AGGGAGGTGGGGT-----A-G-GGAGG-A------AT-GC---------"
# seq3 = "GCAATGGTCGAGATCCTCAAGCGTTGGCCAAAGCGGTGCAGATTCACCACGACTCCCTGAGGACCATGTATTTTGCCTGAATAACAAAAAGCGCACGTCTCCGGACACCTCGAGCCAGAACCCCTGGGTGCTAAACCAGTCCAATGAAGCCCACA"
# seq4 = "--------------G--------------GCAG--AGCAATGGGCGG--GACCCCCAGGCCCTGGCCAAAGC-CGTGCAGGTTCACCAGGATACTCTG---CGCACCATGTACTTCGCTTGAAGGCAGAACGCTGTTACCTCACTGGATAGAAGAAAGCTTTCCAAGC-CCCAA-------GAGCTGT-GCCG--CCCAAATCCAGAGGAAGCAG--GG--AGG--AGGGAGGTGGGGT-----A-G-GGAGG-A------AT-GC---------"

# seq1 = "--------------GAGCCACATATCAGGGCA--AAGCAATGG-GCG---AGACCCCC---AG-GCC-CTGGCCAAAGCT-G-TGCAGGTTCACCAGGA-T-ACTCT---A-CGCACCATGTA-CTTCGCTTG-A--A-GG-CAGAA-CGC--TGT-TACC---TCAC-T-GGATAG--AAGAA-AGCTTTCCAAG--CCC----TG--G---G-AGCT---GTA-CC--ACCCAAA-TCCAGA-GGAAG--CA---AGG-CAG---AGGGAGGTGGGGT-C-GGA--AGGAG-TA-TAG-GA--G-----G----"
# seq2 = "--------------G--------------GCAG--AGCAATGG-GCG-G--GA-CC-C-CCAG-G-CCCTGGCCAAAGC-CG-TGCAGGTTCACCAGGA-T-ACTCTG----CGCACCATGTA-CTTCGCTTG-A--A-GG-CAGAA-CGC--TGT-TACC---TCAC-T-GGATAG--AAGAA-AGCTTTCCAAGC-CCC--A-A-------G-AGCT---GT-GCCG--CCCA-AATCCAGA-GGAAG--CA-G--GG--AGG--AGGGAGGTGGGGT-----A-G-GGAGG-A------AT-GC---------"
# seq3 = "------------------------------------GCAATGGT-CGA---GATCCTCA--AGCGT---TGGCCAAAG--CGGTGCAGATTCACCACGACTC-C-CTGA----GGACCATGTAT-TTTGCCTGAATAAC--A-AAAAGCGCAC-GTCT-CCGGA-CACCTC-G--AGCC-AGAAC-------------CCCTG-G--------GT-GCTAAA----------CCAG--TCCA-AT-GAAGCCCAC-----------------------------------------------A-------------"
# seq4 = "--------------G--------------GCAG--AGCAATGG-GCG-G--GA-CC-C-CCAG-G-CCCTGGCCAAAGC-CG-TGCAGGTTCACCAGGA-T-ACTCTG----CGCACCATGTA-CTTCGCTTG-A--A-GG-CAGAA-CGC--TGT-TACC---TCAC-T-GGATAG--AAGAA-AGCTTTCCAAGC-CCC--A-A-------G-AGCT---GT-GCCG--CCCA-AATCCAGA-GGAAG--CA-G--GG--AGG--AGGGAGGTGGGGT-----A-G-GGAGG-A------AT-GC---------"

numColumns = len(seq1) + 1
numRows = len(seq2) + 1

traceback = {}

# This function computes the score for the inputted row and column by checking
# the values in the table around that cell.
# It checks for opened gaps. It also adds the cell that was used to compute
# the new cell into a traceback dictionary.
def computeScore(x, y):
	match = 0
	mismatch = 1
	gapS = gapOpen
	global gapHorizontal
	global gapVertical

	if(seq1[y-1] == seq2[x-1]):
		match = 1
		mismatch = 0

	val1 = table[x-1][y-1] + (match * matchS) + (mismatch * mismatchS)

	if(gapHorizontal == 1):
		gapS = gapExt
	if(gapVertical == 1):
		gapS = gapExt

	val2 = table[x][y-1] + gapS
	val3 = table[x-1][y] + gapS

	maximum = max(val1, val2)
	maximum = max(maximum, val3)

	if(val1 == maximum):
		pos = (x-1, y-1)
		gapHorizontal = 0
		gapVertical = 0
	elif(val2 == maximum):
		pos = (x, y-1)
		gapHorizontal = 1
		gapVertical = 0
	elif(val3 == maximum):
		pos = (x-1, y)
		gapHorizontal = 0
		gapVertical = 1

	traceback[(x, y)] = pos

	return maximum

# This builds the table.

for i in range(numRows):
    table.append([0] * numColumns)

for i in range(1, numColumns):
    table[0][i] = table[0][i-1] + gapExt 

for i in range(1, numRows):
    table[i][0] = table[i-1][0] + gapExt

for row in range(1, numRows):
    for col in range(1, numColumns):
        table[row][col] = computeScore(row, col)

# This gets the dictionary representing the order of traversal through the
# table. 
def getRealOrder():
    order = []
    actualOrder = {}

    curPos = (numRows - 1, numColumns - 1)
    order.append(curPos)

    while(True):
        (xCur, yCur) = curPos
        if(xCur == 0 and yCur == 0):
            break
        elif(xCur == 0):  
            oldPos = (xCur, yCur-1)
        elif(yCur == 0):
            oldPos = (xCur-1, yCur)
        else:
            oldPos = traceback[curPos]

        order.append(oldPos)
        curPos = oldPos

    order.reverse()

    for i in range(0, len(order)-1):
        actualOrder[order[i]] = order[i + 1]

    return actualOrder

# This uses the real order dictionary to reconstruct the string.
def reconstructString():
    order = getRealOrder()
    curPos = (0, 0)
    string1 = ""
    string2 = ""

    while(True):

        (xCur, yCur) = curPos
        if(xCur == numRows - 1 and yCur == numColumns - 1):
            break

        newPos = order[curPos]
        (xNew, yNew) = newPos

        if(xCur == xNew):
            string1 += seq1[yNew-1]
            string2 += "-"
        elif(yCur == yNew):
            string1 += "-"
            string2 += seq2[xNew-1]
        else:
            string1 += seq1[yNew-1]
            string2 += seq2[xNew-1]

        curPos = newPos

    return string1, string2

# This function uses the match, mismatch and gap scoresto compute the
# alignment score.

def computeAlignmentScore(seq1, seq2):
    nMatches = 0
    nMismatches = 0
    nGaps = 0
    for i in range(len(seq1)):
        if(seq1[i] == seq2[i]):
            nMatches += 1
        elif(seq1[i] == "-"):
            nGaps += 1
        elif(seq2[i] == "-"):
            nGaps += 1
        else:
            nMismatches += 1

    score = (1 * nMatches) + (-1 * nMismatches) + (-1 * nGaps)
    return score


result1, result2 = reconstructString()
print result1
print result2
score = computeAlignmentScore(result1, result2)
print score

# seq1 = "ACCCCCAGGCCCTGGCCAAAGCCGTGCAGGTTCACCAGGATACTCTGCGCACCATGTACTTCGCTTGAAGGCAGAACGCTGTTACCTCACTGGATAGAAGAAAGCTTTCCAAGCCCCAGGAGCTGTGCCACCCAAATCCAGAGGAAGCAAGGAGGAGGGAGGTGGGGTAGGGAGGAGTGTAGGATGCCTTGTTTC"
# seq2 = "GAGCCACATATCAGGGCAAAGCAATGGGCGAGACCCCCAGGCCCTGGCCAAAGCTGTGCAGGTTCACCAGGATACTCTACGCACCATGTACTTCGCTTGAAGGCAGAACGCTGTTACCTCACTGGATAGAAGAAAGCTTTCCAAGCCCTGGGAGCTGTACCACCCAAATCCAGAGGAAGCAAGGCAGAGGGAGGTGGGGTCGGAAGGAGTATAGGAGG"
# seq3 = "GCAATGGTCGAGATCCTCAAGCGTTGGCCAAAGCGGTGCAGATTCACCACGACTCCCTGAGGACCATGTATTTTGCCTGAATAACAAAAAGCGCACGTCTCCGGACACCTCGAGCCAGAACCCCTGGGTGCTAAACCAGTCCAATGAAGCCCACA"
# seq4 = "GGCAGAGCAATGGGCGGGACCCCCAGGCCCTGGCCAAAGCCGTGCAGGTTCACCAGGATACTCTGCGCACCATGTACTTCGCTTGAAGGCAGAACGCTGTTACCTCACTGGATAGAAGAAAGCTTTCCAAGCCCCAAGAGCTGTGCCGCCCAAATCCAGAGGAAGCAGGGAGGAGGGAGGTGGGGTAGGGAGGAATGC"

# possibilities = {}
# resultsScores = {}
# listPos = list(itertools.combinations([seq1, seq2, seq3, seq4], 2))

# for sequences in listPos:
# 	table = []
# 	seq1, seq2 = sequences
# 	traceback = {}

# 	numColumns = len(seq1) + 1
# 	numRows = len(seq2) + 1

# 	for i in range(numRows):
# 		table.append([0] * numColumns)

# 	table[0][1] = table[0][0] + gapOpen

# 	for i in range(1, numColumns):
# 		table[0][i] = table[0][i-1] + gapExt

# 	table[1][0] = table[0][0] + gapOpen

# 	for i in range(1, numRows):
# 		table[i][0] = table[i-1][0] + gapExt

# 	for row in range(1, numRows):
# 		for col in range(1, numColumns):
# 			table[row][col] = computeScore(row, col)

# 	result1, result2 = reconstructString()
# 	score = computeAlignmentScore(result1, result2)
# 	possibilities[sequences] = score
# 	resultsScores[sequences] = (result1, result2)

# print possibilities
