# This function computes the BWM matrix in reverse order using the input
# string. It returns the BWM.
def reversal(seq):
	size = len(seq)
	bwm = list(seq)
	bwm.sort()
	x = 0
	while(x < size-1):
		for i in range(size):
			bwm[i] = seq[i] + bwm[i]	
		bwm.sort()
		x += 1
	return bwm

lst = reversal("AATGCGTCCCCGGAGTAACCGTACCACAACTACCATCACCCGCCGGTATGAGAAACCAAGGGAAAGGGGACAGATGACCAGTCAGACGCAAACGTTTCCGTCCGGCCTAAATATCCAATAGTTTTTATGCACCAAAAATTCAACTAGAAGAATCCTCAGGAAGCAAAATTCAACCAGAAAAGAGCGAGAGATTATGGCAACTATGAGCGGATGGC$CGCAGGAACCCCGAGTTAGGCAACACACATAATGTAAATACATAAATCGAACTATTTATACCAGAAACTTATGTTAGCGCAAATATAGACGTACCCAATGCCTTACGTAATTAGAGAGCCACACTCTACGAAATGAGAAAAAAAACTTGTGAAGTCCCCATACTTATCACGAAGCTGGGGTAAAATGTTCTGGATAAAGAATTGAGAATATGTATAAATGATAACATGTTGTGAAGGTTGTGAATATTCTATGTTTTATTTGGTTTTTCTTAAGAATTAATTTGATTTTTGGGGACAGAACTGCTTTAAAATTGTGATTTTACATGATAATTCAACCATTCCCGCTATTGTATAATTTGTCAAGTGAATCGTAGAGCTTACCTTTAATTGCTAAATTGAGGTATGACGCAACAAATGCAAAAATCAAATAATCCTCAGCTGTCGGGTATCAAAACGTCGTTGTTGATCAAATGACATCATCGCTTTATTTCCGAGAACTCCC")
size = len(lst[0])

# This looks through the rows of the BWM until it finds the one that ends with
# the terminating character: "$"
for i in lst:
	if(i[size - 1] == "$"):
		print i[:size-1]