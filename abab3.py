from random import shuffle

f=open("./preferences.txt", "r")
# contents =f.read()
file = f.readlines()
result = {}
MAX_THRESHOLD = 7
alreadyAdded = []
unmatchables = []

def searchWithFirstPrefPair(file, firstGroupPair, firstGroupPref, index, secondGroupPrefIndex):
	for i in range(len(file) - index):
		otherPair = file[i+index]
		otherPairSplit = otherPair[:-1].split(",")
		otherPairPref = otherPairSplit[secondGroupPrefIndex]
		if (otherPairPref == firstGroupPref):
			if not (firstGroupPref in result):
				result[firstGroupPref] = []
			result[firstGroupPref].append([firstGroupPair, otherPair])
			alreadyAdded.append(otherPair)
			return True
	return False

def searchForPair(file, prefIndex, pair, pairSplit, currIndex):
	firstPref = pairSplit[prefIndex]
	foundMatch = False
	if (searchWithFirstPrefPair(file, pair, firstPref, currIndex, -3)):
		return True
	if (searchWithFirstPrefPair(file, pair, firstPref, currIndex, -2)):
		return True
	if (searchWithFirstPrefPair(file, pair, firstPref, currIndex, -1)):
		return True
	return False

def dealWithUnmatchables():
	if (len(unmatchables) % 2 == 1):
		lastGroup = unmatchables.pop()
		resultsBySmallest = sorted(result, key=lambda k: len(result[k]))
		result[resultsBySmallest[0]].append([lastGroup])
	for i in range(len(unmatchables) / 2):
		group1 = unmatchables[i]
		group2 = unmatchables[-(i+1)]
		resultsBySmallest = sorted(result, key=lambda k: len(result[k]))
		result[resultsBySmallest[0]].append([group1, group2])

def roomInTopic(pairSplit, index):
	if (pairSplit[index] in result):
		if (len(result[pairSplit[index]]) >= MAX_THRESHOLD):
			return False
	return True


def findMatch(file):
	shuffle(file)
	currIndex = 0
	for pair in file:
		currIndex += 1
		if (pair in alreadyAdded):
			continue
		pairSplit = pair[:-1].split(",")
		if (not (roomInTopic(pairSplit, -3) and searchForPair(file, -3, pair, pairSplit, currIndex))):
			if (not (roomInTopic(pairSplit, -2) and searchForPair(file, -2, pair, pairSplit, currIndex))):
				if (not (roomInTopic(pairSplit, -1) and searchForPair(file, -1, pair, pairSplit, currIndex))):
					unmatchables.append(pair)
	if (len(unmatchables) > 0):
		dealWithUnmatchables()

def printResults():
	for (k, v) in sorted(result.items()):
		print("Here are the teams for topic " + k)
		for group in v:
			if (len(group) == 1):
				print(group[0][:-7])
			else:
				print(group[0][:-7] + " & " + group[1][:-7])
		print("\n")


findMatch(file)
printResults()

