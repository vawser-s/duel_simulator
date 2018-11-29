import enum
import settings

def effectDescBuilder(trigger: enum.Enum, Desc: str, opt):

	if trigger.name == "n_a":
		effectDescription = Desc
		return effectDescription
	elif trigger.name == "summon":
		effectDescription = "when Summoned: " + Desc
	elif trigger.name == "attack":
		effectDescription = "when Attacking: " + Desc
	elif trigger.name == "defend":
		effectDescription = "when Attacked: " + Desc
	elif trigger.name == "battle":
		effectDescription = "when Battling: " + Desc
	elif trigger.name == "graveyard":
		effectDescription = "when sent to Graveyard: " + Desc
	elif trigger.name == "destructionBat":
		effectDescription = "when destroyed by Battle: " + Desc
	elif trigger.name == "destructionEff":
		effectDescription = "when destroyed by Card Effects: " + Desc
	elif trigger.name == "otherCardEffDestruction":
		effectDescription = "When one of your monsters is destroyed by a card effect: " + Desc
	elif trigger.name == "destroyBattle":
		effectDescription = "When this card destroys a monster by battle: " + Desc
	elif trigger.name == "discardDest":
		effectDescription = "While in your hand: " + Desc
	else:
		print(trigger)
		raise TypeError

	if opt:
		return "(OPT) " + effectDescription
	else:
		return effectDescription.capitalize()

class card:
	def __init__(self, name: object, atkPoints: object, tribute: object, cardEffectList: list, canBeAttacked = True, attacked: int = 0):
		# Parameters
		self.name = name
		self.atkPoints = atkPoints
		self.effectList = cardEffectList
		self.origEffectList = cardEffectList
		self.effectText = self.returnEffectList()
		self.origEffectText = self.returnEffectList()
		self.attacked = attacked
		self.tribute = tribute
		self.origAtk = atkPoints
		self.canBeAttacked = canBeAttacked

	def ResolveEffect(self, trigger, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):

		result = 1
		changed = None

		i = 1
		for Effect in self.effectList:
				if Effect.get("effectTrigger") == trigger:
					pass
					if settings.returnEffectChecker(self, Effect):

						if Effect.get("opt"):
							settings.addEffectChecker(self, Effect)

						result = Effect.get("effect").resolve(effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer)
						changed = True
					else:
						print("--------------------------------------")
						print("{}'s ({}) effect is One Per Turn only".format(effectMon.name, i))
				else:
					pass
				i = i + 1
		if changed is None:
			return None
		return result

	def returnEffectList(self):
		text = ""
		for Effect in self.effectList:
			text = text + "\n   " + effectDescBuilder(Effect.get("effectTrigger"), Effect.get("effect").desc, Effect.get("opt")) + ". "

		return text

	def checkResolve(self, trigger):
		for Effect in self.effectList:
			if Effect.get("effectTrigger") == trigger:
				if settings.returnEffectChecker(self, Effect):
					return True
		return False
