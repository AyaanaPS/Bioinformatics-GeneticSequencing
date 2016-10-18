import numpy
import math
import matplotlib.pyplot as plt

read_data = numpy.genfromtxt('Q7_kmean.csv', delimiter = ',', skiprows = 1,
	usecols = (1, 2)).tolist()
size = len(read_data)

# Number of Centroids
k = 2

# Initializes the board by choosing the first k values as the centroids.
def initializeBins():
	bins = []
	centroids = []
	for i in range(k):
		bins.append([read_data[i]])
		centroids.append(read_data[i])
	return bins, centroids

# This gets the distance between two points using the distance formula.
def getDistance(pt1, pt2):
	x1 = pt1[0]
	x2 = pt2[0]
	y1 = pt1[1]
	y2 = pt2[1]
	distance = math.sqrt(math.pow((x2-x1), 2) + math.pow((y2-y1), 2))
	return distance

# This fills the bins by iterating through all the points and then putting 
# them in the bin whose centroid is the closest to them.
def fillbins(bins, centroids):
	for i in range(k, size):
		curPoint = read_data[i]
		minDist = 10000000
		bestVal = -1
		for i in range(len(centroids)):
			dist = getDistance(curPoint, centroids[i])
			if dist < minDist:
				minDist = dist
				bestVal = i
		bins[bestVal].append(curPoint)

# This compares two lists. If the number of differences is less than the 
# threshold, it returns False.  Else, it returns True.
def compareLists(old, new, threshold):

	for i in range(k):
		lst1 = old[i]
		lst2 = new[i]
	
		size1 = len(lst1)
		size2 = len(lst2)
		differences = 0

		for i in lst1:
			if i not in lst2:
				differences += 1

		for j in lst2:
			if j not in lst1:
				differences += 1

	if differences > threshold:
		return True

	return False

# This finds the median point in each bin and sets that as the new centroid.
def computeNew(bins):
	newBins = []
	newCentroids = []
	for i in range(k):
		curLst = bins[i]
		size = len(curLst)
		minX = curLst[0][0]
		maxX = curLst[0][0]
		minY = curLst[0][1]
		maxY = curLst[0][1]
		for x in range(1, size):
			if curLst[x][0] < minX:
				minX = curLst[x][0]
			if curLst[x][0] > maxX:
				maxX = curLst[x][0]
			if curLst[x][1] < minY:
				minY = curLst[x][1]
			if curLst[x][1] > maxY:
				maxY = curLst[x][1]
		avgX = (minX + maxX)/2
		avgY = (minY + maxY)/2
		avgPoint = [avgX, avgY]
		smallestDist = 100000
		bestPoint = curLst[0]
		for y in range(size):
			dist = getDistance(avgPoint, curLst[y])
			if dist < smallestDist:
				bestPoint = curLst[y]
		newBins.append([bestPoint])
		newCentroids.append(bestPoint)
	return newBins, newCentroids

# This plots the data from the bins with different colors for each bin.
def plotData(bins):
	colors = ['red', 'blue', 'green', 'yellow']
	for i in range(k):
		curBin = bins[i]
		x = []
		y = []
		for pt in curBin:
			x.append(pt[0])
			y.append(pt[1])
		plt.scatter(x, y, color=colors[i])
	plt.show()

curBins, curCentroids = initializeBins()
fillbins(curBins, curCentroids)
newBins, newCentroids = initializeBins()

# while the oldBins and newBins are very different, it computes newBins.
while(compareLists(curBins, newBins, 5)):
	curBins = newBins
	curCentroids = newCentroids
	newBins, newCentroids = computeNew(curBins)
	fillbins(newBins, newCentroids)

# This plots the bins.
plotData(curBins)

 