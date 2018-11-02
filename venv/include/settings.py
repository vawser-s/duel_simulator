

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

def returnEffectChecker(monster):

	for effectMonster in effectList:
		if monster.name == effectMonster.name:
			print("--------------------------------------")
			print("{}'s effect is One Per Turn only".format(monster.name))

			return False

	return True

def resetEffectChecker():
	global effectList
	effectList = []

def addEffectChecker(monster):
	global effectList
	effectList.append(monster)

def removeEffectChecker(monster):
	global effectList
	i = 0
	for effectMonster in effectList:
		if monster.name == effectMonster.name:
			del effectList[i]
		i = i + 1
