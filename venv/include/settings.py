turnCount = 0

firstTurn = 0

normalSummoned = 0

effectList = []


def printNormalSummon():
	print("Normal Summon Remote: {}".format(normalSummoned))


def changeNormalSummon():
	global normalSummoned
	normalSummoned = 1


def resetNormalSummon():
	global normalSummoned
	normalSummoned = 0


def returnNormalSummon():
	global normalSummoned
	return normalSummoned


def addEffectChecker(monster, effect):
	effectList.append([monster, effect])


def returnEffectChecker(monster, trigger):  # format: [monster, trigger]
	for entry in effectList:
		if monster == entry[0]:
			if trigger == entry[1]:
				return False
	return True


def resetEffectChecker():
	global effectList
	effectList = []