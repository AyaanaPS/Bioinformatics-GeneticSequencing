seq1 = "CCTTGAGTTGTGCAAAAGTGCTTACAGTGCAGGTAGAGCTCAGC-ACCTACTGCAGTATAAGCACTTCTGGCATGACCGTGG-"
seq2 = "-CCTTGGCCATGTAAAAGTGCTTACAGTGCAGGTAGCTTTTTGAGATCTACTGCAATGTAAGCACTTCTTACATTACCATGG-"

observed = 0
size1 = len(seq1)
size2 = len(seq2)

# This simply counts the number of times there are differences in the same
# position in the two sequences.
for i in range(size1):
	if seq1[i] != seq2[i]:
		observed += 1

# This prints the observed number of differences
print observed

# This prints the difference proportion
print observed/float(size1)
