# This package allows for the easy creation of directed graphs in python.
import networkx as nx

# Read the data from the file and split it into the 5 sequence.
f = open('PS2_Q2_Sequence.txt', 'r')
data = f.read().split('\n')
mers = []

# Calculates the 121 30 mers of each sequence and saves them in 5 separate lists
for sequence in data:
    sequence_mers = []
    for index in range(len(sequence) - 29):
        sub_seq = sequence[index:index + 30]
        sequence_mers.append(sub_seq)
    mers.append(sequence_mers)

# Initialize new graph
G = nx.DiGraph()

# For every 30 mer, break it into a prefix (composed of the first 29 chars) and
# a suffix (composed of the last 29 chars). Then add an edge from the prefix
# to the suffix. If neither node exists, this will automatically make the node
# and the edge.
for sequence_mers in mers:
    for mer in sequence_mers:

        prefix = mer[0:29]
        suffix = mer[1:30]
        
        G.add_edge(prefix, suffix)

# Initialize lists needed for tracing the path
nodes = G.nodes()
stack = []
path = []
unequalNodes = []

# Find number of nodes who have an unequal out degree and in degree.
for node in G.nodes():
    if G.out_degree(node) != G.in_degree(node):
        unequalNodes.append(node)

length = len(unequalNodes)

# Check if there are too many or not enough unequalNodes. If this is the case,
# no path exists and an error message is printed.
if length > 2 or length == 1:
    raise Exception('No Eulerian Path Exists')

# If there are exactly 2, which is what is desired, choose the currentNode to 
# be the node whose out degree is bigger than the in degree.
elif length == 2:
    if G.out_degree(unequalNodes[0]) > G.in_degree(unequalNodes[0]):
        currentNode = unequalNodes[0]
    elif G.out_degree(unequalNodes[1]) > G.in_degree(unequalNodes[1]):
        currentNode = unequalNodes[1]
# If there are no nodes who have unequal degrees, the currentNode can be sent
# to any node in the graph. This is set to be the very first node.
else:
    currentNode = nodes[0]

# Loop through the nodes
while(True):
    # If the current node has an outdegree of 0, append it to the path list.
    # Get a new current node from the stack.
    if(G.out_degree(currentNode) == 0):
        path.append(currentNode)
        currentNode = stack.pop()

    # If the out degree is greater than 0, append the currentNode because it
    # must be revisited. Get a list of all of its neighbors and choose one of 
    # them to be the new currentNode. Remove the edge between the old and the
    # new currentNode.
    else:
        stack.append(currentNode)
        neighbors = G.neighbors(currentNode)
        chosenOne = neighbors[0]
        G.remove_edge(currentNode, chosenOne)
        currentNode = chosenOne

    # If the out degree of the node is 0 and there is nothing in the stack then
    # break out of the loop.
    if(G.out_degree(currentNode) == 0 and len(stack) == 0):
        break

# This path list created starts from the end and goes to the beginning. Thus,
# we reverse it.
path.reverse()

# This constructs the superstring of the eulerian path by appending the last 
# character of every node in path except the first, to the first node.
eulerianPath = path[0]
for i in path[1:]:
    eulerianPath += i[28]

# Print out the superstring corresponding to the eulerian path.
print eulerianPath










