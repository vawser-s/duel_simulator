import effect


class card:
	def __init__(self, name: object, atkPoints: object, tribute: object, cardEffect: effect,
				 trigger: object, effectText: object, opt = 1, attacked: int = 0):
		# Parameters
		self.name = name
		self.atkPoints = atkPoints
		self.effect = cardEffect
		self.trigger = trigger
		self.effectText = effectText
		self.attacked = attacked
		self.tribute = tribute
		self.origAtk = atkPoints
		self.opt = opt