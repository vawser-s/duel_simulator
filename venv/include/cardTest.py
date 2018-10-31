from card import *
from duelist import *
from effect import *
# from main import effectDescBuilder

class cardTest:
	def __init__(self, name: object, atkPoints: object, tribute: object, cardEffectList: list, attacked: int = 0):
		# Parameters
		self.name = name
		self.atkPoints = atkPoints
		self.effectList = cardEffectList
		self.effectText = self.returnEffectList()
		self.attacked = attacked
		self.tribute = tribute
		self.origAtk = atkPoints

	def ResolveEffect(self, effTrigger):

		for cardEffect in self.effectList:
				if cardEffect.get("effectTrigger") == effTrigger:
					print("{}".format(cardEffect.get("effectText")))

		pass

	def returnEffectList(self):
		text = ""
		for cardEffect in self.effectList:
			text = text + "" + effectDescBuilder(cardEffect.get("effectTrigger"), cardEffect.get("effectText")) + ". "

		return text

	def returnResolvableEffects(self, effTrigger):
		tempList = []

		for cardEffect in self.effectList:
			if cardEffect.get("effectTrigger") == effTrigger:
				tempList.append(cardEffect)

		return tempList

def effectDescBuilder(effTrigger: Enum, Desc: str):

	if effTrigger.name == "n_a":
		effectDescription = Desc
	elif effTrigger.name == "summon":
		effectDescription = "when Summoned: " + Desc
	elif effTrigger.name == "attack":
		effectDescription = "when Attacking: " + Desc
	elif effTrigger.name == "defend":
		effectDescription = "when Attacked: " + Desc
	elif effTrigger.name == "battle":
		effectDescription = "when Battling: " + Desc
	elif effTrigger.name == "graveyard":
		effectDescription = "when sent to Graveyard: " + Desc
	elif effTrigger.name == "destructionBat":
		effectDescription = "when destroyed by Battle: " + Desc
	elif effTrigger.name == "destructionEff":
		effectDescription = "when destroyed by Card Effects: " + Desc
	else:
		raise TypeError

	return "Once per turn, " + effectDescription

# microCoder = card("Micro Coder", 300, 0, effectCyberseSearch, effTrigger.summon, effectDescBuilder(effTrigger.summon, effectCyberseSearch.desc))

cardEffect = {"effect": effectCyberseSearch, "effectText": effectCyberseSearch.desc, "effectTrigger": effTrigger.summon}
cardEffect2 = {"effect": specialCyberseHand, "effectText": specialCyberseHand.desc, "effectTrigger": effTrigger.battle}

testMans = cardTest("Micro Coder", 300, 0, [cardEffect, cardEffect2])

#testMans.ResolveEffect(effTrigger.summon)

#print(testMans.returnEffectList())
i = 0
print("[{}] {} | ATK: {} | Tributes: {} | Effect: {}".format(i + 1, testMans.name, testMans.atkPoints, testMans.tribute, testMans.effectText))