turnCount = 0

firstTurn = 0

normalSummoned = 0


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
