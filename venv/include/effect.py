import time
import random
from enum import Enum
import settings
import math

class effTrigger(Enum):
	n_a = 1
	summon = 2
	attack = 3
	defend = 4
	battle = 5
	graveyard = 6
	destructionBat = 7
	destructionEff = 8
	otherCardEffDestruction = 9
	destroyBattle = 10

def checkControlInstance(InstanceName: str, monfield: list, noOfInstances: int):
	# Check if you control the correct Monster
	result = False
	total = 0

	for monster in monfield:
		if InstanceName in monster.name:
			total = total + 1

	if total >= noOfInstances:
		result = True

	return result

class effect:
	def __init__(self, desc, extraParam=None, extraParam2=None, extraParam3=None):
		self.desc = desc
		self.extraParam = extraParam
		self.nextraParam = extraParam2
		self.dextraParam = extraParam3

	## TODO Refactor parameters
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		raise NotImplementedError("Subclass must implement abstract method")

class effectDestroy(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name) + settings.darkcyan + "{}".format(effectMon.effectText) + settings.end)
		print("--------------------------------------")
		time.sleep(1.3)
		

		if opponent.monfield:
			while True:
				opponent.checkField()

				print("--------------------------------------")
				target = input("~~Select a monster to destroy:")

				try:
					target = int(target) - 1
				except (TypeError, ValueError, IndexError):
					pass

				try:
					oppMon = opponent.monfield[target]
					break
				except (IndexError, TypeError, AttributeError):
					print("--------------------------------------")
					print("Invalid Selection")
					print("--------------------------------------")

			if oppMon.checkResolve(effTrigger.destructionEff):
				eff = oppMon.ResolveEffect(effTrigger.destructionEff, opponent, effplayer, oppMon, effectMon, effgy, oppgy, turnPlayer)

				if eff == 0:
					opponent.destroyMonsterEff(oppMon, opponent, effplayer, oppMon, effectMon, effgy, oppgy, turnPlayer)
				else:
					pass
			else:
				opponent.destroyMonsterEff(oppMon, opponent, effplayer, oppMon, effectMon, effgy, oppgy, turnPlayer)
		else:
				print("No Opponent monster to destroy")
				return
		return -1

class effectDestroyBoth(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name) + settings.darkcyan + "{}".format(effectMon.effectText) + settings.end)
		print("--------------------------------------")
		time.sleep(1.3)

		print("{}'s Field:".format(effplayer.name))
		effplayer.checkField()
		print("{}'s Field:".format(opponent.name))
		opponent.checkField()

		# Get Player
		while True:
			selection = input("~~~Destroy Opponent's Card or Your own card? (O/Y):")

			if selection == "O" or selection == "o":
				player = opponent
				opponent = effplayer
				break
			elif selection == "Y" or selection == "y":
				player = effplayer
				break
			else:
				print("--------------------------------------")
				print("Invalid Selection")
				print("--------------------------------------")
				
		if player.monfield:
			while True:
				player.checkField()

				print("--------------------------------------")
				target = input("~~Select a monster to destroy:")

				try:
					target = int(target) - 1
				except (TypeError, ValueError, IndexError):
					pass

				try:
					target = player.monfield[target]
					break
				except (IndexError, TypeError, AttributeError):
					print("--------------------------------------")
					print("Invalid Selection")
					print("--------------------------------------")

			if target.checkResolve(effTrigger.destructionEff):
				eff = target.ResolveEffect(effTrigger.destructionEff, player, opponent, target, effectMon, effgy, oppgy, turnPlayer)

				if eff == 0:
					player.destroyMonsterEff(target, player, opponent, target, effectMon, effgy, oppgy, turnPlayer)
				else:
					pass
			else:
				player.destroyMonsterEff(target, player, opponent, target, effectMon, effgy, oppgy, turnPlayer)
		else:
				print("No Opponent monster to destroy")
				return
		return -1

class controlDestroy(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name) + settings.darkcyan + "{}".format(effectMon.effectText) + settings.end)
		print("--------------------------------------")
		time.sleep(1.3)
		# extraParam = Namespace to check for
		# extraParam = No of cards to destroy

		result = checkControlInstance(self.extraParam, effplayer.monfield, 1)

		noOfRuns = self.nextraParam

		x = 0


		if result:
			if opponent.monfield:
				while x < noOfRuns:
					# checks if any monsters left
					if opponent.monfield:
						pass
					else:
						print("No More Possible Targets...")
						break

					while True:
						opponent.checkField()

						print("--------------------------------------")
						target = input("~~Select a monster to destroy:")

						try:
							target = int(target) - 1
						except (TypeError, ValueError, IndexError):
							pass

						try:
							oppMon = opponent.monfield[target]
							break
						except (IndexError, TypeError, AttributeError):
							print("--------------------------------------")
							print("Invalid Selection")
							print("--------------------------------------")

					if oppMon.checkResolve(effTrigger.destructionEff):
						eff = oppMon.ResolveEffect(effTrigger.destructionEff, opponent, effplayer, oppMon, effectMon, effgy, oppgy, turnPlayer)

						if eff == 0:
							opponent.destroyMonsterEff(oppMon, effplayer, opponent, oppMon, effectMon, effgy, oppgy,
													   turnPlayer)
						else:
							pass
					else:
						opponent.destroyMonsterEff(oppMon, effplayer, opponent, oppMon, effectMon, effgy, oppgy,
												   turnPlayer)

					x = x + 1
			else:
				print("No Possible Targets...")
		else:
			print("You need to control a {} monster to resolve {}'s effect".format(self.extraParam, effectMon.name))

class destroyHand(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name) + settings.darkcyan + "{}".format(effectMon.effectText) + settings.end)
		print("--------------------------------------")
		time.sleep(1.3)

		if effplayer.hand:
			while True:
				effplayer.checkHand()

				print("--------------------------------------")
				target = input("~~Select a monster to destroy:")

				try:
					target = int(target) - 1
				except (TypeError, ValueError, IndexError):
					pass

				try:
					target = effplayer.hand[target]
					break
				except (IndexError, TypeError, AttributeError):
					print("--------------------------------------")
					print("Invalid Selection")
					print("--------------------------------------")

			if target.checkResolve(effTrigger.destructionEff):
				eff = target.ResolveEffect(effTrigger.destructionEff, effplayer, opponent, target, oppMon, effgy, oppgy, turnPlayer)

				if eff == 0 or eff is None:
					effplayer.destroyMonsterEffHand(target, effplayer, opponent, target, oppMon, effgy, oppgy, turnPlayer)
				else:
					pass
			else:
				effplayer.destroyMonsterEffHand(target, effplayer, opponent, target, oppMon, effgy, oppgy, turnPlayer)
		else:
				print("No monster to destroy")
				return
		return -1

# NOT DESIGNED TO BE USED SOLELY BY ITSELF
class destroyAll(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		tempListeff = []  #Used so any monsters summoned during the resolution do not get destroyed
		tempListopp = []  #Used so any monsters summoned during the resolution do not get destroyed

		for monster in effplayer.monfield:
			if monster != effectMon:
				tempListeff.append(monster)

		for monster in opponent.monfield:
			if monster != effectMon:
				tempListopp.append(monster)

		while effplayer.monfield and tempListeff:

			monster = effplayer.monfield[0]

			if effplayer.monfield[0] in tempListeff:
				if monster.checkResolve(effTrigger.destructionEff):
					eff = monster.ResolveEffect(effTrigger.destructionEff, effplayer, opponent, monster, oppMon, effgy,
					                            oppgy, turnPlayer)

					if eff == 0 or eff is None:
						effplayer.destroyMonsterEff(monster, effplayer, opponent, monster, oppMon, effgy, oppgy,
						                            turnPlayer)
					else:
						pass
				else:
					effplayer.destroyMonsterEff(monster, effplayer, effplayer, monster, oppMon, effgy, oppgy,
					                            turnPlayer)

					tempListeff.remove(monster)

		while opponent.monfield and tempListopp:

			monster = opponent.monfield[0]

			if opponent.monfield[0] in tempListopp:
				if monster.checkResolve(effTrigger.destructionEff):
					eff = monster.ResolveEffect(effTrigger.destructionEff, opponent, effplayer, monster, oppMon, effgy,
					                            oppgy, turnPlayer)

					if eff == 0 or eff is None:
						opponent.destroyMonsterEff(monster, opponent, effplayer, monster, oppMon, effgy, oppgy,
						                            turnPlayer)
					else:
						pass
				else:
					opponent.destroyMonsterEff(monster, opponent, effplayer, monster, oppMon, effgy, oppgy,
					                            turnPlayer)

				tempListopp.remove(monster)

		return 0

class effectDamage(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name) + settings.darkcyan + "{}".format(effectMon.effectText) + settings.end)
		print("--------------------------------------")
		time.sleep(1.3)
		
		# extraParam = Life Point loss

		opponent.loseLP(self.extraParam)

class effectDamageSelf(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name) + settings.darkcyan + "{}".format(effectMon.effectText) + settings.end)
		print("--------------------------------------")
		time.sleep(1.3)
		
		# extra = Life Point Loss

		effplayer.loseLP(self.extraParam)

class effectRestore(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name) + settings.darkcyan + "{}".format(effectMon.effectText) + settings.end)
		print("--------------------------------------")
		time.sleep(1.3)
		
		# extraParam = Life Point Gain

		effplayer.gainLP(self.extraParam)

class effectCrash(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name) + settings.darkcyan + "{}".format(effectMon.effectText) + settings.end)
		print("--------------------------------------")
		time.sleep(1.3)

		try:
			effectMon.atkPoints = oppMon.atkPoints
			print("{} Copies the opponents attack!".format(effectMon.name))
			time.sleep(0.5)
			return 0
		except (AttributeError, UnboundLocalError):
			pass

class playerDraw(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name) + settings.darkcyan + "{}".format(effectMon.effectText) + settings.end)
		print("--------------------------------------")
		time.sleep(1.3)
		
		# extraParam = No of Cards to Draw

		effplayer.draw(self.extraParam)

		return

class controlDiscardDraw(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name) + settings.darkcyan + "{}".format(effectMon.effectText) + settings.end)
		print("--------------------------------------")
		time.sleep(1.3)
		
		# extraParam = Namespace to check for
		# extraParam = No of Cards to draw

		result = checkControlInstance(self.extraParam, effplayer.monfield, 1)

		if effplayer.hand:
			if result:
				effplayer.effectdiscardCard(effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer)
				effplayer.draw(self.nextraParam)
			else:
				print("You need to control a {} monster to resolve {}'s effect".format(self.extraParam, effectMon.name))
		else:
			print("--------------------------------------")
			print("You must be able to discard a card for cost")

class siphonLife(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name) + settings.darkcyan + "{}".format(effectMon.effectText) + settings.end)
		print("--------------------------------------")
		time.sleep(1.3)
		
		# extraParam = Life Point Siphon Amount

		opponent.loseLP(self.extraParam)
		effplayer.gainLP(self.extraParam)

class mill(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name) + settings.darkcyan + "{}".format(effectMon.effectText) + settings.end)
		print("--------------------------------------")
		time.sleep(1.3)
		

		effplayer.mill(effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer)

		time.sleep(1.3)

		pass

class siphonLifeAndMill(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name) + settings.darkcyan + "{}".format(effectMon.effectText) + settings.end)
		print("--------------------------------------")
		time.sleep(1.3)
		
		# extraParam = Life Point Siphon Amount

		opponent.loseLP(self.extraParam)
		effplayer.gainLP(self.extraParam)

		print("--------------------------------------")
		time.sleep(0.5)

		# Mill a Card
		effplayer.mill(effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer)

		time.sleep(1.3)

		pass

class effectPlayerRandDiscard(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name) + settings.darkcyan + "{}".format(effectMon.effectText) + settings.end)
		print("--------------------------------------")
		time.sleep(1.3)
		
		# extraParam = No Of Cards to Discard

		x = 0

		while True:
			# Choose a random number in hand to discard
			handSize = effplayer.hand.__len__()

			try:
				selection = random.randint(0, handSize - 1)
				effplayer.discardCard(selection)

				x = x + 1

				if x == self.extraParam:
					return None

			except IndexError:
				if effplayer.hand.__len__() == 0:
					print("{}'s Hand is Empty".format(effplayer.name))
					return None
				else:
					print("Card is not in {}'s Hand".format(effplayer.name))
					return None

class effectOpponentDiscard(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name) + settings.darkcyan + "{}".format(effectMon.effectText) + settings.end)
		print("--------------------------------------")
		time.sleep(1.3)
		
		# extraParam = No Of Cards to Discard

		x = 0

		while True:
			# Choose a random number in hand to discard
			handSize = opponent.hand.__len__()

			# Break if opponent's hand is empty
			if handSize == 0:
				print("{}'s hand is empty".format(opponent.name))
				break

			try:
				selection = random.randint(0, handSize - 1)
				opponent.discardCard(selection)

				x = x + 1

				if x == self.extraParam:
					break

			except IndexError:
				raise NotImplementedError

class noBattleDestruction(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name) + settings.darkcyan + "{}".format(effectMon.effectText) + settings.end)
		print("--------------------------------------")
		time.sleep(1.3)

		print("{} cannot be destroyed by Battle".format(effectMon.name))

		return 1

class noEffectDestruction(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("Counter Monster Effect Activate!")
		print("--------------------------------------")
		time.sleep(1.3)

		print("{} cannot be destroyed by Effects".format(effectMon.name))

		return 1

class searchDeck(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name) + settings.darkcyan + "{}".format(effectMon.effectText) + settings.end)
		print("--------------------------------------")
		time.sleep(1.3)
		

		effplayer.searchDeck()

class searchSpecificDeck(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name) + settings.darkcyan + "{}".format(effectMon.effectText) + settings.end)
		print("--------------------------------------")
		time.sleep(1.3)
		
		# extraParam = Namespace to Search
		# nextraParam = Namespace to Search

		effplayer.searchSpecificDeck(self.extraParam)

class searchSpecificDeckNamespace(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name) + settings.darkcyan + "{}".format(effectMon.effectText) + settings.end)
		print("--------------------------------------")
		time.sleep(1.3)
		
		# extraParam = Namespace to Search
		# nextraParam = Namespace to Search

		effplayer.searchSpecificDeckNamespace(self.extraParam, self.nextraParam)

class extraNormalSummon(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name) + settings.darkcyan + "{}".format(effectMon.effectText) + settings.end)
		print("--------------------------------------")
		time.sleep(1.3)
		

		print("You get one extra normal summon")

		settings.resetNormalSummon()

class gainAttack(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name) + settings.darkcyan + "{}".format(effectMon.effectText) + settings.end)
		print("--------------------------------------")
		time.sleep(1.3)
		
		# extraParam = Attack Point Gain

		effectMon.atkPoints = effectMon.atkPoints + self.extraParam

		print("{} has gained {} Attack Points".format(effectMon.name, self.extraParam))

		time.sleep(0.5)

		if turnPlayer == effplayer:
			if oppMon:
				return effectMon.atkPoints - oppMon.atkPoints
			else:
				return effectMon.atkPoints
		else:
			return oppMon.atkPoints - effectMon.atkPoints

class gainAttackDifference(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name) + settings.darkcyan + "{}".format(effectMon.effectText) + settings.end)
		print("--------------------------------------")
		time.sleep(1.3)
		

		difference = effplayer.lifepoints - opponent.lifepoints

		if difference < 0:
			difference = opponent.lifepoints - effplayer.lifepoints

		if difference == 0:
			print("Life Points are equal, no Atk Gain")
			return

		effectMon.atkPoints = effectMon.atkPoints + difference

		print("{} has gained {} Attack Points".format(effectMon.name, difference))

		time.sleep(0.5)

class grantAttack(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name) + settings.darkcyan + "{}".format(effectMon.effectText) + settings.end)
		print("--------------------------------------")
		time.sleep(1.3)
		
		# extraParam = Attack Point Gain

		effplayer.grantAttack(self.extraParam, effectMon)

		return

class grantAll(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name) + settings.darkcyan + "{}".format(effectMon.effectText) + settings.end)
		print("--------------------------------------")
		time.sleep(1.3)
		# extraParam = ATK point increase

		if effplayer.monfield.__len__() == 0:
			print("Field Empty")
			return

		for monster in effplayer.monfield:
			monster.atkPoints = monster.atkPoints + self.extraParam
			print("{} has gained {} Atk Points".format(monster.name, self.extraParam))

class grantAttackNamespace(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name) + settings.darkcyan + "{}".format(effectMon.effectText) + settings.end)
		print("--------------------------------------")
		time.sleep(1.3)
		
		# extraParam = Namespace to grant attack to
		# nextraParam = Amount of Attack per instance

		total = 0

		for monster in effplayer.monfield:
			if self.extraParam in monster.name:
				total = total + 1

		if total == 0:
			print("No {} monsters on field".format(self.extraParam))
			return
		else:
			print("--------------------------------------")
			print("You have {} ".format(total) + settings.green + "{}".format(self.extraParam) + settings.end + " monsters on the field, so you give {} Atk to {} monsters".format(self.nextraParam, total))
			print("--------------------------------------")

		for monster in effplayer.monfield:
			if self.extraParam in monster.name:
				effplayer.grantAttack(total * self.nextraParam, effectMon)

class fieldToHand(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name) + settings.darkcyan + "{}".format(effectMon.effectText) + settings.end)
		print("--------------------------------------")
		time.sleep(1.3)
		

		if opponent.monfield:
			while True:
				opponent.checkField()

				print("--------------------------------------")
				target = input("~~Select a monster to Bounce:")
				target = int(target) - 1

				try:
					oppMon = opponent.monfield[target]
					break
				except (IndexError, TypeError):
					print("--------------------------------------")
					print("Invalid Selection")

			opponent.bounce(oppMon)
		else:
				print("No Opponent monster to return")

				return
		return

class gyToHand(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name) + settings.darkcyan + "{}".format(effectMon.effectText) + settings.end)
		print("--------------------------------------")
		time.sleep(1.3)
		

		effplayer.graveyardToHand()

class tributeTOSSGy(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name) + settings.darkcyan + "{}".format(effectMon.effectText) + settings.end)
		print("--------------------------------------")
		time.sleep(1.3)
		

		while True:
			print("--------------------------------------")
			print("Effect: {}".format(effectMon.effectText))
			selection = input("Activate {}'s Effect? (Y/N)".format(effectMon.name))
			print("--------------------------------------")
			selection = str(selection)

			if selection == "Y" or selection == "y":

				monster = effectMon

				target = effplayer.checkArrayLoc(effplayer.monfield, monster)
				del effplayer.monfield[target]

				print("{} Has been tributed".format(effectMon.name))

				print("--------------------------------------")

				effplayer.ssGraveyard()

				print("--------------------------------------")

				effplayer.sendToGrave(monster, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer)

				return
			elif selection == "N" or selection == "n":
				return

class tributeTOSSDeckSpecific(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name) + settings.darkcyan + "{}".format(effectMon.effectText) + settings.end)
		time.sleep(1.3)
		
		# extraParam = Namespace to summon from

		while True:
			print("--------------------------------------")
			print("Effect: {}".format(effectMon.effectText))
			selection = input("~~Activate {}'s Effect? (Y/N)".format(effectMon.name))
			print("--------------------------------------")
			selection = str(selection)

			if selection == "Y" or selection == "y":

				monster = effectMon

				target = effplayer.checkArrayLoc(effplayer.monfield, monster)
				del effplayer.monfield[target]

				print("{} Has been tributed".format(effectMon.name))

				print("--------------------------------------")

				effplayer.specialDeckSpecific(self.extraParam, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer)

				print("--------------------------------------")

				effplayer.sendToGrave(effplayer, opponent, monster, oppMon, effgy, oppgy, turnPlayer)

				return
			elif selection == "N" or selection == "n":
				return

class specialHand(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name) + settings.darkcyan + "{}".format(effectMon.effectText) + settings.end)
		print("--------------------------------------")
		time.sleep(1.3)
		

		effplayer.specialHandEffect(effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer)

class specialSpecificHand(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name) + settings.darkcyan + "{}".format(effectMon.effectText) + settings.end)
		print("--------------------------------------")
		time.sleep(1.3)
		
		# extraParam = Namespace to special/search

		effplayer.specialHandSpecific(self.extraParam, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer)

class discardToSpecialHand(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name) + settings.darkcyan + "{}".format(effectMon.effectText) + settings.end)
		print("--------------------------------------")
		time.sleep(1.3)
		
		# extraParam = Namespace to special/search

		effplayer.effectdiscardCard(effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer)

		effplayer.specialHandSpecific(self.extraParam, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer)

class discardToSpecialGY(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name) + settings.darkcyan + "{}".format(effectMon.effectText) + settings.end)
		print("--------------------------------------")
		time.sleep(1.3)
		
		# extraParam = Namespace to special/search

		effplayer.effectdiscardCard(effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer)

		if self.extraParam and self.nextraParam:
			effplayer.specialGraveyardSpecific(effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer, self.extraParam, self.nextraParam, )
		else:
			effplayer.specialGraveyardSpecific(effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer, self.extraParam)

class specialExactHand(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name) + settings.darkcyan + "{}".format(effectMon.effectText) + settings.end)
		print("--------------------------------------")
		time.sleep(1.3)
		
		# extraParam = Namespace to special/search

		effplayer.specialHandExact(self.extraParam, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer)

# DESIGNED TO BE USED AS A RESPONSE TO AN EFFECT DESTRUCTION ON FIELD
class specialMeHand(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates in the Hand!".format(effectMon.name))
		print("--------------------------------------")
		time.sleep(1.3)

		effplayer.summonfromHand(effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer)

class specialDeckExact(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name) + settings.darkcyan + "{}".format(effectMon.effectText) + settings.end)
		print("--------------------------------------")
		time.sleep(1.3)
		
		# extraParam = Namespace to special/search

		effplayer.specialDeckExact(self.extraParam, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer)

class specialDeckSpecific(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name) + settings.darkcyan + "{}".format(effectMon.effectText) + settings.end)
		print("--------------------------------------")
		time.sleep(1.3)
		# extraParam = Namespace to special/search
		# nextraParam = extra Namespace

		if self.nextraParam:
			effplayer.specialDeckSpecific(self.extraParam, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer, self.nextraParam)
		else:
			effplayer.specialDeckSpecific(self.extraParam, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer)

class specialGraveyardSpecific(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name) + settings.darkcyan + "{}".format(effectMon.effectText) + settings.end)
		print("--------------------------------------")
		time.sleep(1.3)
		# extraParam = Namespace
		# nextraParam = Namespace

		effplayer.specialGraveyardSpecific(effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer, self.extraParam, self.nextraParam)

class specialDeckSpecificLessAttack(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name) + settings.darkcyan + "{}".format(effectMon.effectText) + settings.end)
		print("--------------------------------------")
		time.sleep(1.3)
		# extraParam = Namespace to special/search

		effplayer.specialDeckSpecificLessAttack(self.extraParam, self.nextraParam, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer)

class gainAtkforInstance(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name) + settings.darkcyan + "{}".format(effectMon.effectText) + settings.end)
		print("--------------------------------------")
		time.sleep(1.3)
		
		# extraParam = Namespace to gain attack from
		# nextraPAram = Attack Point Increase

		instanceName = self.extraParam
		atkChange = self.nextraParam
		fieldCount = 0
		fieldATK = 0
		gyATK = 0
		gyCount = 0

		for monster in effplayer.monfield:
			if instanceName in monster.name and monster.name != effectMon.name:
				fieldCount = fieldCount + 1

		for monster in effplayer.gy:
			if instanceName in monster.name and monster.name != effectMon.name:
				gyCount = gyCount + 1

		if fieldCount:
			fieldATK = fieldCount * atkChange
			print("{} {} monsters on field, so {} ATK gained".format(fieldCount, instanceName, fieldATK))

		if gyCount:
			gyATK = gyCount * atkChange
			print("{} {} monsters in graveyard, so {} ATK gained".format(gyCount, instanceName, gyATK))

		totalATK = fieldATK + gyATK

		if totalATK:
			effectMon.atkPoints = effectMon.atkPoints + totalATK
			print("{}'s new Attack: {}".format(effectMon.name, effectMon.atkPoints))

		else:
			print("No Attack Gained")

		# Check if a Battle Effect or not
		if effectMon.checkResolve(effTrigger.summon):
			return
		if effectMon.checkResolve(effTrigger.battle):
			damage = effectMon.atkPoints - oppMon.atkPoints
			return damage

# NOT DESIGNED TO BE USED SOLELY BY ITSELF | ALWAYS PUT BEHIND OTHER DEFENDING OR ATTACKING EFFECTS
class halfAttacked(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("--------------------------------------")

		oppMon.atkPoints = int(oppMon.atkPoints / 2)
		print("{}'s ATK points have been halved to {}".format(oppMon.name, oppMon.atkPoints))
		time.sleep(1.3)

# Same as above but can be used alone
class halfAttackedMessage(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name) + settings.darkcyan + "{}".format(effectMon.effectText) + settings.end)
		print("--------------------------------------")
		time.sleep(1.3)

		oppMon.atkPoints = int(oppMon.atkPoints / 2)
		print("{}'s ATK points have been halved to {}".format(oppMon.name, oppMon.atkPoints))

class zeroAttack(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name) + settings.darkcyan + "{}".format(effectMon.effectText) + settings.end)
		print("--------------------------------------")
		time.sleep(1.3)
		

		oppMon.atkPoints = 0
		print("{}'s ATK points have been reduced to 0".format(oppMon.name))

		time.sleep(1.3)

class tributetoGrantAttack(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name) + settings.darkcyan + "{}".format(effectMon.effectText) + settings.end)
		time.sleep(1.3)
		

		while True:
			print("--------------------------------------")
			print("Effect: {}".format(effectMon.effectText))
			selection = input("Activate {}'s Effect? (Y/N)".format(effectMon.name))
			print("--------------------------------------")
			selection = str(selection)

			if selection == "Y" or selection == "y":

				monster = effectMon

				target = effplayer.checkArrayLoc(effplayer.monfield, monster)
				del effplayer.monfield[target]

				print("{} Has been tributed".format(effectMon.name))

				print("--------------------------------------")

				effplayer.grantAttack(monster.atkPoints, monster)

				effplayer.sendToGrave(effplayer, opponent, monster, oppMon, effgy, oppgy, turnPlayer)

				return
			elif selection == "N" or selection == "n":
				return

class gainLPforHand(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name) + settings.darkcyan + "{}".format(effectMon.effectText) + settings.end)
		time.sleep(1.3)
		
		# extraParam = Life Point Gain per Card in Hand

		handSize = effplayer.hand.__len__()

		print("{} has {} Cards in his Hand...".format(effplayer.name, effplayer.hand.__len__()))

		effplayer.gainLP(self.extraParam * handSize)

# NOT DESIGNED TO BE USED SOLELY BY ITSELF
class stealMonster(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		if opponent.monfield:
			opponent.checkField()
			while True:
				selection = input("~~Select a card to steal")

				try:
					selection = int(selection) - 1
					break
				except (TypeError, IndexError, AttributeError):
					print("--------------------------------------")
					print("Invalid Selection")

			monster = opponent.monfield[selection]

			effplayer.summon(monster)
			monster.attacked = 1
			del opponent.monfield[selection]

			print("--------------------------------------")
			print("{} has been stolen to {}'s Field".format(monster.name, effplayer.name))
		else:
			print("Opponent has no monsters to steal")

class controlStealMonster(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name) + settings.darkcyan + "{}".format(effectMon.effectText) + settings.end)
		time.sleep(1.3)
		
		# self.extraParam = Namespace to check for

		result = checkControlInstance(self.extraParam, effplayer.monfield, 2)

		if result:
			StealMonster.resolve(effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer)
		else:
			print("--------------------------------------")
			print("You need to control 2 {} monsters to resolve {}'s effect".format(self.extraParam, effectMon.name))

class tributetoSteal(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("--------------------------------------")
		print("{}'s Effect Activates!".format(effectMon.name) + settings.darkcyan + "{}".format(effectMon.effectText) + settings.end)
		time.sleep(1.3)
		
		# self.extraParam = Namespace to check for

		if effectMon not in effplayer.monfield:
			print("{} has left field, effect ending...")
			time.sleep(0.5)
			return

		while True:
			print("--------------------------------------")
			print("Effect: {}".format(effectMon.effectText))
			selection = input("~~Tribute a monster for {}'s Effect? (Y/N)".format(effectMon.name))
			selection = str(selection)

			if selection == "Y" or selection == "y":
				print("--------------------------------------")

				if self.nextraParam:
					tempList = effplayer.checkSpecificField(self.extraParam, self.nextraParam)
				else:
					tempList = effplayer.checkSpecificField(self.extraParam)

				if not tempList:
					print("No targets to tribute...")
					return

				while True:
					selection = input("~~Please select a target to tribute: ")

					try:
						selection = int(selection) - 1

						if tempList:
							pass
						else:
							print("No Cards to tribute")
							return

						if selection in tempList:
							# Tribute the monster

							tributedCard = effplayer.monfield[selection]
							effplayer.sendToGrave(effplayer, opponent, tributedCard, oppMon, effgy, oppgy, turnPlayer)

							del effplayer.monfield[selection]
							print("{} has been tributed".format(tributedCard.name))
							# Steal a monster in its place

							print("--------------------------------------")
							StealMonster.resolve(effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer)

							break
						else:
							print("--------------------------------------")
							print("Invalid Selection")
					except (TypeError, IndexError):
						print("--------------------------------------")
						print("Invalid Selection")

			elif selection == "N" or selection == "n":
				return

class shuffleToSSGraveyard(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("--------------------------------------")
		print("{}'s Effect Activates!".format(effectMon.name) + settings.darkcyan + "{}".format(effectMon.effectText) + settings.end)
		time.sleep(1.3)
		
		# extraParam = No. of Cards to shuffle back

		effplayer.shuffleHandIntoDeck(self.extraParam)

		effplayer.ssGraveyard()

class drawForDifference(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("--------------------------------------")
		print("{}'s Effect Activates!".format(effectMon.name) + settings.darkcyan + "{}".format(effectMon.effectText) + settings.end)
		time.sleep(1.3)
		

		if effplayer.lifepoints > opponent.lifepoints:
			difference = effplayer.lifepoints - opponent.lifepoints
		else:
			difference = opponent.lifepoints - effplayer.lifepoints

		cardsDrawn = int(math.floor(difference / 1000))

		if cardsDrawn == 0:
			print("Difference is not greater than 1000, 0 cards drawn...")
		else:
			print("Difference is: {}".format(difference))
			effplayer.draw(cardsDrawn)

		time.sleep(1.3)

class tributeToDrawDisc(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name) + settings.darkcyan + "{}".format(effectMon.effectText) + settings.end)
		time.sleep(1.3)
		# extraParam = No of cards to draw

		while True:
			print("--------------------------------------")
			selection = input("Activate {}'s Effect? (Y/N)".format(effectMon.name))
			print("--------------------------------------")
			selection = str(selection)

			if selection == "Y" or selection == "y":

				monster = effectMon

				target = effplayer.checkArrayLoc(effplayer.monfield, monster)

				if not isinstance(target, int):
					print("--------------------------------------")
					print("--------------------------------------")
					print("--------------------------------------")
					print("--------------------------------------")
					print("checkArrayLoc Broke in this instance, producing: " + str(target))
					print("--------------------------------------")
					print("--------------------------------------")
					print("--------------------------------------")
					print("--------------------------------------")
					raise TypeError


				del effplayer.monfield[target]

				print("{} Has been tributed".format(effectMon.name))

				print("--------------------------------------")

				effplayer.effectdiscardCard(effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer)

				effplayer.draw(self.extraParam)

				effplayer.sendToGrave(effplayer, opponent, monster, oppMon, effgy, oppgy, turnPlayer)

				return
			elif selection == "N" or selection == "n":
				return

class phoenixResurrection(effect):
	@staticmethod
	def StandbyResolution(resolve, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		if resolve:
			if effplayer == turnPlayer:
				print("--------------------------------------")
				print("{}'s Effect Activates!".format(effectMon.name) + settings.darkcyan + "{}".format(effectMon.effectText) + settings.end)
				time.sleep(1.3)

				if effectMon in effplayer.gy:
					effplayer.monfield.append(effectMon)
					i = effplayer.checkArrayLoc(effplayer.gy, effectMon)
					del effplayer.gy[i]

					print(settings.green + "{}" + settings.end + " has been Special Summoned".format(effectMon.name))
					print(settings.green + "ATK: {} | Effect: ".format(str(effectMon.atkPoints), effectMon.effectText) + settings.end + settings.darkcyan + "{}" + settings.end)

					pass

					destroyAll.resolve(resolve, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer)

				else:
					if effplayer == turnPlayer:
						print("{} Must be in the graveyard to resolve this effect".format(effectMon.name))
			else:
				print("--------------------------------------")
				print("{}'s Effect Activates!".format(effectMon.name) + settings.darkcyan + "{}".format(effectMon.effectText) + settings.end)
				time.sleep(1.3)

				if effectMon in opponent.gy:
					opponent.monfield.append(effectMon)
					i = opponent.checkArrayLoc(opponent.gy, effectMon)
					del opponent.gy[i]

					print(settings.green + "{}".format(effectMon.name) + settings.end + " has been Special Summoned".format(effectMon.name))
					print(settings.green + "ATK: {} | Effect: ".format(str(effectMon.atkPoints), effectMon.effectText) + settings.end + settings.darkcyan + "{}".format(effectMon.effectText) + settings.end)

					pass

					print("--------------------------------------")
					print(settings.green + "{}".format(effectMon.name) + settings.end + " Nukes the field!")
					print("--------------------------------------")

					time.sleep(1.3)

					destroyAll.resolve(resolve, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer)

				else:
					print("{} Must be in the graveyard to resolve this effect".format(effectMon.name))

	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name) + settings.darkcyan + "{}".format(effectMon.effectText) + settings.end)
		time.sleep(1.3)

		settings.addStandbyEffectChecker(effectMon, self)
		print("{} will return next standby phase...".format(effectMon.name))

class ffSummon(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name) + settings.darkcyan + "{}".format(effectMon.effectText) + settings.end)
		time.sleep(1.3)
		# extraParam = namespace
		# nextraParam = namespace
		# dextraParam = no of different names fitting namespace

		count = 0
		tempList = []

		# Count the number of namespace Card in Grave
		for monster in effplayer.gy:
			if self.extraParam in monster.name and monster not in tempList or self.nextraParam in monster.name and monster not in tempList:
				count = count + 1
				tempList.append(monster)

		if count >= self.dextraParam:
			print("--------------------------------------")
			print("You meet the requirements to activate {}'s effect".format(effectMon.name))
			selection = input("Activate Effect? (Y/N): ")

			selection = str(selection)

			if selection == "Y" or selection == "y":

				# Do the thing
				i = 0
				x = self.dextraParam
				while i < self.dextraParam:
					effplayer.specialGraveyardSpecificNeg(self.extraParam, self.nextraParam)
					x = x - 1
					if x:
						print("{} More monsters to summon".format(x))
					i = i + 1

				return
			elif selection == "N" or selection == "n":
				return
		else:
			print("--------------------------------------")
			print("You DO NOT meet the requirements to activate {}'s effect".format(effectMon.name))
			return
		pass


class addEffect(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name) + settings.darkcyan + "{}".format(
			effectMon.effectText) + settings.end)
		time.sleep(1.3)
		# extraParam = Effect Dictionary

		effplayer.grantEffect(self.extraParam)


class addEffectSpecific(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name) + settings.darkcyan + "{}".format(
			effectMon.effectText) + settings.end)
		time.sleep(1.3)
		# extraParam = Effect Dictionary
		# nextraParsm = namespace
		# dextraParsm = namespace

		if self.dextraParam:
			effplayer.grantEffectSpecific(self.extraParam, self.nextraParam, self.dextraParam)
		else:
			effplayer.grantEffectSpecific(self.extraParam, self.nextraParam)


# Drawing Effects
playerDraw1 = playerDraw("Draw One Card", 1)
playerDraw2 = playerDraw("Draw Two Cards", 2)
controlStormriderDraw2 = controlDiscardDraw("If you control a Storm Rider; Discard 1 card; Draw 2 cards", "Storm Rider", 2)
DifferenceDraw = drawForDifference("Draw one card per 1000 point difference between both players lifepoints)", 0)
tribDisc1Draw2 = tributeToDrawDisc("You can tribute this card; Draw 2 cards, then discard one card", 2)

# Disruptive Effects
Destroy = effectDestroy("Destroy Your Opponents Monster", 0)
destroyEither = effectDestroyBoth("Destroy a monster on either player's field", 0)
destroyInHand = destroyHand("Destroy a monster in your hand", 0)
bounceMonster = fieldToHand("Bounce an Opponents Monster", 0)
controlStormriderDestroy = controlDestroy("If you control a 'Storm Rider' card, destroy up to 2 monsters your opponent controls", "Storm Rider", 2)
StealMonster = stealMonster("Steal an Opponents Monster", 0)
StormriderStealMonster = controlStealMonster("If you control 2 'Storm Rider' card; Switch player control of one opponents monster", "Storm Rider")
tributeStormtoSteal = tributetoSteal("You can tribute any number of 'Storm Rider' or 'Storm Bird' Cards; Switch player control of the identical amount of opponents monsters", "Storm Rider", "Storm Bird")
nukeField = destroyAll("Destroy all monsters on field")

# Restoration Effects
restore1000 = effectRestore("Restore Life Points by 1000", 1000)
restore2000 = effectRestore("Restore Life Points by 2000", 2000)
RestoreLPForHand1000 = gainLPforHand("Restore 1000 Life Points for Every card in your hand", 1000)

# Damaging Effects
Damage1000 = effectDamage("Damage Opponent by 1000", 1000)
Damage8000 = effectDamage("Damage Opponent by 8000", 8000)
DamageSelf = effectDamageSelf("Damage Player by 1000", 1000)
siphonLife800 = siphonLife("Steal 800 Life points from opponent", 800)
siphonLife1500 = siphonLife("Steal 1500 Life points from opponent", 1500)
siphonLifeAndMill1500 = siphonLifeAndMill("Steal 1500 and mill a card", 1500)
siphonLifeAndMill800 = siphonLifeAndMill("Steal 800 and mill a card", 800)

# Discarding Effects
playerDisc1 = effectPlayerRandDiscard("Player discards One Card", 1)
oppDisc1 = effectOpponentDiscard("Opponent Discards One Card", 1)
oppDisc2 = effectOpponentDiscard("Opponent Discards Two Cards", 2)

# Battle Phase Specific Effects
matchAttack = effectCrash("Copies Opponents Monsters Attack", 0)
battleImmune = noBattleDestruction("Is Not Destroyed by that battle", 0)
effectImmune = noEffectDestruction("Is Not Destroyed by that effect", 0)

# Card Searching Effects
effectSearch = searchDeck("Add a card from Deck to Hand", 0)
effectCodeSearch = searchSpecificDeckNamespace("Add a 'Code' or '-code' card from Deck to hand", "Code", "code")
effectCyberseSearch = searchSpecificDeck("Add a 'Cyberse' card from Deck to hand", "Cyberse")
effectVampSearch = searchSpecificDeck("Add a 'Vampire' card from Deck to hand", "Vampire")
effectHeraldSearch = searchSpecificDeck("Add a 'Herald' card from Deck to hand", "Herald")
effectAgentSearch = searchSpecificDeck("Add a 'Agent' card from Deck to hand", "Agent")
effectGishkiSearch = searchSpecificDeck("Add a 'Gishki' card from Deck to hand", "Gishki")
effectEvigishkiSearch = searchSpecificDeck("Add an 'Evigishki' card from Deck to hand", "Evigishki")
effectGishkiMirrorSearch = searchSpecificDeck("Add a 'Gishki Aquamirror' card from Deck to hand", "Gishki Aquamirror")
effectDarkMagicianSearch = searchSpecificDeck("Add a 'Dark Magician' card from your deck to your hand", "Dark Magician")
effectGirlSearch = searchSpecificDeck("Add a 'Magician Girl' from your Deck to your hand", "Magician Girl")
effectStormSearch = searchSpecificDeckNamespace("Add a 'Storm Rider' or 'Storm Bird' card from your deck to your hand", "Storm Rider", "Storm Bird")
effectFireSearch = searchSpecificDeckNamespace("Add a 'Fire Fist' or 'Fire King' card from your deck to your hand", "Fire Fist", "Fire King")

# Attack Manipulation Effects
gain500 = gainAttack("Gains 500 attack before battle. Loses attack upon destruction", 500)
gain1000 = gainAttack("Gains 1000 attack before battle. Loses attack upon destruction", 1000)
gainDifference = gainAttackDifference("Gain Atk Points equal to the difference between your lifepoints", 0)
grant800 = grantAttack("Grant a monster on your field 800 Attack (not including this card)", 800)
darkMagicianGain400 = gainAtkforInstance("Gain 400 attack for each 'Dark Magician' monster on the field or in your Graveyard", "Dark Magician", 400)
evigishkiGain400 = gainAtkforInstance("Gain 400 attack for each 'Evigishki' monster on the field or in the graveyard", "Evigishki", 400)
heraldGain400 = gainAtkforInstance("Gain 400 attack for each 'Herald' monster on the field or in the graveyard", "Herald", 400)
stormBirdGain400 = gainAtkforInstance("Gain 400 attack for each 'Storm Bird' monster on the field or in the graveyard", "Storm Bird", 400)
stormRiderGain400 = gainAtkforInstance("Gain 400 attack for each 'Storm Rider' monster on the field or in the graveyard", "Storm Rider", 400)
halfAtk = halfAttacked("Half the attacking monsters attack", 2)
halfAtkMsg = halfAttackedMessage("Half the attacking monsters attack", 2)
atk0 = zeroAttack("Reduce target monster's attack to 0", 0)
tribtoGrantAtk = tributetoGrantAttack("You can tribute this card: Grant another monster this monsters ATK points", 0)
grantStormriderAttack = grantAttackNamespace("For each 'Storm Rider' card on the field, grant a Card 300 ATK x No. of 'Storm Rider' Card on the field", "Storm Rider", 300)
atk100GrantAll = grantAll("Grant all monsters on field 100 Atk", 100)
atk500GrantAll = grantAll("Grant all monsters on field 500 Atk", 500)

# Summon Manipulation Effects
doubleSummon = extraNormalSummon("Gain an extra normal summon", 0)
specialAgentHand = specialSpecificHand("Special Summon an 'Agent' Monster from your hand", "Agent")
specialCyberseHand = specialSpecificHand("Special Summon a 'Cyberse' Monster from your hand", "Cyberse")
specialVampireHand = specialSpecificHand("Special Summon a 'Vampire' Monster from your hand", "Vampire")
specialGishkiHand = specialSpecificHand("Special Summon a 'Gishki' Monster from your hand", "Gishki")
specialDarkMagicianHand = specialExactHand("Special Summon a 'Dark Magician' from your hand", "Dark Magician")
specialMagicianGirlHand = specialSpecificHand("Special Summon a 'Magician Girl' Card from your hand", "Magician Girl")
specialStormBirdHand = specialSpecificHand("Special Summon a 'Storm Bird' Monster from your hand", "Storm Bird")
specialCodeHand = specialSpecificHand("Special Summon a 'Code' Monster from your hand", "Code")
specialfromHand = specialHand("Special Summon a monster from your hand", 0)
discSpecVampHand = discardToSpecialHand("Discard one card, Special Summon a vampire from your Hand", "Vampire")
discSpecStormGY = discardToSpecialGY("Discard one Card, Special Summon a 'Storm Bird' or 'Storm Rider' from your graveyard", "Storm Rider", "Storm Bird")
specialDarkMagicianDeck = specialDeckExact("Special Summon a Dark Magician from your Deck", "Dark Magician")
specialStormRiderDeck = specialDeckSpecific("Special Summon a 'Storm Rider' from your deck", "Storm Rider")
specialCodeDeck = specialDeckSpecific("Special Summon a 'Code' monster from your deck", "Code")
specialGishkiDeck = specialDeckSpecific("Special Summon a 'Gishki' monster from your deck", "Gishki")
specialAgentDeck = specialDeckSpecific("Special Summon a 'Agent' monster from your deck", "Agent")
specialHeraldDeck = specialDeckSpecific("Special Summon a 'Herald' monster from your deck", "Herald")
specialFormationDeck = specialDeckSpecific("Special Summon a 'Fire Formation' monster from your deck", "Fire Formation")
specialFistDeckLess2000 = specialDeckSpecificLessAttack("Special Summon a 'Fire Fist' monster from your deck (< 2000 ATK)", "Fire Fist", 2000)
specialGirlLess2000 = specialDeckSpecificLessAttack("Special Summon a 'Magician Girl' monster from your deck (< 2000 ATK)", "Magician Girl", 2000)
tribToSpecialStormBird = tributeTOSSDeckSpecific("You can tribute this card; Special summon a 'Storm Bird' card from your deck", "Storm Bird")
shuffleToSSGraveyard = shuffleToSSGraveyard("Shuffle 1 card from your hand into the deck; Special summon a monster from your Graveyard", 1)
specialFireKingGrave = specialGraveyardSpecific("Special Summon a Fire King or Fire Fist monster from your graveyard", "Fire Fist", "Fire King")
specialEffDestruction = specialMeHand("Special summon this card from your hand", 0)
FFSummon = ffSummon("If you have 3 different 'Fire Formation' cards in your graveyard, Special Summon 3 monsters from your graveyard (Summon Effects Negated)", "Fire Fist", "Fire King", 3)

# Recursion Effects
gyToHand = gyToHand("Return a card from your Graveyard to your Hand", 0)
Trib_SS_GY = tributeTOSSGy("you can Tribute this card: Special Summon a monster from the Graveyard", 0)
Mill = mill("Send one card from your deck to the graveyard", 0)

# Special Effects
PhoenixResurrection = phoenixResurrection("Next Standby Phase; Special Summon this card and destroy all monsters on the field", 0)

# Effect Manipulation Effects
GrantFloat1 = addEffect("Grant a monster on the field the effect: 'When sent to Graveyard; Draw 1 Card'",
                        {"effect"       : playerDraw1,
                         "effectTrigger": effTrigger.graveyard})
GrantFloat1Cyberse = addEffectSpecific(
	"Grant a 'Cyberse' monster on the field the effect: 'When sent to Graveyard; Draw 1 Card'", {"effect"       : playerDraw1,
	                                                                                             "effectTrigger": effTrigger.graveyard},
	"Cyberse")
