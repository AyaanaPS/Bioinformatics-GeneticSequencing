import numpy
import matplotlib.pyplot as plt

read_data = numpy.loadtxt('STAT3_ChlP.txt', skiprows = 1, usecols = (1,2,3))
size = len(read_data)

basePairs = []
densities = []
numBP = 0
totDensity = 0
numInPeak = 0

for x in range(size):
	start = int(read_data[x][0])
	stop = int(read_data[x][1])
	density = read_data[x][2]
	for base in range(start, stop):
		basePairs.append(base)
		densities.append(density)
		totDensity += density
		numBP += 1

		if density > 1.0:
			numInPeak += 1

averageDensity = totDensity/numBP
print "Average Density Overall: ", averageDensity
print "K Value: ", numInPeak

plt.plot(basePairs, densities)
plt.show()

