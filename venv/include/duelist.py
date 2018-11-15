import sys
from effect import *
from card import *


class duelist:

	# Duelist Constructor
	def __init__(self, name: str, lifepoints: int, hand: list, monfield: list, deck: list, graveyard: list):
		# Paramerters
		self.name = name
		self.lifepoints = lifepoints
		self.hand = hand
		self.monfield = monfield
		self.deck = deck
		self.gy = graveyard

	# Return largest string in an array (menu formatting)
	@staticmethod
	def getMaxLength(monarray: list):

		max_len = ""
		# Figure out longest string that exists
		for monster in monarray:
			if len(max_len) < len(monster.name):
				max_len = monster.name
			else:
				pass

		return len(max_len)

	# Return a specific list location for a Card
	@staticmethod
	def checkArrayLoc(array: list, monster: object):
		i = 0
		for m in array:
			if m == monster:
				return i
			i = i + 1

	# Add card(s) to Hand
	def draw(self, noOfCards):

		# Check if deck empty, and if so, that player loses
		if self.deck.__len__() == 0:
			print("{} has run out of cards in his deck, he loses the game".format(self.name))
			time.sleep(1)
			input("Press the enter key to exit")
			sys.exit(0)

		# Check if the amount of cards being drawn is more than 1
		if noOfCards > 1:
			print("{} Draws {} cards...".format(self.name, noOfCards))
		else:
			print("{} Draws {} card...".format(self.name, noOfCards))

		# Loop through the amount of cards, removing them
		# from the deck and appending them to the hand array
		i = 0

		while i <= noOfCards - 1:
			# Add card from deck to hand
			card = self.deck[0]
			self.hand.append(card)

			# Removing card from deck
			del self.deck[0]

			# Increment
			i = i + 1

	def searchSpecificDeck(self, name):
		if self.deck.__len__() == 0:
			print("Deck is empty")
			return

		i = 0
		tempListNum = []
		print("{}s Deck:".format(self.name))

		max_len = self.getMaxLength(self.deck)

		# Loop through the hand and display each card fitting the namespace
		for monster in self.deck:
			if name in monster.name:
				if i >= 9:
					print("[{}] {} | ATK: {} | Tributes: {} | Effect: {}".format((i + 1), monster.name.ljust(max_len, ),
																				 str(monster.atkPoints).ljust(4, ),
																				 monster.tribute, monster.effectText))
				else:
					print(
						"[{}]  {} | ATK: {} | Tributes: {} | Effect: {}".format((i + 1), monster.name.ljust(max_len, ),
																				str(monster.atkPoints).ljust(4, ),
																				monster.tribute, monster.effectText))
				tempListNum.append(i)
			else:
				pass

			i = i + 1

		if tempListNum:
			while True:
				# Get user Selection
				selection = input("~~~Select the card to Add (Type the Number):")

				try:
					selection = int(selection) - 1
				except ValueError:
					pass

				# Add the card to the hand
				if selection in tempListNum:
					addedCard = self.deck[selection]
					self.hand.append(addedCard)
					print("--------------------------------------")
					print("{} has searched the following card:".format(self.name))
					print("Name: {} | ATK: {} | Effect: {}".format(addedCard.name, str(addedCard.atkPoints),
																   addedCard.effectText))

					del self.deck[selection]

					self.shuffle()

					return
				else:
					print("--------------------------------------")
					print("Invalid Selection")
					print("--------------------------------------")
		else:
			print("No Cards to search")
			return

	# Add a specific card from deck to hand matching a namespace
	def searchSpecificDeckNamespace(self, *names):
		if self.deck.__len__() == 0:
			print("Deck is empty")
			return

		i = 0
		tempListNum = []
		print("{}s Deck:".format(self.name))

		max_len = self.getMaxLength(self.deck)

		# Loop through the hand and display each card fitting the namespace
		for monster in self.deck:
			for name in names:
				if name in monster.name:
					if i >= 9:
						print("[{}] {} | ATK: {} | Tributes: {} | Effect: {}".format((i + 1), monster.name.ljust(max_len, ), str(monster.atkPoints).ljust(4, ), monster.tribute, monster.effectText))
					else:
						print("[{}]  {} | ATK: {} | Tributes: {} | Effect: {}".format((i + 1), monster.name.ljust(max_len, ), str(monster.atkPoints).ljust(4, ), monster.tribute, monster.effectText))
					tempListNum.append(i)
				else:
					pass

			i = i + 1

		if tempListNum:
			while True:
				# Get user Selection
				selection = input("~~~Select the card to Add (Type the Number):")

				try:
					selection = int(selection) - 1
				except ValueError:
					pass

				# Add the card to the hand
				if selection in tempListNum:
					addedCard = self.deck[selection]
					self.hand.append(addedCard)
					print("--------------------------------------")
					print("{} has searched the following card:".format(self.name))
					print("Name: {} | ATK: {} | Effect: {}".format(addedCard.name, str(addedCard.atkPoints), addedCard.effectText))

					del self.deck[selection]

					self.shuffle()

					return
				else:
					print("--------------------------------------")
					print("Invalid Selection")
					print("--------------------------------------")
		else:
			print("No Cards to search")
			return

	# Return a list of names on field specific to a namespace(s)
	def checkSpecificField(self, *names):
		tempListNum = []

		if self.monfield.__len__() > 0:

			i = 0
			print("{}s Field:".format(self.name))

			max_len = self.getMaxLength(self.monfield)

			# Loop through the hand and display each card fitting the namespace
			for monster in self.monfield:
				for name in names:
					if name in monster.name:
						if i >= 9:
							print("[{}] {} | ATK: {} | Tributes: {} | Effect: {}".format((i + 1), monster.name.ljust(max_len, ), str(monster.atkPoints).ljust(4, ), monster.tribute, monster.effectText))
						else:
							print("[{}]  {} | ATK: {} | Tributes: {} | Effect: {}".format((i + 1), monster.name.ljust(max_len, ), str(monster.atkPoints).ljust(4, ), monster.tribute, monster.effectText))
						tempListNum.append(i)
					else:
						pass

				i = i + 1

			return tempListNum
		else:
			print("No Other Monsters on your field")
			return tempListNum

	# Add a specific card from deck to hand
	def searchDeck(self):

		if self.deck.__len__() == 0:
			print("Deck is empty")
			return

		# Loop through deck array and ask duelist which card to add
		while True:
			# Display Cards
			self.checkDeck()

			# Get user selection
			selection = input("~~~Select the card to Add (Type the Number):")

			try:
				selection = int(selection) - 1
			except ValueError:
				pass

			try:
				if self.deck.__len__() - 1 >= selection >= 0:
					addedCard = self.deck[selection]

					self.shuffle()

					break
				else:
					print("--------------------------------------")
					print("Invalid Selection")
					print("--------------------------------------")
			except TypeError:
				print("--------------------------------------")
				print("Invalid Selection")
				print("--------------------------------------")

		# Add Selection to hand and remove from deck

		self.hand.append(addedCard)
		print("--------------------------------------")
		print("{} has searched the following card:".format(self.name))
		print("Name: {} | ATK: {} | Tribute: {} | Effect: {}".format(addedCard.name, str(addedCard.atkPoints), str(addedCard.tribute), addedCard.effectText))

		del self.deck[selection]

	# Display Player Hand
	def checkHand(self):
		if self.hand.__len__() != 0:
			i = 0

			max_len = self.getMaxLength(self.hand)

			for monster in self.hand:
				if i >= 9:
					print("[{}] {} | ATK: {} | Tributes: {} | Effect: {}".format((i + 1), monster.name.ljust(max_len, ), str(monster.atkPoints).ljust(4, ), monster.tribute, monster.effectText))
				else:
					print(
						"[{}]  {} | ATK: {} | Tributes: {} | Effect: {}".format((i + 1), monster.name.ljust(max_len, ), str(monster.atkPoints).ljust(4, ), monster.tribute, monster.effectText))
				i = i + 1
		else:
			print("Hand Empty")
			return

	# Display Player Field
	def checkField(self):
		# check the monster zone array

		if self.monfield.__len__() != 0:
			i = 0

			max_len = self.getMaxLength(self.monfield)

			for monster in self.monfield:
				if i >= 9:
					print("[{}] {} | ATK: {} | Tributes: {} | Effect: {}".format((i + 1), monster.name.ljust(max_len, ), str(monster.atkPoints).ljust(4, ), monster.tribute, monster.effectText))
				else:
					print(
						"[{}]  {} | ATK: {} | Tributes: {} | Effect: {}".format((i + 1), monster.name.ljust(max_len, ), str(monster.atkPoints).ljust(4, ), monster.tribute, monster.effectText))
				i = i + 1
		else:
			print("Field Empty")
			return

	# Display all monsters who have not attacked
	def checkFieldAtk(self):
		# check the monster zone array

		if self.monfield.__len__() != 0:
			i = 0

			max_len = self.getMaxLength(self.monfield)

			for monster in self.monfield:
				if monster.attacked == 0:
					if i >= 9:
						print("[{}] {} | ATK: {} | Tributes: {} | Effect: {}".format((i + 1), monster.name.ljust(max_len, ), str(monster.atkPoints).ljust(4, ), monster.tribute, monster.effectText))
					else:
						print(
							"[{}]  {} | ATK: {} | Tributes: {} | Effect: {}".format((i + 1), monster.name.ljust(max_len, ), str(monster.atkPoints).ljust(4, ), monster.tribute, monster.effectText))
				else:
					pass
				i = i + 1
		else:
			print("Field Empty")
			return

	# Display Player Deck
	def checkDeck(self):
		print("{}s Deck:".format(self.name))

		if self.deck.__len__() != 0:
			i = 0

			max_len = self.getMaxLength(self.deck)

			for monster in self.deck:
				if i >= 9:
					print("[{}] {} | ATK: {} | Tributes: {} | Effect: {}".format((i + 1), monster.name.ljust(max_len, ), str(monster.atkPoints).ljust(4, ), monster.tribute, monster.effectText))
				else:
					print("[{}]  {} | ATK: {} | Tributes: {} | Effect: {}".format((i + 1), monster.name.ljust(max_len, ), str(monster.atkPoints).ljust(4, ), monster.tribute, monster.effectText))
				i = i + 1
		else:
			print("Deck Empty")
			return

	# Display Player Graveyard
	def checkGraveyard(self):
		print("{}s Graveyard:".format(self.name))

		if self.gy.__len__() != 0:
			i = 0

			max_len = self.getMaxLength(self.gy)

			for monster in self.gy:
				if i >= 9:
					print("[{}] {} | ATK: {} | Tributes: {} | Effect: {}".format((i + 1), monster.name.ljust(max_len, ), str(monster.atkPoints).ljust(4, ), monster.tribute, monster.effectText))
				else:
					print(
						"[{}]  {} | ATK: {} | Tributes: {} | Effect: {}".format((i + 1), monster.name.ljust(max_len, ), str(monster.atkPoints).ljust(4, ), monster.tribute, monster.effectText))
				i = i + 1
		else:
			print("Graveyard Empty")
			return

	# Special Summon from Graveyard
	def ssGraveyard(self):

		if self.gy.__len__() == 0:
			print("Graveyard is Empty")
			return

		while True:
			self.checkGraveyard()

			selection = input("~~Please select a monster to Special Summon:")

			try:
				selection = int(selection) - 1
			except ValueError:
				pass

			try:
				if self.gy.__len__() - 1 >= selection >= 0:
					playedCard = self.gy[selection]
					break
				else:
					print("--------------------------------------")
					print("Invalid Selection")
					print("--------------------------------------")
			except TypeError:
				print("--------------------------------------")
				print("Invalid Selection")
				print("--------------------------------------")

		pass

		self.summon(playedCard)
		print("--------------------------------------")
		print("{} has been Special Summoned".format(playedCard.name))
		print("ATK: {} | Effect: {}".format(str(playedCard.atkPoints), playedCard.effectText))
		time.sleep(1)

	# Return card from Graveyard to Hand
	def graveyardToHand(self):
		if self.gy.__len__() == 0:
			print("Graveyard is Empty")
			return

		while True:
			self.checkGraveyard()

			selection = input("~~Please select a monster to Add to Hand")

			try:
				selection = int(selection) - 1
			except ValueError:
				pass

			try:
				if self.gy.__len__() - 1 >= selection >= 0:
					addedCard = self.gy[selection]
					break
				else:
					print("--------------------------------------")
					print("Invalid Selection")
					print("--------------------------------------")
			except TypeError:
				print("--------------------------------------")
				print("Invalid Selection")
				print("--------------------------------------")

		self.hand.append(addedCard)

		del self.gy[selection]

		print("--------------------------------------")
		print("{} has been added to {}'s Hand".format(addedCard.name, self.name))
		print("ATK: {} | Effect: {}".format(str(addedCard.atkPoints), addedCard.effectText))

	def summon(self, monster: card):
		if self.monfield.__len__() == 5:
			print("Monster Field is Full, cannot Summon")
			return 0
		else:
			self.monfield.append(monster)
			return 1

	# Send card to Grave
	def sendToGrave(self, effplayer, opponent, sentMon, oppMon, effgy, oppgy, turnPlayer):

		self.gy.append(sentMon)

		sentMon.ResolveEffect(effTrigger.graveyard, effplayer, opponent, sentMon, oppMon, effgy, oppgy, turnPlayer)

		self.shuffle()

	# Send a card from Deck to grave
	def mill(self, effplayer, opponent, sentMon, oppMon, effgy, oppgy, turnPlayer):
		del sentMon

		if self.deck.__len__() == 0:
			print("Deck is empty")
			return

		# Loop through deck array and ask duelist which card to add
		while True:
			# Display Cards
			self.checkDeck()

			# Get user selection
			selection = input("~~~Select the card to Mill (Type the Number):")

			try:
				selection = int(selection) - 1
			except ValueError:
				pass

			try:
				if self.deck.__len__() - 1 >= selection >= 0:
					milledCard = self.deck[selection]
					break
				else:
					print("--------------------------------------")
					print("Invalid Selection")
					print("--------------------------------------")
			except TypeError:
				print("--------------------------------------")
				print("Invalid Selection")
				print("--------------------------------------")

		# Add Selection to gy and remove from deck

		print("--------------------------------------")
		print("{} has milled the following card:".format(self.name))
		print("Name: {} | ATK: {} | Effect: {}".format(milledCard.name, str(milledCard.atkPoints), milledCard.effectText))

		del self.deck[selection]

		self.shuffle()

		self.sendToGrave(effplayer, opponent, milledCard, oppMon, effgy, oppgy, turnPlayer)

	# Play Card from hand
	def playCard(self):

		# Loop through hand array and ask duelist which card to play
		while True:
			# Display Cards
			self.checkHand()

			# Get user selection
			print("[0]  Return")
			selection = input("~~~Select A Card to play: ")

			try:
				selection = int(selection) - 1
			except ValueError:
				pass

			try:
				if selection == -1:
					return 0
				elif self.hand.__len__() - 1 >= selection >= 0:
					playedCard = self.hand[selection]
					break
				else:
					print("--------------------------------------")
					print("Invalid Selection")
					print("--------------------------------------")
			except TypeError:
				print("--------------------------------------")
				print("Invalid Selection")
				print("--------------------------------------")

		nSummon = int(settings.returnNormalSummon())

		# If you have not normal summoned this turn
		if nSummon == 0:
			# If there is a monster already on the field
			if self.monfield:
				# If the monster requires a tribute
				if playedCard.tribute == 1:
					# Display Current Field

					print("--------------------------------------")

					self.checkField()

					# Allow user to choose which monster to Tribute
					selectionTrib = input(
						"~~{} requires {} Tribute. Select a monster to tribute:".format(playedCard.name, playedCard.tribute))
					selectionTrib = int(selectionTrib) - 1

					# Tribute the selection
					tribute = self.monfield[selectionTrib]
					del self.monfield[selectionTrib]
					print("{} has been tributed".format(tribute.name))

					# Play the card from your hand
					self.monfield.append(playedCard)
					self.removeCard(selection)
					self.gy.append(tribute)

					settings.changeNormalSummon()  # Normal Summon = 1

					print("--------------------------------------")

					# Print the stats of the played card
					print("{} has Played ~{}~ from their hand".format(self.name, playedCard.name))
					print("ATK: {} | Effect: {}".format(str(playedCard.atkPoints), playedCard.effectText))

					# Return Result
					return 1  # 1 = Successful Summon

				# If the monster does not require a tribute
				elif playedCard.tribute == 0:
					# Play the card from your hand
					self.monfield.append(playedCard)
					self.removeCard(selection)
					settings.changeNormalSummon()  # Normal Summon = 1

					print("--------------------------------------")

					# Print the stats of the played card
					print("{} has Played ~{}~ from their hand".format(self.name, playedCard.name))
					print("ATK: {} | Effect: {}".format(str(playedCard.atkPoints), playedCard.effectText))

					# Return Result
					return 1  # 1 = Successful Summon

			# If there is not a monster on the field
			else:
				# If the monster required a tribute
				if playedCard.tribute == 1:
					# Print the requirements
					print("--------------------------------------")
					print("Monsters requires One Tribute")

					# Return the result
					return 0  # 0 = Failed Summon

				# If the monster does not require a tribute
				if playedCard.tribute == 0:
					# Play the card from your hand
					self.monfield.append(playedCard)
					self.removeCard(selection)
					settings.changeNormalSummon()  # Normal Summon = 1

					print("--------------------------------------")

					# Print the stats of the played card
					print("{} has Played ~{}~ from their hand".format(self.name, playedCard.name))
					print("ATK: {} | Effect: {}".format(str(playedCard.atkPoints), playedCard.effectText))

					# Return Result
					return 1  # 1 = Successful Summon
		# If you have normal summoned this turn
		else:
			# Print the requirements
			print("--------------------------------------")
			print("You have used your normal summon for the turn")

			# Return the result
			return 0  # 0 = Failed Summon

	# Display LP and Deck
	def checkLP_Deck(self):
		print("{}:".format(self.name))
		print("Life Points: {} | Cards left in Deck: {}".format(self.lifepoints, self.deck.__len__()))

	# Shuffle Deck
	def shuffle(self):
		random.shuffle(self.deck)
		print("Deck Shuffled")
		time.sleep(0.5)

	# Remove Card from Hand (as destinct from Discarding)
	def removeCard(self, selection):
		try:
			del self.hand[selection]
		except IndexError:
			if self.hand.__len__() == 0:
				print("Hand is Empty")
			else:
				print("Card is not in Hand")

	# Discard Card from Hand
	def discardCard(self, selection):
		try:
			monster = self.hand[selection]
			del self.hand[selection]

			self.gy.append(monster)

			print("The Following card was discarded from {}'s Hand:".format(self.name))
			print("{} | ATK: {} | Effect: {}".format(monster.name, monster.atkPoints, monster.effectText))
		except IndexError:
			if self.hand.__len__() == 0:
				print("Hand is Empty")
			else:
				print("Card is not in Hand")

	def shuffleHandIntoDeck(self, noOfCards):
		x = 0
		while x < noOfCards:
			while True:
				self.checkHand()

				selection = input("~~Please select a monster to Shuffle:")

				try:
					selection = int(selection) - 1
				except ValueError:
					pass

				try:
					if self.hand.__len__() - 1 >= selection >= 0:
						shuffledCard = self.hand[selection]
						break
					else:
						print("--------------------------------------")
						print("Invalid Selection")
						print("--------------------------------------")
				except TypeError:
					print("--------------------------------------")
					print("Invalid Selection")
					print("--------------------------------------")

			pass

			self.deck.append(shuffledCard)
			del self.hand[selection]

			print("{} has been shuffled into the deck".format(shuffledCard.name))

			x = x + 1

		time.sleep(0.5)

	def effectdiscardCard(self, effplayer, opponent, effMon, oppMon, effgy, oppgy, turnPlayer):
		del effMon

		if self.hand.__len__() == 0:
			print("Hand is empty")

			return

		while True:
			self.checkHand()

			selection = input("~~Please select a monster to Discard:")

			try:
				selection = int(selection) - 1
			except ValueError:
				pass

			try:
				if self.hand.__len__() - 1 >= selection >= 0:
					discardedCard = self.hand[selection]
					break
				else:
					print("--------------------------------------")
					print("Invalid Selection")
					print("--------------------------------------")
			except TypeError:
				print("--------------------------------------")
				print("Invalid Selection")
				print("--------------------------------------")

		pass

		effplayer.gy.append(discardedCard)
		del self.hand[selection]

		print("{} has been discarded from {}'s hand".format(discardedCard.name, self.name))

		time.sleep(1)


		discardedCard.ResolveEffect(effTrigger.graveyard, effplayer, opponent, discardedCard, oppMon, effgy, oppgy, turnPlayer)

	# Lose LifePoints
	def loseLP(self, damage):

		# Calculate damage and print result
		self.lifepoints = self.lifepoints - damage

		if self.lifepoints < 0:
			self.lifepoints = 0

		print("{} has taken {} points of damage, and is now on {} life points".format(self.name, damage, self.lifepoints))
		if self.lifepoints == 0:
			print("~~~{} has reached {} lifepoints, the game is over. Returning to Main Menu...".format(self.name, self.lifepoints))
			time.sleep(2)

	# Gain LifePoints
	def gainLP(self, heal):

		# Calculate heal and print result
		self.lifepoints = self.lifepoints + heal
		print("{} has gained {} life points, and is now on {}".format(self.name, heal, self.lifepoints))

	# Destroy Monster (Battle)
	def destroyMonsterBat(self, target, effplayer, opponent, sentMon, oppMon, effgy, oppgy, turnPlayer):
		del sentMon

		location = self.checkArrayLoc(self.monfield, target)

		# Select the destroyed Monster
		try:
			destroyedMonster = self.monfield[location]
		except (IndexError, TypeError):
			return 0

		# resetting attack values, for the AtkGain Effect
		destroyedMonster.atkPoints = destroyedMonster.origAtk

		# Remove from field array
		del self.monfield[location]

		time.sleep(0.5)

		# Append to graveyard and print result
		self.gy.append(destroyedMonster)
		print("{} has been destroyed and sent to the Graveyard".format(destroyedMonster.name))

		destroyedMonster.ResolveEffect(effTrigger.graveyard, effplayer, opponent, destroyedMonster, oppMon, effgy, oppgy, turnPlayer)


	# Destroy Monster (Effect)
	def destroyMonsterEff(self, target, effplayer, opponent, sentMon, oppMon, effgy, oppgy, turnPlayer):
		del sentMon

		location = self.checkArrayLoc(self.monfield, target)

		# Select the destroyed Monster
		destroyedMonster = self.monfield[location]

		# resetting attack values, for the AtkGain Effect
		destroyedMonster.atkPoints = destroyedMonster.origAtk

		# Remove from field array
		del self.monfield[location]

		# Append to graveyard and print result
		self.gy.append(destroyedMonster)
		print("{} has been destroyed and sent to the Graveyard".format(destroyedMonster.name))

		time.sleep(0.5)

		destroyedMonster.ResolveEffect(effTrigger.graveyard, effplayer, opponent, destroyedMonster, oppMon, effgy, oppgy, turnPlayer)

	# Return Monster to Opponents Hand
	def bounce(self, target):
		location = self.checkArrayLoc(self.monfield, target)

		# Select the destroyed Monster
		bouncedMonster = self.monfield[location]

		# resetting attack values, for the AtkGain Effect
		bouncedMonster.atkPoints = bouncedMonster.origAtk

		# Remove from field array
		del self.monfield[location]

		# Append to graveyard and print result
		self.hand.append(bouncedMonster)
		print("{} has been returnd to {}'s Hand".format(bouncedMonster.name, self.name))

	# Special Summon a Monster from your Hand
	def specialHandEffect(self, effplayer, opponent, sentMon, oppMon, effgy, oppgy, turnPlayer):

		del sentMon

		if self.hand.__len__() == 0:
			print("Hand is empty")

			return

		while True:
			self.checkHand()

			selection = input("~~Please select a monster to Special Summon:")

			try:
				selection = int(selection) - 1
			except ValueError:
				pass

			try:
				if self.hand.__len__() - 1 >= selection >= 0:
					specialedCard = self.hand[selection]
					break
				else:
					print("--------------------------------------")
					print("Invalid Selection")
					print("--------------------------------------")
			except TypeError:
				print("--------------------------------------")
				print("Invalid Selection")
				print("--------------------------------------")

		pass

		self.summon(specialedCard)
		del self.hand[selection]
		print("--------------------------------------")
		print("{} has been Special Summoned".format(specialedCard.name))
		print("ATK: {} | Effect: {}".format(str(specialedCard.atkPoints), specialedCard.effectText))

		time.sleep(1)


		specialedCard.ResolveEffect(effTrigger.summon, effplayer, opponent, specialedCard, oppMon, effgy, oppgy, turnPlayer)

	# Special Summon a monster from your hand FITTING the given namespace
	def specialHandSpecific(self, name, effplayer, opponent, sentMon, oppMon, effgy, oppgy, turnPlayer):
		i = 0
		tempListNum = []
		print("{}s Hand:".format(self.name))
		del sentMon

		# Loop through the hand and display each card fitting the namespace
		while True:
			try:
				currentCard = self.hand[i]
			except IndexError:
				if self.deck.__len__() == 0:
					print("Hand is Empty")
				else:
					raise IndexError
				break

			if name in currentCard.name:
				print("[{}] {} | ATK: {} | Effect: {}".format((i + 1), currentCard.name.ljust(25, ), str(currentCard.atkPoints).ljust(4, ), currentCard.effectText))
				tempListNum.append(i)
			else:
				pass

			i = i + 1

			if i == self.hand.__len__():
				break

		if tempListNum:
			while True:
				# Get user Selection
				selection = input("~~~Select the card to SS (Type the Number):")

				try:
					selection = int(selection) - 1
				except ValueError:
					pass

				# Special Summon the Card
				if selection in tempListNum:
					specialedCard = self.hand[selection]

					self.summon(specialedCard)

					del self.hand[selection]

					print("--------------------------------------")
					print("{} has been Special Summoned".format(specialedCard.name))
					print("ATK: {} | Effect: {}".format(str(specialedCard.atkPoints), specialedCard.effectText))

					time.sleep(1)

					specialedCard.ResolveEffect(effTrigger.summon, effplayer, opponent, specialedCard, oppMon, effgy,
					                            oppgy, turnPlayer)

					return

				else:
					print("--------------------------------------")
					print("Invalid Selection")
					print("--------------------------------------")
		else:
			print("No Possible Targets")

	# Special Summon a monster from your hand EXAXTLY MATCHING the given namespace
	def specialHandExact(self, name, effplayer, opponent, sentMon, oppMon, effgy, oppgy, turnPlayer):
		i = 0
		tempListNum = []
		print("{}s Hand:".format(self.name))
		del sentMon

		max_len = self.getMaxLength(self.hand)

		# Loop through the hand and display each card fitting the namespace
		for monster in self.hand:
			if monster.name == name:
				if i >= 9:
					print("[{}] {} | ATK: {} | Tributes: {} | Effect: {}".format((i + 1), monster.name.ljust(max_len, ), str(monster.atkPoints).ljust(4, ), monster.tribute, monster.effectText))
				else:
					print("[{}]  {} | ATK: {} | Tributes: {} | Effect: {}".format((i + 1), monster.name.ljust(max_len, ), str(monster.atkPoints).ljust(4, ), monster.tribute, monster.effectText))
				tempListNum.append(i)
			else:
				pass

			i = i + 1

		if tempListNum:
			while True:
				# Get user Selection
				selection = input("~~~Select the card to Summon (Type the Number):")

				try:
					selection = int(selection) - 1
				except ValueError:
					pass

				# Special Summon the Card
				if selection in tempListNum:
					specialedCard = self.hand[selection]

					self.summon(specialedCard)

					del self.hand[selection]

					print("--------------------------------------")
					print("{} has been Special Summoned".format(specialedCard.name))
					print("ATK: {} | Effect: {}".format(str(specialedCard.atkPoints), specialedCard.effectText))

					time.sleep(1)

					specialedCard.ResolveEffect(effTrigger.summon, effplayer, opponent, specialedCard, oppMon, effgy,
					                            oppgy, turnPlayer)

					return

				else:
					print("--------------------------------------")
					print("Invalid Selection")
					print("--------------------------------------")
		else:
			print("No Possible Targets")

	# Special Summon a monster from your deck EXACTLY MATCHING the given namespace
	def specialDeckExact(self, name, effplayer, opponent, sentMon, oppMon, effgy, oppgy, turnPlayer):
		i = 0
		tempListNum = []
		print("{}s Deck:".format(self.name))
		del sentMon

		max_len = self.getMaxLength(self.deck)

		# Loop through the hand and display each card fitting the namespace
		for monster in self.deck:
			if monster.name == name:
				if i >= 9:
					print("[{}] {} | ATK: {} | Tributes: {} | Effect: {}".format((i + 1), monster.name.ljust(max_len, ), str(monster.atkPoints).ljust(4, ), monster.tribute, monster.effectText))
				else:
					print("[{}]  {} | ATK: {} | Tributes: {} | Effect: {}".format((i + 1), monster.name.ljust(max_len, ), str(monster.atkPoints).ljust(4, ), monster.tribute, monster.effectText))
				tempListNum.append(i)
			else:
				pass

			i = i + 1

		if tempListNum:
			while True:
				# Get user Selection
				selection = input("~~~Select the card to Summon (Type the Number):")

				try:
					selection = int(selection) - 1
				except ValueError:
					pass

				# Special Summon the Card
				if selection in tempListNum:
					specialedCard = self.deck[selection]

					self.summon(specialedCard)

					print("--------------------------------------")
					print("{} has been Special Summoned".format(specialedCard.name))
					print("ATK: {} | Effect: {}".format(str(specialedCard.atkPoints), specialedCard.effectText))

					time.sleep(1)

					specialedCard.ResolveEffect(effTrigger.summon, effplayer, opponent, specialedCard, oppMon, effgy,
					                            oppgy, turnPlayer)

					del self.deck[selection]

					return

				else:
					print("--------------------------------------")
					print("Invalid Selection")
					print("--------------------------------------")
		else:
			print("No Possible Targets")

	# Grand a monster on your field a designated amount of attack, not including the played card
	def grantAttack(self, attack, playedCard):

		# Checking the second array point, because if the player monster is the only monster,
		# there won't be a second monster on the field
		try:
			# Print all other monsters on the field
			i = 0
			tempListNum = []

			max_len = self.getMaxLength(self.monfield)

			for monster in self.monfield:
				if monster.name != playedCard.name:
					if i >= 9:
						print("[{}] {} | ATK: {} | Tributes: {} | Effect: {}".format((i + 1), monster.name.ljust(max_len, ), str(monster.atkPoints).ljust(4, ), monster.tribute, monster.effectText))

					else:
						print("[{}]  {} | ATK: {} | Tributes: {} | Effect: {}".format((i + 1), monster.name.ljust(max_len, ), str(monster.atkPoints).ljust(4, ), monster.tribute, monster.effectText))
					tempListNum.append(i)
				else:
					pass

				i = i + 1

			if tempListNum:
				while True:

					# Get User Selection
					target = input("~~Select a target to give attack to:")

					try:
						target = int(target) - 1
					except ValueError:
						pass

					# Buff the card the Card
					if target in tempListNum:
						buffedCard = self.monfield[target]
						break
					else:
						print("--------------------------------------")
						print("Invalid Selection")
						print("--------------------------------------")

				buffedCard.atkPoints = buffedCard.atkPoints + attack

				print("--------------------------------------")

				print("{}'s Attack has been increased by {}".format(buffedCard.name, attack))

				return
			else:
				print("No Appropriate Targets on the field")
				print("--------------------------------------")
		except (IndexError, AttributeError):
			print("No Appropriate Targets on the field")
			print("--------------------------------------")

			return

	# Special Summon a monster from the deck FITTING the namespace
	def specialDeckSpecific(self, name, effplayer, opponent, sentMon, oppMon, effgy, oppgy, turnPlayer):
		i = 0
		tempListNum = []
		print("{}s Deck:".format(self.name))
		del sentMon

		max_len = self.getMaxLength(self.deck)

		# Loop through the hand and display each card fitting the namespace
		for monster in self.deck:
			if name in monster.name:
				if i >= 9:
					print("[{}] {} | ATK: {} | Tributes: {} | Effect: {}".format((i + 1), monster.name.ljust(max_len, ), str(monster.atkPoints).ljust(4, ), monster.tribute, monster.effectText))
				else:
					print("[{}]  {} | ATK: {} | Tributes: {} | Effect: {}".format((i + 1), monster.name.ljust(max_len, ), str(monster.atkPoints).ljust(4, ), monster.tribute, monster.effectText))

				tempListNum.append(i)
			else:
				pass

			i = i + 1

		if tempListNum:
			while True:
				# Get user Selection
				selection = input("~~~Select the card to Summon (Type the Number):")

				try:
					selection = int(selection) - 1
				except ValueError:
					pass

				# Special Summon the Card
				if selection in tempListNum:
					specialedCard = self.deck[selection]

					self.summon(specialedCard)

					del self.deck[selection]

					print("--------------------------------------")
					print("{} has been Special Summoned".format(specialedCard.name))
					print("ATK: {} | Effect: {}".format(str(specialedCard.atkPoints), specialedCard.effectText))

					time.sleep(1)

					specialedCard.ResolveEffect(effTrigger.summon, effplayer, opponent, specialedCard, oppMon, effgy,
					                            oppgy, turnPlayer)

					return

				else:
					print("--------------------------------------")
					print("Invalid Selection")
					print("--------------------------------------")
		else:
			print("No Possible Targets")

	def specialDeckSpecificLessAttack(self, name, atk, effplayer, opponent, sentMon, oppMon, effgy, oppgy, turnPlayer):
		i = 0
		tempListNum = []
		print("{}s Deck:".format(self.name))
		del sentMon

		max_len = self.getMaxLength(self.deck)

		# Loop through the hand and display each card fitting the namespace
		for monster in self.deck:
			if name in monster.name and monster.atkPoints < atk:
				if i >= 9:
					print("[{}] {} | ATK: {} | Tributes: {} | Effect: {}".format((i + 1), monster.name.ljust(max_len, ), str(monster.atkPoints).ljust(4, ), monster.tribute, monster.effectText))
				else:
					print("[{}]  {} | ATK: {} | Tributes: {} | Effect: {}".format((i + 1), monster.name.ljust(max_len, ), str(monster.atkPoints).ljust(4, ), monster.tribute, monster.effectText))

				tempListNum.append(i)
			else:
				pass

			i = i + 1

		if tempListNum:
			while True:
				# Get user Selection
				selection = input("~~~Select the card to Summon (Type the Number):")

				try:
					selection = int(selection) - 1
				except ValueError:
					pass

				# Special Summon the Card
				if selection in tempListNum:
					specialedCard = self.deck[selection]

					self.summon(specialedCard)

					del self.deck[selection]

					print("--------------------------------------")
					print("{} has been Special Summoned".format(specialedCard.name))
					print("ATK: {} | Effect: {}".format(str(specialedCard.atkPoints), specialedCard.effectText))

					time.sleep(1)

					specialedCard.ResolveEffect(effTrigger.summon, effplayer, opponent, specialedCard, oppMon, effgy,
					                            oppgy, turnPlayer)

					return

				else:
					print("--------------------------------------")
					print("Invalid Selection")
					print("--------------------------------------")
		else:
			print("No Possible Targets")

	def specialGraveyardSpecific(self, effplayer, opponent, sentMon, oppMon, effgy, oppgy, turnPlayer, *names):
		i = 0
		tempListNum = []
		print("{}s GY:".format(self.name))
		del sentMon

		max_len = self.getMaxLength(self.gy)

		# Loop through the hand and display each card fitting the namespace
		for monster in self.gy:
			for name in names:
				if name in monster.name:
					if i >= 9:
						print("[{}] {} | ATK: {} | Tributes: {} | Effect: {}".format((i + 1), monster.name.ljust(max_len, ), str(monster.atkPoints).ljust(4, ), monster.tribute, monster.effectText))
					else:
						print("[{}]  {} | ATK: {} | Tributes: {} | Effect: {}".format((i + 1), monster.name.ljust(max_len, ), str(monster.atkPoints).ljust(4, ), monster.tribute, monster.effectText))

					tempListNum.append(i)
				else:
					pass
			i = i + 1

		if tempListNum:
			while True:
				# Get user Selection
				selection = input("~~~Select the card to Summon (Type the Number):")

				try:
					selection = int(selection) - 1
				except ValueError:
					pass

				# Special Summon the Card
				if selection in tempListNum:
					specialedCard = self.gy[selection]

					self.summon(specialedCard)

					del self.gy[selection]

					print("--------------------------------------")
					print("{} has been Special Summoned".format(specialedCard.name))
					print("ATK: {} | Effect: {}".format(str(specialedCard.atkPoints), specialedCard.effectText))

					time.sleep(1)

					specialedCard.ResolveEffect(effTrigger.summon, effplayer, opponent, specialedCard, oppMon, effgy,
					                            oppgy, turnPlayer)

					return

				else:
					print("--------------------------------------")
					print("Invalid Selection")
					print("--------------------------------------")
		else:
			print("No Possible Targets")


