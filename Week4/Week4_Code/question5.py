import random

# This opens the data, gets rid of the unnecessary text and saves it as a list.
f = open('parsimony_seqs.fasta')
tempSeqs = f.readlines() [1::2]
seqs = [i.replace("\n", "") for i in tempSeqs]

node_list = []

# This defines the Node class.
class Node():
	def __init__(self, val, parent, right, left, score):
		self.val = val
		self.parent = parent
		self.right = right
		self.left = left
		self.score = score

# This is an intersect helper function.
def intersect(a, b):
	return list(set(a) & set(b))

# This is a union helper function.
def union(a, b):
	return list(set(a) | set(b))

# This generates a tree with the given sequence. The scores and values are set
# to 0 and empty lists respectively.

def createTree(seq):

	root = Node([], None, None, None, 0)
	root.left = Node(list(seq[4]), root, None, None, 0)
	root.right = Node([], root, None, None, 0)
	root.right.left = Node([], root.right, None, None, 0)
	root.right.left.left = Node(list(seq[3]), root.right.left, None, None, 0)
	root.right.left.right = Node(list(seq[2]), root.right.left, None, None, 0)
	root.right.right = Node([], root.right, None, None, 0)
	root.right.right.left = Node(list(seq[1]), root.right.right, None, None, 0)
	root.right.right.right = Node(list(seq[0]), root.right.right, None, None, 0)

	return root

# This fills up the tree from the bottom up. The score is increased by one if 
# no intersect is found. The value is the result of either the intersect or
# union.

def bottom_up(tree):
	if(tree):
		if(tree.left == None and tree.right == None):
			return (tree.val, 0)
		else:
			(leftVal, leftScore) = bottom_up(tree.left)	
			(rightVal, rightScore) = bottom_up(tree.right)

			lstIntersect = intersect(leftVal, rightVal)
			lstUnion = union(leftVal, rightVal)

			if(len(lstIntersect) != 0):
				tree.val = lstIntersect
				tree.score = leftScore + rightScore
				return (lstIntersect, leftScore + rightScore)
			else:
				tree.val = lstUnion
				tree.score = leftScore + rightScore + 1
				return (lstUnion, leftScore + rightScore + 1)

# This checks the scores from the top down by computing a score based on which
# letter (if there are more than one) from the root value is used.
# It appropriately updates the root nodes value.

def topDown(curr):
	minScore = 20
	actualChars = []
	nodeLst = [curr, curr.left, curr.right, curr.right.right, 
		curr.right.left, curr.right.right.left, curr.right.right.right,
		curr.right.left.right, curr.right.left.left]

	for letter in curr.val:

		score = 0

		for i in nodeLst:
			if(i.parent == None):
				i.val = list(letter)
			else:
				if(i.parent.val[0] in i.val):
					i.val = i.parent.val
				else:
					i.val = random.choice(i.val)
					score += 1

		if score < minScore:
			minScore = score
			actualChars = list(letter)

		elif score == minScore:
			actualChars.append(letter)

	curr.val = actualChars
	curr.score = minScore

	return curr

# This generates a list of nodes by creating a tree for each sequence (where each
# sequence is a column of the aligned sequences) and then implementing the 
# bottom up algorithm and the top down algorithm on it. The node list is filled 
# with the root node for each generated tree.

def generateNodeLst():
	for i in range(len(seqs[0])):
		sequence = seqs[0][i] + seqs[1][i] + seqs[2][i] + seqs[3][i] + seqs[4][i]
		tree = createTree(sequence)
		(rootVal, score) = bottom_up(tree)
		if(len(rootVal) > 1):
			tree = topDown(tree)
		node_list.append(tree)

# This generates a string from the final list of trees. It appends the values of
# each root. It appropriately appends them if there are more then one letter in 
# the value.

def generateString():
	ancestorStr = ''
	for i in node_list:
		if(len(i.val) > 1):
			ancestorStr += '[' + '/'.join(i.val) + ']'
		else:
			ancestorStr += i.val[0]
	return ancestorStr

# This gets and prints the result of all of the bottom.

generateNodeLst()
result = generateString()




