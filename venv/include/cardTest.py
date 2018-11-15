from effect import *
import settings
def effectDescBuilder(trigger: Enum, Desc: str):

	if trigger.name == "n_a":
		effectDescription = Desc
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
	else:
		raise TypeError

	return "(OPT) " + effectDescription

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

	def ResolveEffect(self, trigger, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):

		result = 1
		changed = None

		i = 1
		for Effect in self.effectList:
				if Effect.get("effectTrigger") == trigger:
					pass
					if settings.returnEffectChecker(self, Effect):
						settings.addEffectChecker(effectMon, Effect)
						result = Effect.get("effect").resolve(effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer)
						changed = True
					else:
						print("{}'s ({}) effect is One Per Turn only".format(effectMon.name, i))
				else:
					pass
				i = i + 1
		## TODO: Fix Dependency on Battle effects (that they do not conflict)
		if changed is None:
			return None
		return result

	def returnEffectList(self):
		text = ""
		for Effect in self.effectList:
			text = text + "" + effectDescBuilder(Effect.get("effectTrigger"), Effect.get("effect").desc) + ". "

		return text

	def checkResolve(self, trigger):
		for Effect in self.effectList:
			if Effect.get("effectTrigger") == trigger:
				if settings.returnEffectChecker(self, Effect):
					return True
		return False