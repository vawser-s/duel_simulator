turnCount = 0

firstTurn = 0

normalSummoned = 0

global effectList
effectList = []

global standbyEffectList
standbyEffectList = []

global endEffectList
endEffectList = []

bold = "\033[1m"
yellow = '\033[93m'
end = "\033[0m"
darkcyan = '\033[36m'
green = '\033[;33m'


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


def returnEffectChecker(monster, effect):  # format: [monster, trigger]
	for entry in effectList:
		if monster.name == entry[0].name:
			if effect == entry[1]:
				return False
	return True


def resetEffectChecker():
	global effectList
	effectList = []


def addStandbyEffectChecker(monster, effect):
	standbyEffectList.append([monster, effect])


def resolveStandbyEffects(effplayer, opponent, turnPlayer):
	if standbyEffectList:
		for entry in standbyEffectList:
			entry[1].StandbyResolution(1, effplayer, opponent, entry[0], None, None, None, turnPlayer)

		resetStandbyEffectChecker()
	else:
		return


def resetStandbyEffectChecker():
	global standbyEffectList
	standbyEffectList = []


def addEndEffectChecker(monster, effect, player):
	endEffectList.append([monster, effect, player])

def resolveEndEffects():
	if endEffectList:
		for entry in endEffectList:  # Entry: [monster, effect, player]
			entry[1].EndResolution(1, entry[2], entry[0])
			# effect.EndReslution(resolve, player, monster)

		resetEndEffectChecker()

		return True
	else:
		return False

def resetEndEffectChecker():
	global endEffectList
	endEffectList = []

