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
	def __init__(self, desc, extraParam=None, extraParam2=None):
		self.desc = desc
		self.extraParam = extraParam
		self.nextraParam = extraParam2

	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		raise NotImplementedError("Subclass must implement abstract method")

class effectDestroy(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name))
		print("--------------------------------------")
		time.sleep(1)
		

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
					opponent.destroyMonsterEff(oppMon, effplayer, opponent, oppMon, effectMon, effgy, oppgy, turnPlayer)
				else:
					pass
			else:
				opponent.destroyMonsterEff(oppMon, effplayer, opponent, oppMon, effectMon, effgy, oppgy, turnPlayer)
		else:
				print("No Opponent monster to destroy")
				return
		return -1

class controlDestroy(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name))
		print("--------------------------------------")
		time.sleep(1)
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

					if oppMon.trigger.name == "destructionEff":
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

class effectDamage(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name))
		print("--------------------------------------")
		time.sleep(1)
		
		# extraParam = Life Point loss

		opponent.loseLP(self.extraParam)

class effectDamageSelf(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name))
		print("--------------------------------------")
		time.sleep(1)
		
		# extra = Life Point Loss

		effplayer.loseLP(self.extraParam)

class effectRestore(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name))
		print("--------------------------------------")
		time.sleep(1)
		
		# extraParam = Life Point Gain

		effplayer.gainLP(self.extraParam)

class effectCrash(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name))
		print("--------------------------------------")
		time.sleep(1)

		try:
			effectMon.atkPoints = oppMon.atkPoints
			print("{} Copies the opponents attack!".format(effectMon.name))
			time.sleep(0.5)
			return 0
		except (AttributeError, UnboundLocalError):
			pass


class playerDraw(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name))
		print("--------------------------------------")
		time.sleep(1)
		
		# extraParam = No of Cards to Draw

		effplayer.draw(self.extraParam)

class controlDiscardDraw(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name))
		print("--------------------------------------")
		time.sleep(1)
		
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
		print("{}'s Effect Activates!".format(effectMon.name))
		print("--------------------------------------")
		time.sleep(1)
		
		# extraParam = Life Point Siphon Amount

		opponent.loseLP(self.extraParam)
		effplayer.gainLP(self.extraParam)

class mill(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name))
		print("--------------------------------------")
		time.sleep(1)
		

		effplayer.mill(effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer)

		time.sleep(1)

		pass

class siphonLifeAndMill(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name))
		print("--------------------------------------")
		time.sleep(1)
		
		# extraParam = Life Point Siphon Amount

		opponent.loseLP(self.extraParam)
		effplayer.gainLP(self.extraParam)

		print("--------------------------------------")
		time.sleep(0.5)

		# Mill a Card
		effplayer.mill(effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer)

		time.sleep(1)

		pass

class effectPlayerRandDiscard(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name))
		print("--------------------------------------")
		time.sleep(1)
		
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
		print("{}'s Effect Activates!".format(effectMon.name))
		print("--------------------------------------")
		time.sleep(1)
		
		# extraParam = No Of Cards to Discard

		x = 0

		while True:
			# Choose a random number in hand to discard
			handSize = opponent.hand.__len__()

			try:
				selection = random.randint(0, handSize - 1)
				opponent.discardCard(selection)

				x = x + 1

				if x == self.extraParam:
					break

			except IndexError:
				if opponent.hand.__len__() == 0:
					print("{}'s Hand is Empty".format(opponent.name))
					break
				else:
					print("Card is not in {}'s Hand".format(opponent.name))
					break

class noBattleDestruction(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name))
		print("--------------------------------------")
		time.sleep(1)

		print("{} cannot be destroyed by Battle".format(effectMon.name))

		return 1

class noEffectDestruction(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("Counter Monster Effect Activate!")
		print("--------------------------------------")
		time.sleep(1)

		print("{} cannot be destroyed by Effects".format(effectMon.name))

		return 1

class searchDeck(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name))
		print("--------------------------------------")
		time.sleep(1)
		

		effplayer.searchDeck()

class searchSpecificDeck(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name))
		print("--------------------------------------")
		time.sleep(1)
		
		# extraParam = Namespace to Search
		# nextraParam = Namespace to Search

		effplayer.searchSpecificDeck(self.extraParam)

class searchSpecificDeck2(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name))
		print("--------------------------------------")
		time.sleep(1)
		
		# extraParam = Namespace to Search
		# nextraParam = Namespace to Search

		effplayer.searchSpecificDeck(self.extraParam, self.nextraParam)

class extraNormalSummon(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name))
		print("--------------------------------------")
		time.sleep(1)
		

		print("You get one extra normal summon")

		settings.resetNormalSummon()

class gainAttack(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name))
		print("--------------------------------------")
		time.sleep(1)
		
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
		print("{}'s Effect Activates!".format(effectMon.name))
		print("--------------------------------------")
		time.sleep(1)
		

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
		print("{}'s Effect Activates!".format(effectMon.name))
		print("--------------------------------------")
		time.sleep(1)
		
		# extraParam = Attack Point Gain

		effplayer.grantAttack(self.extraParam, effectMon)

		return

class grantAttackNamespace(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name))
		print("--------------------------------------")
		time.sleep(1)
		
		# extraParam = Namespace to grant attack to
		# nextraParam = Amount of Attack per instance

		total = 0

		for monster in effplayer.monfield:
			if self.extraParam in monster.name:
				total = total + 1

		for monster in effplayer.monfield:
			if self.extraParam in monster.name:
				effplayer.grantAttack(total * self.nextraParam, effectMon)

class fieldToHand(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name))
		print("--------------------------------------")
		time.sleep(1)
		

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
		return 0

class gyToHand(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name))
		print("--------------------------------------")
		time.sleep(1)
		

		effplayer.graveyardToHand()

class tributeTOSSGy(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name))
		print("--------------------------------------")
		time.sleep(1)
		

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
		print("{}'s Effect Activates!".format(effectMon.name))
		time.sleep(1)
		
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
		print("{}'s Effect Activates!".format(effectMon.name))
		print("--------------------------------------")
		time.sleep(1)
		

		effplayer.specialHandEffect(effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer)
		return 0

class specialSpecificHand(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name))
		print("--------------------------------------")
		time.sleep(1)
		
		# extraParam = Namespace to special/search

		effplayer.specialHandSpecific(self.extraParam, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer)

class discardToSpecialHand(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name))
		print("--------------------------------------")
		time.sleep(1)
		
		# extraParam = Namespace to special/search

		effplayer.effectdiscardCard(effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer)

		effplayer.specialHandSpecific(self.extraParam, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer)

class discardToSpecialGY(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name))
		print("--------------------------------------")
		time.sleep(1)
		
		# extraParam = Namespace to special/search

		effplayer.effectdiscardCard(effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer)

		if self.extraParam and self.nextraParam:
			effplayer.specialGraveyardSpecific(effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer, self.extraParam, self.nextraParam, )
		else:
			effplayer.specialGraveyardSpecific(effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer, self.extraParam, )

class specialExactHand(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name))
		print("--------------------------------------")
		time.sleep(1)
		
		# extraParam = Namespace to special/search

		effplayer.specialHandExact(self.extraParam, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer)

class specialDeckExact(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name))
		print("--------------------------------------")
		time.sleep(1)
		
		# extraParam = Namespace to special/search

		effplayer.specialDeckExact(self.extraParam, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer)

class specialDeckSpecific(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name))
		print("--------------------------------------")
		time.sleep(1)
		# extraParam = Namespace to special/search

		effplayer.specialDeckSpecific(self.extraParam, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer)

class specialDeckSpecificLessAttack(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name))
		print("--------------------------------------")
		time.sleep(1)
		# extraParam = Namespace to special/search

		effplayer.specialDeckSpecificLessAttack(self.extraParam, self.nextraParam, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer)

class gainAtkforInstance(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name))
		print("--------------------------------------")
		time.sleep(1)
		
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

class halfAttackedDraw(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name))
		print("--------------------------------------")
		time.sleep(1)
		
		# extraParam = No of Cards to draw

		oppMon.atkPoints = int(oppMon.atkPoints / 2)
		print("{}'s ATK points have been halved to {}".format(oppMon.name, oppMon.atkPoints))

		effplayer.draw(self.extraParam)

class zeroAttack(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name))
		print("--------------------------------------")
		time.sleep(1)
		

		oppMon.atkPoints = 0
		print("{}'s ATK points have been reduced to 0".format(oppMon.name))

		time.sleep(1)

class tributetoGrantAttack(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("{}'s Effect Activates!".format(effectMon.name))
		time.sleep(1)
		

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
		print("{}'s Effect Activates!".format(effectMon.name))
		time.sleep(1)
		
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
		print("{}'s Effect Activates!".format(effectMon.name))
		time.sleep(1)
		
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
		print("{}'s Effect Activates!".format(effectMon.name))
		time.sleep(1)
		
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
		print("{}'s Effect Activates!".format(effectMon.name))
		time.sleep(1)
		
		# extraParam = No. of Cards to shuffle back

		effplayer.shuffleHandIntoDeck(self.extraParam)

		effplayer.ssGraveyard()

class drawForDifference(effect):
	def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
		print("--------------------------------------")
		print("{}'s Effect Activates!".format(effectMon.name))
		time.sleep(1)
		

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

		time.sleep(1)

# Define the effects used

# Drawing Effects
playerDraw1 = playerDraw("Draw One Card", 1)
playerDraw2 = playerDraw("Draw Two Cards", 2)
controlStormriderDraw2 = controlDiscardDraw("If you control a Stormrider; Discard 1 card; Draw 2 cards", "Stormrider", 2)
DifferenceDraw = drawForDifference("Draw one card per 1000 point difference between both players lifepoints)", 0)

# Disruptive Effects
Destroy = effectDestroy("Destroy Your Opponents Monster", 0)
bounceMonster = fieldToHand("Bounce an Opponents Monster", 0)
controlStormriderDestroy = controlDestroy("If you control a 'Stormrider' card, destroy up to 2 monsters your opponent controls", "Stormrider", 2)
StealMonster = stealMonster("Steal an Opponents Monster", 0)
StormriderStealMonster = controlStealMonster("If you control 2 'Stormrider' card; Switch player control of one opponents monster", "Stormrider")
tributeStormtoSteal = tributetoSteal("You can tribute any number of 'Stormrider' or 'Stormbird' Cards; Switch player control of the identical amount of opponents monsters", "Stormrider", "Stormbird")

# Restoration Effects
Restore1000 = effectRestore("Restore Life Points by 1000", 1000)
Restore2000 = effectRestore("Restore Life Points by 2000", 2000)
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
effectCodeSearch = searchSpecificDeck("Add a 'Code' card from Deck to hand", "Code")
effectCyberseSearch = searchSpecificDeck("Add a 'Cyberse' card from Deck to hand", "Cyberse")
effectVampSearch = searchSpecificDeck("Add a 'Vampire' card from Deck to hand", "Vampire")
effectHeraldSearch = searchSpecificDeck("Add a 'Herald' card from Deck to hand", "Herald")
effectAgentSearch = searchSpecificDeck("Add a 'Agent' card from Deck to hand", "Agent")
effectGishkiSearch = searchSpecificDeck("Add a 'Gishki' card from Deck to hand", "Gishki")
effectEvigishkiSearch = searchSpecificDeck("Add an 'Evigishki' card from Deck to hand", "Evigishki")
effectGishkiMirrorSearch = searchSpecificDeck("Add a 'Gishki Aquamirror' card from Deck to hand", "Gishki Aquamirror")
effectDarkMagicianSearch = searchSpecificDeck("Add a 'Dark Magician' card from your deck to your hand", "Dark Magician")
effectGirlSearch = searchSpecificDeck("Add a 'Magician Girl' from your Deck to your hand", "Magician Girl")
effectStormSearch = searchSpecificDeck2("Add a 'Stormrider' or 'Stormbird' card from your deck to your hand", "Stormrider", "Stormbird")

# Attack Manipulation Effects
gain500 = gainAttack("Gains 500 attack before battle. Loses attack upon destruction", 500)
gain1000 = gainAttack("Gains 1000 attack before battle. Loses attack upon destruction", 1000)
gainDifference = gainAttackDifference("Gain Atk Points equal to the difference between your lifepoints", 0)
grant800 = grantAttack("Grant a monster on your field 800 Attack (not including this card)", 800)
darkMagicianGain500 = gainAtkforInstance("Gain 400 attack for each 'Dark Magician' monster on the field or in your Graveyard", "Dark Magician", 400)
evigishkiGain400 = gainAtkforInstance("Gain 400 attack for each 'Evigishki' monster on the field or in the graveyard", "Evigishki", 400)
halfAtkDraw2 = halfAttackedDraw("Half the attacking monsters attack; Draw Two Cards", 2)
Atk0 = zeroAttack("Reduce target monster's attack to 0", 0)
tribtoGrantAtk = tributetoGrantAttack("You can tribute this card: Grant another monster this monsters ATK points", 0)
grantStormriderAttack = grantAttackNamespace("For each 'Stormrider' card on the field, grant a Card 300 ATK x No. of 'Stormrider' Card on the field", "Stormrider", 300)

# Summon Manipulation Effects
doubleSummon = extraNormalSummon("Gain an extra normal summon", 0)
specialAgentHand = specialSpecificHand("Special Summon an 'Agent' Monster from your hand", "Agent")
specialCyberseHand = specialSpecificHand("Special Summon a 'Cyberse' Monster from your hand", "Cyberse")
specialVampireHand = specialSpecificHand("Special Summon a 'Vampire' Monster from your hand", "Vampire")
specialGishkiHand = specialSpecificHand("Special Summon a 'Gishki' Monster from your hand", "Gishki")
specialDarkMagicianHand = specialExactHand("Special Summon a 'Dark Magician' from your hand", "Dark Magician")
specialMagicianGirlHand = specialSpecificHand("Special Summon a 'Magician Girl' Card from your hand", "Magician Girl")
specialStormBirdHand = specialSpecificHand("Special Summon a 'Stormbird' Monster from your hand", "Stormbird")
specialCodeHand = specialSpecificHand("Special Summon a 'Code' Monster from your hand", "Code")
specialfromHand = specialHand("Special Summon a monster from your hand", 0)
discSpecVampHand = discardToSpecialHand("Discard one card, Special Summon a vampire from your Hand", "Vampire")
discSpecStormGY = discardToSpecialGY("Discard one Card, Special Summon a 'Stormbird' or 'Stormrider' from your graveyard", "Stormrider", "Stormbird")
specialDarkMagicianDeck = specialDeckExact("Special Summon a Dark Magician from your Deck", "Dark Magician")
specialStormRiderDeck = specialDeckSpecific("Special Summon a 'Stormrider' from your deck", "Stormrider")
specialCodeDeck = specialDeckSpecific("Special Summon a 'Code' monster from your deck", "Code")
specialGishkiDeck = specialDeckSpecific("Special Summon a 'Gishki' monster from your deck", "Gishki")
specialAgentDeck = specialDeckSpecific("Special Summon a 'Agent' monster from your deck", "Agent")
specialHeraldDeck = specialDeckSpecific("Special Summon a 'Herald' monster from your deck", "Herald")
specialGirlLess2000 = specialDeckSpecificLessAttack("Special Summon a 'Magician Girl' monster from your deck with less than 2000 attack", "Magician Girl", 2000)
tribToSpecialStormBird = tributeTOSSDeckSpecific("You can tribute this card; Special summon a 'Stormbird' card from your deck", "Stormbird")
shuffleToSSGraveyard = shuffleToSSGraveyard("Shuffle 1 card from your hand into the deck; Special summon a monster from your Graveyard", 1)

# Recursion Effects
gyToHand = gyToHand("Return a card from your Graveyard to your Hand", 0)
Trib_SS_GY = tributeTOSSGy("you can Tribute this card: Special Summon a monster from the Graveyard", 0)
Mill = mill("Send one card from your deck to the graveyard", 0)

# Effect Manipulation Effects

