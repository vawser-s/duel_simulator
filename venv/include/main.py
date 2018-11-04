# https://docs.python.org/3/library/enum.html <-- FOR ENUM INFO
from copy import *

from card import *
from duelist import *
from effect import *

from settings import *

# Method to setup the card database and runs player_deck_setup()
def cardSetup():

	# The card template is as follows:
	# card(Name, Atk Points, Effect Name, Effect Trigger Enum, Effect Derscription)

	# Cyber Deck
	global microCoder
	global microCoder2
	global codeGenerator
	global codeGenerator2
	global codeRadiator
	global codeRadiator2
	global ladyDebug
	global ladyDebug2
	global cyberseGadget
	global cyberseGadget2
	global cyberseAccelerator
	global cyberseAccelerator2
	global cyberseWhiteHat
	global cyberseWhiteHat2
	global cyberseClockDragon
	global cyberseClockDragon2
	global dualAssembwurm
	global dualAssembwurm2
	global segmentDriver
	global segmentDriver2
	microCoder = card("Micro Coder", 300, 0, effectCyberseSearch, effTrigger.summon, effectDescBuilder(effTrigger.summon, effectCyberseSearch.desc))
	codeGenerator = card("Code Generator", 1300, 0, effectCodeSearch, effTrigger.summon, effectDescBuilder(effTrigger.summon, effectCodeSearch.desc))
	codeRadiator = card("Code Radiator", 1600, 0, doubleSummon, effTrigger.summon, effectDescBuilder(effTrigger.summon, doubleSummon.desc))
	ladyDebug = card("Lady Debug", 1000, 0, specialCyberseHand, effTrigger.summon, effectDescBuilder(effTrigger.summon, specialCyberseHand.desc))
	cyberseGadget = card("Cyberse Gadget", 1400, 0, Destroy, effTrigger.summon, effectDescBuilder(effTrigger.summon, Destroy.desc))
	cyberseAccelerator = card("Cyberse Accelerator", 2000, 0, oppDisc1, effTrigger.summon, effectDescBuilder(effTrigger.summon, oppDisc1.desc))
	cyberseWhiteHat = card("Cyberse White Hat", 2100, 1, effectSearch, effTrigger.summon, effectDescBuilder(effTrigger.summon, effectSearch.desc))
	cyberseClockDragon = card("Cyberse Clock Dragon", 2500, 1, specialfromHand, effTrigger.destructionEff, effectDescBuilder(effTrigger.destructionEff, specialfromHand.desc))
	dualAssembwurm = card("Dual Assembwurm", 2800, 1, oppDisc2, effTrigger.battle, effectDescBuilder(effTrigger.battle, oppDisc2.desc))
	segmentDriver = card("Cyberse Driver", 2200, 1, bounceMonster, effTrigger.summon, effectDescBuilder(effTrigger.summon, bounceMonster.desc))
	microCoder2 = deepcopy(microCoder)
	codeGenerator2 = deepcopy(codeGenerator)
	codeRadiator2 = deepcopy(codeRadiator)
	ladyDebug2 = deepcopy(ladyDebug)
	cyberseGadget2 = deepcopy(cyberseGadget)
	cyberseAccelerator2 = deepcopy(cyberseAccelerator)
	cyberseWhiteHat2 = deepcopy(cyberseWhiteHat)
	cyberseClockDragon2 = deepcopy(cyberseClockDragon)
	dualAssembwurm2 = deepcopy(dualAssembwurm)
	segmentDriver2 = deepcopy(segmentDriver)

	# Vampire Deck
	global vampireFamiliar
	global vampireFamiliar2
	global vampireSucker
	global vampireSucker2
	global vampireFraulein
	global vampireFraulein2
	global vampireGrace
	global vampireGrace2
	global vampireGenesis
	global vampireGenesis2
	global mezuki
	global mezuki2
	global unizombie
	global unizombie2
	global shiranuiSolitare
	global shiranuiSolitare2
	global armageddonKnight
	global armageddonKnight2
	global zombieMaster
	global zombieMaster2
	vampireFamiliar = card("Vampire Familiar", 300, 0, effectVampSearch, effTrigger.graveyard, effectDescBuilder(effTrigger.graveyard, effectVampSearch.desc))
	vampireFamiliar2 = deepcopy(vampireFamiliar)
	vampireSucker = card("Vampire Sucker", 1600, 0, discSpecVampHand, effTrigger.summon, effectDescBuilder(effTrigger.summon, discSpecVampHand.desc))
	vampireSucker2 = deepcopy(vampireSucker)
	vampireFraulein = card("Vampire Fraulein", 800, 0, battleImmune, effTrigger.destructionBat, effectDescBuilder(effTrigger.destructionBat, battleImmune.desc))
	vampireFraulein2 = deepcopy(vampireFraulein)
	vampireGrace = card("Vampire Grace", 2200, 1, SiphonLifeAndMill800, effTrigger.summon, effectDescBuilder(effTrigger.summon, SiphonLifeAndMill800.desc))
	vampireGrace2 = deepcopy(vampireGrace)
	vampireGenesis = card("Vampire Genesis", 2800, 1, SiphonLifeAndMill1500, effTrigger.battle, effectDescBuilder(effTrigger.battle, SiphonLifeAndMill1500.desc))
	vampireGenesis2 = deepcopy(vampireGenesis)
	mezuki = card("Mezuki", 1600, 0, Destroy, effTrigger.summon, effectDescBuilder(effTrigger.summon, Destroy.desc))
	mezuki2 = deepcopy(mezuki)
	unizombie = card("Uni-Zombie", 1500, 0, GYToHand, effTrigger.summon, effectDescBuilder(effTrigger.summon, GYToHand.desc))
	unizombie2 = deepcopy(unizombie)
	shiranuiSolitare = card("Shiranui Solitare", 1300, 0, PlayerDraw1, effTrigger.graveyard, effectDescBuilder(effTrigger.graveyard, PlayerDraw1.desc))
	shiranuiSolitare2 = deepcopy(shiranuiSolitare)
	armageddonKnight = card("Armageddon Knight", 1400, 0, Mill, effTrigger.summon, effectDescBuilder(effTrigger.summon, Mill.desc))
	armageddonKnight2 = deepcopy(armageddonKnight)
	zombieMaster = card("Zombie Master", 1800, 0, oppDisc1, effTrigger.summon, effectDescBuilder(effTrigger.summon, oppDisc1.desc))
	zombieMaster2 = deepcopy(zombieMaster)

	# Gishki Deck
	global gishkiBeast
	global gishkiBeast2
	global gishkiAbyss
	global gishkiAbyss2
	global gishkiAquamirror
	global gishkiAquamirror2
	global gishkiShadow
	global gishkiShadow2
	global visionGishki
	global visionGishki2
	global gishkiAriel
	global gishkiAriel2
	global evigishkiLevianima
	global evigishkiLevianima2
	global evigishkiSoulOgre
	global evigishkiSoulOgre2
	global evigishkiGustKraken
	global evigishkiGustKraken2
	global evigishkiPsychlone
	global evigishkiPsychlone2
	gishkiBeast = card("Gishki Beast", 1500, 0, gain500, effTrigger.battle, effectDescBuilder(effTrigger.battle, gain500.desc))
	gishkiBeast2 = deepcopy(gishkiBeast)
	gishkiAbyss = card("Gishki Abyss", 800, 0, PlayerDraw2, effTrigger.battle, effectDescBuilder(effTrigger.battle, PlayerDraw2.desc))
	gishkiAbyss2 = deepcopy(gishkiAbyss)
	gishkiAquamirror = card("Gishki Aquamirror", 0, 0, doubleSummon, effTrigger.summon, effectDescBuilder(effTrigger.summon, doubleSummon.desc))
	gishkiAquamirror2 = deepcopy(gishkiAquamirror)
	gishkiShadow = card("Gishki Shadow", 1200, 0, battleImmune, effTrigger.destructionBat, effectDescBuilder(effTrigger.destructionBat, battleImmune.desc))
	gishkiShadow2 = deepcopy(gishkiShadow)
	visionGishki = card("Vision Gishki ", 1800, 0, effectGishkiSearch, effTrigger.battle, effectDescBuilder(effTrigger.battle, effectGishkiSearch.desc))
	visionGishki2 = deepcopy(visionGishki)
	gishkiAriel = card("Gishki Ariel", 1200, 0, bounceMonster, effTrigger.summon, effectDescBuilder(effTrigger.summon, bounceMonster.desc))
	gishkiAriel2 = deepcopy(gishkiAriel)
	evigishkiLevianima = card("Evigishki Levianima", 2200, 1, effectGishkiSearch, effTrigger.summon, effectDescBuilder(effTrigger.summon, effectGishkiSearch.desc))
	evigishkiLevianima2 = deepcopy(evigishkiLevianima)
	evigishkiSoulOgre = card("Evigishki Soul Ogre", 2800, 1, gain1000, effTrigger.battle, effectDescBuilder(effTrigger.battle, gain1000.desc))
	evigishkiSoulOgre2 = deepcopy(evigishkiSoulOgre)
	evigishkiGustKraken = card("Evigishki Gustkraken", 2500, 1, specialGishkiHand, effTrigger.battle, effectDescBuilder(effTrigger.battle, specialGishkiHand.desc))
	evigishkiGustKraken2 = deepcopy(evigishkiGustKraken)
	evigishkiPsychlone = card("Evigishki Psychlone", 2000, 1, Destroy, effTrigger.battle, effectDescBuilder(effTrigger.battle, Destroy.desc))
	evigishkiPsychlone2 = deepcopy(evigishkiPsychlone)

	# Herald Deck
	global orangeHerald
	global orangeHerald2
	global purpleHerald
	global purpleHerald2
	global arcHerald
	global arcHerald2
	global dawnHerald
	global dawnHerald2
	global agentEarth
	global agentEarth2
	global agentVenus
	global agentVenus2
	global agentMars
	global agentMars2
	global agentSaturn
	global agentSaturn2
	global heraldPerfection
	global heraldPerfection2
	global masterHyperion
	global masterHyperion2
	orangeHerald = card("Herald of Orange Light", 1000, 0, effectHeraldSearch, effTrigger.summon, effectDescBuilder(effTrigger.summon, effectHeraldSearch.desc))
	orangeHerald2 = deepcopy(orangeHerald)
	purpleHerald = card("Herald of Purple Light", 800, 0, matchAttack, effTrigger.battle, effectDescBuilder(effTrigger.battle, matchAttack.desc))
	purpleHerald2 = deepcopy(purpleHerald)
	arcHerald = card("Herald of Arc Light", 1800, 0, Restore2000, effTrigger.summon, effectDescBuilder(effTrigger.summon, Restore2000.desc))
	arcHerald2 = deepcopy(arcHerald)
	dawnHerald = card("Herald of the Dawn", 0, 0, doubleSummon, effTrigger.summon, effectDescBuilder(effTrigger.summon, doubleSummon.desc))
	dawnHerald2 = deepcopy(dawnHerald)
	agentEarth = card("Agent of Mystery: Earth", 1200, 0, effectAgentSearch, effTrigger.summon, effectDescBuilder(effTrigger.summon, effectAgentSearch.desc))
	agentEarth2 = deepcopy(agentEarth)
	agentVenus = card("Agent of Creation: Venus", 1600, 0, specialAgentHand, effTrigger.summon, effectDescBuilder(effTrigger.summon, specialAgentHand.desc))
	agentVenus2 = deepcopy(agentVenus)
	agentMars = card("Agent of Force: Mars", 0, 0, gainDifference, effTrigger.summon, effectDescBuilder(effTrigger.summon, gainDifference.desc))
	agentMars2 = deepcopy(agentMars)
	agentSaturn = card("Agent of Judgment: Saturn", 2400, 1, RestoreLPForHand1000, effTrigger.summon, effectDescBuilder(effTrigger.summon, RestoreLPForHand1000.desc))
	agentSaturn2 = deepcopy(agentSaturn)
	heraldPerfection = card("Herald of Perfection", 2800, 1, gainDifference, effTrigger.summon, effectDescBuilder(effTrigger.summon, gainDifference.desc))
	heraldPerfection2 = deepcopy(heraldPerfection)
	masterHyperion = card("Master Hyperion", 2800, 1, specialfromHand, effTrigger.summon, effectDescBuilder(effTrigger.summon, specialfromHand.desc))
	masterHyperion2 = deepcopy(masterHyperion)

	global darkMagician
	global darkMagician2
	global darkGMagician
	global darkGMagician2
	global magicianRod
	global magicianRod2
	global magicianRobe
	global magicianRobe2
	global chocolateGirl
	global chocolateGirl2
	global appleGirl
	global appleGirl2
	global kiwiGirl
	global kiwiGirl2
	global berryGirl
	global berryGirl2
	global ebonIllusion
	global ebonIllusion2
	global magiMagiGirl
	global magiMagiGirl2
	darkMagician = card("Dark Magician", 2500, 1, effectImmune, effTrigger.destructionEff, effectDescBuilder(effTrigger.destructionEff, effectImmune.desc))
	darkMagician2 = deepcopy(darkMagician)
	darkGMagician = card("Dark Magician Girl", 2300, 1, darkMagicianGain500, effTrigger.summon, effectDescBuilder(effTrigger.summon, darkMagicianGain500.desc))
	darkGMagician2 = deepcopy(darkGMagician)
	magicianRod = card("Magician's Rod", 1600, 0, effectDarkMagicianSearch, effTrigger.summon, effectDescBuilder(effTrigger.summon, effectDarkMagicianSearch.desc))
	magicianRod2 = deepcopy(magicianRod)
	magicianRobe = card("Magician's Robe", 800, 0, doubleSummon, effTrigger.summon, effectDescBuilder(effTrigger.summon, doubleSummon.desc))
	magicianRobe2 = deepcopy(magicianRobe)
	chocolateGirl = card("Chocolate Magician Girl", 1800, 0, specialMagicianGirlHand, effTrigger.summon, effectDescBuilder(effTrigger.summon, specialMagicianGirlHand.desc))
	chocolateGirl2 = deepcopy(chocolateGirl)
	appleGirl = card("Apple Magician Girl", 1000, 0, halfAtkDraw2, effTrigger.defend, effectDescBuilder(effTrigger.defend, halfAtkDraw2.desc))
	appleGirl2 = deepcopy(appleGirl)
	berryGirl = card("Berry Magician Girl", 1200, 0, tribtoGrantAtk, effTrigger.summon, effectDescBuilder(effTrigger.summon, tribtoGrantAtk.desc))
	berryGirl2 = deepcopy(berryGirl)
	kiwiGirl = card("Kiwi Magician Girl", 300, 0, bounceMonster, effTrigger.summon, effectDescBuilder(effTrigger.summon, bounceMonster.desc))
	kiwiGirl2 = deepcopy(kiwiGirl)
	ebonIllusion = card("Ebon Illusion Magician", 2400, 1, specialDarkMagicianDeck, effTrigger.summon, effectDescBuilder(effTrigger.summon, specialDarkMagicianDeck.desc))
	ebonIllusion2 = deepcopy(ebonIllusion)
	magiMagiGirl = card("Magi Magician Girl", 2600, 1, Atk0, effTrigger.defend, effectDescBuilder(effTrigger.defend, Atk0.desc))
	magiMagiGirl2 = deepcopy(magiMagiGirl)

	global stormRiderAllyson
	global stormRiderAllyson2
	global stormBirdZephris
	global stormBirdZephris2
	global stormRiderHellion
	global stormRiderHellion2
	global stormBirdHellDiver
	global stormBirdHellDiver2
	global stormRiderCanto
	global stormRiderCanto2
	global stormBirdSkylar
	global stormBirdSkylar2
	global stormRiderNess
	global stormRiderNess2
	global stormBirdGale
	global stormBirdGale2
	global stormBringerAlizeh
	global stormBringerAlizeh2
	global stormGodMonsoon
	global stormGodMonsoon2
	stormRiderAllyson = card("Allyson: Stormrider", 800, 0, specialStormBirdHand, effTrigger.summon, effectDescBuilder(effTrigger.summon, specialStormBirdHand.desc))
	stormRiderAllyson2 = deepcopy(stormRiderAllyson)
	stormRiderHellion = card("Hellion: Stormrider", 900, 0, specialStormRiderDeck, effTrigger.summon, effectDescBuilder(effTrigger.summon, specialStormRiderDeck.desc))
	stormRiderHellion2 = deepcopy(stormRiderHellion)
	stormRiderCanto = card("Canto: Stormrider", 500, 0, doubleSummon, effTrigger.summon, effectDescBuilder(effTrigger.summon, doubleSummon.desc))
	stormRiderCanto2 = deepcopy(stormRiderCanto)
	stormRiderNess = card("Ness: Stormrider", 750, 0, discSpecStormGY, effTrigger.summon, effectDescBuilder(effTrigger.summon, discSpecStormGY.desc))
	stormRiderNess2 = deepcopy(stormRiderNess)
	stormBirdZephris = card("Zephris: Stormbird", 1600, 0, controlStormriderDraw2, effTrigger.summon, effectDescBuilder(effTrigger.summon, controlStormriderDraw2.desc))
	stormBirdZephris2 = deepcopy(stormBirdZephris)
	stormBirdHellDiver = card("Hell Diver: Stormbird", 1800, 0, controlStormriderDestroy, effTrigger.summon, effectDescBuilder(effTrigger.summon, controlStormriderDestroy.desc))
	stormBirdHellDiver2 = deepcopy(stormBirdHellDiver)
	stormBirdSkylar = card("Skylar: Stormbird", 1000, 0, grantStormriderAttack, effTrigger.summon, effectDescBuilder(effTrigger.summon, grantStormriderAttack.desc))
	stormBirdSkylar2 = deepcopy(stormBirdSkylar)
	stormBirdGale = card("Gale: Stormbird", 1500, 0, tribToSpecialStormBird, effTrigger.summon, effectDescBuilder(effTrigger.summon, tribToSpecialStormBird.desc))
	stormBirdGale2 = deepcopy(stormBirdGale)
	stormBringerAlizeh = card("Alizeh: Stormbringer", 2500, 1, StormriderStealMonster, effTrigger.summon, effectDescBuilder(effTrigger.summon, StormriderStealMonster.desc))
	stormBringerAlizeh2 = deepcopy(stormBringerAlizeh)
	stormGodMonsoon = card("Monsoon: Stormgod", 3000, 1, tributeStormtoSteal, effTrigger.summon, effectDescBuilder(effTrigger.summon, tributeStormtoSteal.desc))
	stormGodMonsoon2 = deepcopy(stormGodMonsoon)

	# TEST CARDS

	global copyMachine
	copyMachine = card("Copy Machine", 0, 0, matchAttack, effTrigger.battle, matchAttack.desc)

	global discard1Guy
	global deviousDiscard1Guy
	global deviousDiscardDiva
	global battleImmuneIvan
	global effectImmuneEdgar
	global cyberDigger
	global deckDigger
	global doubleSummoner
	global resurrector
	global reAdder
	global graveyardGarry
	global lifeVitalizer
	global defenderDan
	global gameEnder1
	global gameEnder2
	discard1Guy = card("Discard Guy", 500, 0, playerDisc1, effTrigger.summon, playerDisc1.desc)
	deviousDiscard1Guy = card("Devious Discard Guy", 0, 0, oppDisc1, effTrigger.summon, oppDisc1.desc)
	deviousDiscardDiva = card("Devious Discard Diva", 2500, 0, playerDisc1, effTrigger.battle, playerDisc1.desc)
	battleImmuneIvan = card("Battle Immune Ivan", 0, 0, battleImmune, effTrigger.destructionBat, battleImmune.desc)
	effectImmuneEdgar = card("Effect Immune Edgar", 1500, 0, effectImmune, effTrigger.destructionEff, effectImmune.desc)
	cyberDigger = card("Cyber Digger", 1000, 0, effectCodeSearch, effTrigger.summon, effectCodeSearch.desc)
	deckDigger = card("Deck Digger", 200, 0, effectSearch, effTrigger.summon, effectSearch.desc)
	doubleSummoner = card("Double Summoner", 1500, 0, doubleSummon, effTrigger.summon, doubleSummon.desc)
	resurrector = card("Resurrector", 0, 0, Trib_SS_GY, effTrigger.summon, Trib_SS_GY.desc)
	reAdder = card("Re-Adder", 1200, 0, GYToHand, effTrigger.summon, GYToHand.desc)
	graveyardGarry = card("Graveyard Garry", 2000, 1, PlayerDraw2, effTrigger.graveyard, PlayerDraw2.desc)
	lifeVitalizer = card("Life Vitalizer", 1800, 0, gainDifference, effTrigger.summon, gainDifference.desc)
	defenderDan = card("Defender Dan", 2000, 0, PlayerDraw1, effTrigger.defend, effectDescBuilder(effTrigger.defend, PlayerDraw1.desc))
	gameEnder1 = card("Game Ender EFF", 0, 0, Damage8000, effTrigger.summon, effectDescBuilder(effTrigger.summon, Damage8000.desc))
	gameEnder2 = card("Game Ender BTL", 0, 0, Damage8000, effTrigger.battle, effectDescBuilder(effTrigger.battle, Damage8000.desc))

# Method to build the asppropriate effect descriptions for cards
def effectDescBuilder(trigger: Enum, Desc: str):

	if trigger.name == "n_a":
		effectDescription = Desc
	elif trigger.name == "summon":
		effectDescription = "When Summoned: " + Desc
	elif trigger.name == "attack":
		effectDescription = "When this card Attacks: " + Desc
	elif trigger.name == "defend":
		effectDescription = "When this card is Attacked: " + Desc
	elif trigger.name == "battle":
		effectDescription = "When this card Battles: " + Desc
	elif trigger.name == "graveyard":
		effectDescription = "When this card is sent to the Graveyard: " + Desc
	elif trigger.name == "destructionBat":
		effectDescription = "When this card would be destroyed by Battle: " + Desc
	elif trigger.name == "destructionEff":
		effectDescription = "When this card would be destroyed by a card effect: " + Desc
	else:
		raise TypeError

	return "Once per turn, " + effectDescription

# Prints Deck List before they are assigned to a player
def printDeckList(DeckList: list):
	print("Deck List:")

	if DeckList.__len__() != 0:
		i = 0

		max_len = _player.getMaxLength(DeckList)

		for monster in DeckList:
			if i >= 9:
				print("[{}] {} | ATK: {} | Tributes: {} | Effect: {}".format((i + 1), monster.name.ljust(max_len, ),
																			 str(monster.atkPoints).ljust(4, ),
																			 monster.tribute, monster.effectText))
			else:
				print("[{}]  {} | ATK: {} | Tributes: {} | Effect: {}".format((i + 1), monster.name.ljust(max_len, ),
																			  str(monster.atkPoints).ljust(4, ),
																			  monster.tribute, monster.effectText))
			i = i + 1

	input("Press Enter to Continue...")

	return

# Finds the max length of the words in a list of dictionaries (Menu Formatting)
def findDictLength(dictionaryList: list, index: str):
	max_len = ""

	# Find the Longest list element
	for item in dictionaryList:
		if len(max_len) < len(item[index]):
			max_len = item[index]
		else:
			pass

	return len(max_len)

# Method to setup decks once the cards have been set
def player_deck_setup():
	CyberDeck = []
	VampireDeck = []
	GishkiDeck = []
	HeraldDeck = []
	MagicianDeck = []
	StormDeck = []

	PlayerList = []

	pass

	CyberDeck.append(microCoder)
	CyberDeck.append(microCoder2)
	CyberDeck.append(codeGenerator)
	CyberDeck.append(codeGenerator2)
	CyberDeck.append(codeRadiator)
	CyberDeck.append(codeRadiator2)
	CyberDeck.append(ladyDebug)
	CyberDeck.append(ladyDebug2)
	CyberDeck.append(cyberseGadget)
	CyberDeck.append(cyberseGadget2)
	CyberDeck.append(cyberseAccelerator)
	CyberDeck.append(cyberseAccelerator2)
	CyberDeck.append(cyberseWhiteHat)
	CyberDeck.append(cyberseWhiteHat2)
	CyberDeck.append(cyberseClockDragon)
	CyberDeck.append(cyberseClockDragon2)
	CyberDeck.append(dualAssembwurm)
	CyberDeck.append(segmentDriver)
	CyberDeck.append(segmentDriver2)

	VampireDeck.append(vampireFamiliar)
	VampireDeck.append(vampireFamiliar2)
	VampireDeck.append(vampireSucker)
	VampireDeck.append(vampireSucker2)
	VampireDeck.append(vampireFraulein)
	VampireDeck.append(vampireFraulein2)
	VampireDeck.append(vampireGrace)
	VampireDeck.append(vampireGrace2)
	VampireDeck.append(vampireGenesis)
	VampireDeck.append(mezuki)
	VampireDeck.append(mezuki2)
	VampireDeck.append(unizombie)
	VampireDeck.append(unizombie2)
	VampireDeck.append(shiranuiSolitare)
	VampireDeck.append(shiranuiSolitare2)
	VampireDeck.append(armageddonKnight)
	VampireDeck.append(armageddonKnight2)
	VampireDeck.append(zombieMaster)
	VampireDeck.append(zombieMaster2)

	GishkiDeck.append(gishkiBeast)
	GishkiDeck.append(gishkiBeast2)
	GishkiDeck.append(gishkiAbyss)
	GishkiDeck.append(gishkiAbyss2)
	GishkiDeck.append(gishkiAquamirror)
	GishkiDeck.append(gishkiAquamirror2)
	GishkiDeck.append(gishkiShadow)
	GishkiDeck.append(gishkiShadow2)
	GishkiDeck.append(visionGishki)
	GishkiDeck.append(visionGishki2)
	GishkiDeck.append(gishkiAriel)
	GishkiDeck.append(gishkiAriel2)
	GishkiDeck.append(evigishkiLevianima)
	GishkiDeck.append(evigishkiLevianima2)
	GishkiDeck.append(evigishkiSoulOgre)
	GishkiDeck.append(evigishkiGustKraken)
	GishkiDeck.append(evigishkiGustKraken)
	GishkiDeck.append(evigishkiPsychlone)
	GishkiDeck.append(evigishkiPsychlone2)

	HeraldDeck.append(orangeHerald)
	HeraldDeck.append(orangeHerald2)
	HeraldDeck.append(purpleHerald)
	HeraldDeck.append(purpleHerald2)
	HeraldDeck.append(arcHerald)
	HeraldDeck.append(arcHerald2)
	HeraldDeck.append(dawnHerald)
	HeraldDeck.append(dawnHerald2)
	HeraldDeck.append(agentEarth)
	HeraldDeck.append(agentEarth2)
	HeraldDeck.append(agentVenus)
	HeraldDeck.append(agentVenus2)
	HeraldDeck.append(agentMars)
	HeraldDeck.append(agentMars2)
	HeraldDeck.append(agentSaturn)
	HeraldDeck.append(agentSaturn2)
	HeraldDeck.append(heraldPerfection)
	HeraldDeck.append(masterHyperion)
	HeraldDeck.append(masterHyperion)

	MagicianDeck.append(darkMagician)
	MagicianDeck.append(darkMagician2)
	MagicianDeck.append(darkGMagician)
	MagicianDeck.append(darkGMagician2)
	MagicianDeck.append(magicianRod)
	MagicianDeck.append(magicianRod2)
	MagicianDeck.append(magicianRobe)
	MagicianDeck.append(magicianRobe2)
	MagicianDeck.append(chocolateGirl)
	MagicianDeck.append(chocolateGirl2)
	MagicianDeck.append(appleGirl)
	MagicianDeck.append(appleGirl2)
	MagicianDeck.append(berryGirl)
	MagicianDeck.append(berryGirl2)
	MagicianDeck.append(kiwiGirl)
	MagicianDeck.append(kiwiGirl2)
	MagicianDeck.append(ebonIllusion)
	MagicianDeck.append(ebonIllusion2)
	MagicianDeck.append(magiMagiGirl)
	MagicianDeck.append(magiMagiGirl2)

	StormDeck.append(stormRiderAllyson)
	StormDeck.append(stormRiderAllyson2)
	StormDeck.append(stormRiderHellion)
	StormDeck.append(stormRiderHellion2)
	StormDeck.append(stormRiderCanto)
	StormDeck.append(stormRiderCanto2)
	StormDeck.append(stormRiderNess)
	StormDeck.append(stormRiderNess2)
	StormDeck.append(stormBirdZephris)
	StormDeck.append(stormBirdZephris2)
	StormDeck.append(stormBirdHellDiver)
	StormDeck.append(stormBirdHellDiver2)
	StormDeck.append(stormBirdSkylar)
	StormDeck.append(stormBirdSkylar2)
	StormDeck.append(stormBirdGale)
	StormDeck.append(stormBirdGale2)
	StormDeck.append(stormBringerAlizeh)
	StormDeck.append(stormBringerAlizeh2)
	StormDeck.append(stormGodMonsoon)

	random.shuffle(CyberDeck)
	random.shuffle(VampireDeck)
	random.shuffle(GishkiDeck)
	random.shuffle(HeraldDeck)
	random.shuffle(MagicianDeck)
	random.shuffle(StormDeck)

	for monster in CyberDeck:
		monster.attacked = 0

	for monster in VampireDeck:
		monster.attacked = 0

	for monster in GishkiDeck:
		monster.attacked = 0

	for monster in HeraldDeck:
		monster.attacked = 0

	for monster in MagicianDeck:
		monster.attacked = 0

	for monster in StormDeck:
		monster.attacked = 0

	CyberPlayer = {
		"name": "Playmaker",
		"desc": "A tech-savvy kid, who knows his way around a computer. Plays to undermine his opponents strategy from the roots",
		"deck": CyberDeck,
		"deckName": "Cyberse",
		"deckDesc": "Discarding / SS Hand",
		"voicelines": []
	}

	VampirePlayer = {
		"name": "Count Klaric",
		"desc": "A skilled player with an obsession with vampire mythology. Focuses on sacrificing her own cards to drain his opponents' life dry",
		"deck": VampireDeck,
		"deckName": "Vampire",
		"deckDesc": "Stealing Life / Graveyard Effects",
		"voicelines": []
	}

	GishkiPlayer = {
		"name": "Gishki Avance",
		"desc": "A distant traveler who has seen all walks of life. His deck mercilessely attacks his opponent, growing stronger each battle",
		"deck": GishkiDeck,
		"deckName": "Gishki",
		"deckDesc": "Attack Boosts / Battling",
		"voicelines": []
	}

	HeraldPlayer = {
		"name": "Arch Priest Xero",
		"desc": "A high ranking official within a church he is devoted to. His deck aims to  restore his own life and gain power as he does so",
		"deck": HeraldDeck,
		"deckName": "Herald Agents",
		"deckDesc": "Life Point Gain / Special Summon From Hand",
		"voicelines": []
	}

	MagicianPlayer = {
		"name": "Dennis",
		"desc": "A sidewalk performer with a nack of delivering a spectacle. his deck focuses on defending himself until his best magician is ready",
		"deck": MagicianDeck,
		"deckName": "Magicians",
		"deckDesc": "Defending / Summoning Dark Magician",
		"voicelines": []

	}

	StormPlayer = {
		"name": "Ventus",
		"desc": "A professional Speed Duelist who like to ride the wind on his hoverboard. His deck focuses on swarming Riders which power up his Stormbirds",
		"deck": StormDeck,
		"deckName": "Stormriders",
		"deckDesc": "Swarming / Stealing Monsters",
		"voicelines": []
	}

	PlayerList.append(CyberPlayer)
	PlayerList.append(VampirePlayer)
	PlayerList.append(GishkiPlayer)
	PlayerList.append(HeraldPlayer)
	PlayerList.append(MagicianPlayer)
	PlayerList.append(StormPlayer)

	# Get the user's chosen Player
	while True:

		print("--------------------------------------")
		print("Player Select:")

		maxPlayerName = findDictLength(PlayerList, "name")
		maxDeckName = findDictLength(PlayerList, "deckName")

		maxDeckDesc = findDictLength(PlayerList, "deckDesc")

		i = 0
		for player in PlayerList:
			print("[{}] Name: {} | Deck: {} | Theme: {}".format(i + 1, player.get("name").ljust(maxPlayerName, ),  player.get("deckName").ljust(maxDeckName, ), player.get("deckDesc").ljust(maxDeckDesc, )))
			i = i + 1

		selection = input("~~Please Select a character:")

		try:
			selection = int(selection) - 1

			_player.name = PlayerList[selection].get("name")
			_player.deck = PlayerList[selection].get("deck")

			print("--------------------------------------")
			print("You have selected {} as your player character".format(_player.name))

			while True:
				print("--------------------------------------")
				print("[1] Duel")
				print("[2] View Deck List")
				print("[0] Return")

				selection = input("~~Select an option:")
				try:
					selection = int(selection)

					if selection == 1:
						# Remove the players deck from the possible list
						i = 0
						for player in PlayerList:
							if player.get("deck") == _player.deck:
								PlayerList.pop(i)
							i = i + 1
						break
					elif selection == 2:
						printDeckList(_player.deck)
						pass
					elif selection == 0:
						_player.name = ""
						_player.deck = []
						break
				except ValueError:
					print("--------------------------------------")
					print("Invalid Selection")

			if _player.name and _player.deck:
				break

		except (ValueError, TypeError, AttributeError, IndexError):
			print("--------------------------------------")
			print("Invalid Selection")

	print("\n" * 50)

	# Get the user's chosen Opponent
	while True:
		print("--------------------------------------")
		print("Opponent Select:")

		maxPlayerName = findDictLength(PlayerList, "name")
		maxDeckName = findDictLength(PlayerList, "deckName")

		maxDeckDesc = findDictLength(PlayerList, "deckDesc")

		i = 0
		for opponent in PlayerList:
			print("[{}] Name: {} | Deck: {} | Theme: {}".format(i + 1, opponent.get("name").ljust(maxPlayerName, ), opponent.get("deckName").ljust(maxDeckName, ), opponent.get("deckDesc").ljust(maxDeckDesc, )))
			i = i + 1

		selection = input("~~Please Select a character to play against:")

		try:
			selection = int(selection) - 1

			_foe.name = PlayerList[selection].get("name")
			_foe.deck = PlayerList[selection].get("deck")

			print("--------------------------------------")
			print("You have selected {} as your oposition character".format(_foe.name))

			print("--------------------------------------")
			selection = input("Confirm Selection (Y/N): ")

			if selection == "Y" or selection == "y":
				break

			elif selection == "N" or selection == "n":
				pass

		except (ValueError, TypeError, AttributeError, IndexError):
			print("--------------------------------------")
			print("Invalid Selection")

	print("--------------------------------------")

	time.sleep(0.5)

	print("\n" * 50)

# Reset Gamestate
def reset():

	print("Resetting Gamestate: ")
	_player.monfield = []
	_foe.monfield = []

	_player.hand = []
	_foe.hand = []

	_player.lifepoints = 8000
	_foe.lifepoints = 8000

	global turnCount
	turnCount = 0

	global firstTurn
	firstTurn = 0

	resetNormalSummon()

	print("\n" * 50)

	pass

# Method to contain the main menu and all its options
def mainMenu():

	# Loop through menu always, program should system.exit() before this gets broken
	while True:

		# Print menu options
		print("---------- Welcome to Duels ----------")

		print("[1] Play a Duel")

		print("[2] Exit")

		print("[3] Debug")

		# get the selection, and open the appropriate submenu
		try:
			selection = input("~~~Please select a menu option")
			selection = int(selection)
			if selection == 1:
				i = 0

				cardSetup()

				player_deck_setup()

				print("--------------------------------------")
				print("Duel Begin")
				time.sleep(1)

				# -- Main loop from which the duels run --
				while True:
					if i == 1:
						exitProg = turnMenu(_foe, _player)
						i = 0
					elif i == 0:
						exitProg = turnMenu(_player, _foe)
						i = 1
					else:
						print("Duel Machine Broke: Turn Error")
						exitProg = None

					if exitProg == "true":
						break
					elif exitProg == "false":
						pass
					else:
						print("exitProg error")
						pass

			elif selection == 2:
				# Ends program with no errors
				sys.exit(0)

			elif selection == 3:
				# Sets yup debug mode and allows python console input by returning
				print("--------------------------------------")
				print("Debug Mode Enabled")

				cardSetup()

				player_deck_setup()

				TestDeck = [discard1Guy, deviousDiscard1Guy, battleImmuneIvan, cyberDigger, deckDigger, doubleSummoner, resurrector, reAdder, graveyardGarry]

				_player.hand.append(discard1Guy)
				_player.hand.append(deviousDiscard1Guy)
				_player.hand.append(battleImmuneIvan)
				_player.hand.append(cyberDigger)
				_player.hand.append(deckDigger)
				_player.hand.append(doubleSummoner)
				_player.hand.append(resurrector)
				_player.hand.append(reAdder)
				_player.hand.append(graveyardGarry)

				_foe.hand.append(deviousDiscard1Guy)
				_foe.hand.append(battleImmuneIvan)

				_player.gy.append(discard1Guy)
				_player.gy.append(deviousDiscard1Guy)
				_player.gy.append(battleImmuneIvan)
				_player.gy.append(cyberDigger)
				_player.gy.append(deckDigger)
				_player.gy.append(doubleSummoner)
				_player.gy.append(resurrector)
				_player.gy.append(reAdder)
				_player.gy.append(graveyardGarry)

				_player.deck = TestDeck
				_foe.deck = TestDeck

				return
			else:
				# Return Error
				print("--------------------------------------")
				print("Invalid Selection")
		except ValueError:
			# Return error
			print("--------------------------------------")
			print("Invalid Selection")

# Menu that contains a players turn menus
def turnMenu(currentPlayer: duelist, passivePlayer: duelist):


	# resetting attacked values on Field
	try:
		for monster in currentPlayer.monfield:
			monster.attacked = 0
	except IndexError:
		pass
	try:
		for monster in passivePlayer.monfield:
			monster.attacked = 0
	except IndexError:
		pass

	# resetting attacked values in graveyard

	try:
		for monster in currentPlayer.gy:
			monster.attacked = 0
	except IndexError:
		pass

	try:
		for monster in passivePlayer.gy:
			monster.attacked = 0
	except IndexError:
		pass

	# Retrieve the global variables and set up rest of needed variables
	global turnCount
	global firstTurn
	global destination
	destination = ""

	effectCheck = 0

	resetNormalSummon()

	resetEffectChecker()

	# Move the turn count and announce the turn
	turnCount = turnCount + 1
	print("--------------------------------------")
	print("Turn {}: {}'s Turn".format(turnCount, currentPlayer.name))

	time.sleep(0.7)

	# Checks for first turn

	# DRAW PHASE
	if firstTurn == 0:
		_player.draw(5)

		# -------------vv-Add Cards here to Test-vv---------------------------------------------------------------------
		# -------------vv-Add Cards here to Test-vv---------------------------------------------------------------------
		# -------------vv-Add Cards here to Test-vv---------------------------------------------------------------------
		# -------------vv-Add Cards here to Test-vv---------------------------------------------------------------------
		# _player.hand.append()
		# _foe.hand.append()
		# -------------^^-Add Cards here to Test-^^---------------------------------------------------------------------
		# -------------^^-Add Cards here to Test-^^---------------------------------------------------------------------
		# -------------^^-Add Cards here to Test-^^---------------------------------------------------------------------
		# -------------^^-Add Cards here to Test-^^---------------------------------------------------------------------

		_foe.draw(4)

	else:
		currentPlayer.draw(1)

	# Print current field status
	print("--------------------------------------")
	currentPlayer.checkField()

	# MAIN PHASE
	while True:

		while True:
			if currentPlayer.lifepoints == 0 or passivePlayer.lifepoints == 0:
				selection = 8
				break

			print("--------------------------------------")
			print("[1] Play a Card")

			print("[2] Check your Hand")

			print("[3] Check your Field")

			print("[4] Check your Graveyard")

			print("[5] Check Player Life Points and Deck")

			print("[6] Go to Battle Phase (Ends turn after)")

			print("[7] End your Turn")

			print("[8] Return to Main Menu")

			# get user selection
			try:
				selection = input("~~~Select an Action")
				selection = int(selection)
				print("--------------------------------------")
				break
			except ValueError:
				print("--------------------------------------")
				print("Invalid Selection")

		# applies applicable action to selection
		if selection == 1:  # [1] Play a Card

			nSummon = int(returnNormalSummon())

			if nSummon == 0:
				effectCheck = 0

			# Play the card, and return whether a card was actually played (can just return)
			result = currentPlayer.playCard()

			length = currentPlayer.monfield.__len__()

			# checks if the user returned ®or actually played a card
			if result == 0:
				pass
			else:
				playedCard = currentPlayer.monfield[length - 1]

				if playedCard.tribute == 1:
					tributedCard = currentPlayer.gy[-1]

					if tributedCard.trigger.name == "graveyard":
						monster = tributedCard
						if currentPlayer == _player:
							passivePlayer = _foe
						else:
							passivePlayer = _player

						try:
							oppmonster = None
							monster.effect.resolve(currentPlayer, passivePlayer, monster,
							                       oppmonster, currentPlayer.gy, passivePlayer.gy, currentPlayer)
							effectCheck = 1
						except IndexError:
							oppmonster = None
							monster.effect.resolve(currentPlayer, passivePlayer, monster,
							                       oppmonster, currentPlayer.gy, passivePlayer.gy, currentPlayer)
							effectCheck = 1

				# Check if the monster has an on-summon effect effect, and activate it if it hasn't used it yet
				if effectCheck == 0:
					try:
						if playedCard.trigger.name == "summon" and returnEffectChecker(playedCard):
							monster = playedCard
							if currentPlayer == _player:
								passivePlayer = _foe
							else:
								passivePlayer = _player

							try:
								oppmonster = None
								monster.effect.resolve(currentPlayer, passivePlayer, monster,
													   oppmonster, currentPlayer.gy, passivePlayer.gy, currentPlayer)
								effectCheck = 1
							except IndexError:
								oppmonster = None
								monster.effect.resolve(currentPlayer, passivePlayer, monster,
													   oppmonster, currentPlayer.gy, passivePlayer.gy, currentPlayer)
								effectCheck = 1
					# except AttributeError:
						# effectCheck = 1
						# pass
					except IndexError:
						pass

				else:
					pass

		elif selection == 2:  # [2] Check Hand
			currentPlayer.checkHand()
			pass

		elif selection == 3:  # [3] Check Field
			print("{}'s Field:".format(_player.name))
			currentPlayer.checkField()
			print("{}'s Field:".format(_foe.name))
			passivePlayer.checkField()

		elif selection == 4:  # [4] Check your Graveyard
			currentPlayer.checkGraveyard()
			passivePlayer.checkGraveyard()

		elif selection == 5:  # [5] Check Life Points and Deck Size
			currentPlayer.checkLP_Deck()
			passivePlayer.checkLP_Deck()

		# Destinations
		elif selection == 6 and firstTurn == 1:  # [6] Battle Phase
			destination = "battle"
			if currentPlayer.name == _player.name:
				exitBattle = battleMenu(_player, _foe)

				if exitBattle == 1:
					pass
				elif exitBattle == 0:
					break
			elif currentPlayer.name == _foe.name:
				exitBattle = battleMenu(_foe, _player)

				if exitBattle == 1:
					pass
				elif exitBattle == 0:
					break

		elif selection == 6 and firstTurn == 0:  # [6] Battle Phase
			print("Cannot attack on first turn")
			pass

		elif selection == 7:  # [7] End Turn
			destination = "end"
			break

		elif selection == 8:  # [8] Return to Main Menu
			destination = "menu"
			break

		else:
			print("--------------------------------------")
			print("Invalid Selection")

	# Checking Destinations here, to allow turn loop to end/reset and prevent nested loops
	if destination == "end" or destination == "battle":
		# move to next players turn
		print("Turn End")
		time.sleep(0.5)

		print("\n" * 50)

		if firstTurn == 0:
			firstTurn = 1

		exitProg = "false"
		return exitProg
	elif destination == "menu":
		# Reset
		reset()

		exitProg = "true"

		# exit method
		print("\n" * 2)

		# Return to Main Menu
		return exitProg

# Menu that contains the battle phase
def battleMenu(turnPlayer: duelist, passivePlayer: duelist):
	print("Battle Phase Engaged")

	# Check Field

	print("--------------------------------------")
	print("Your Field:")
	turnPlayer.checkField()

	print("--------------------------------------")
	print("{}'s Field".format(passivePlayer.name))
	passivePlayer.checkField()

	# Battle Phase Menu

	while True:
		if turnPlayer.lifepoints == 0 or passivePlayer.lifepoints == 0:
			selection = 2
			global destination
			destination = "menu"
			break


		print("--------------------------------------")
		print("[1] Attack with a Monster")

		print("[2] End your Turn")

		print("[0]  Return")

		try:
			selection = input("~~~Select an Action")
			selection = int(selection)

			if selection > 2:
				raise ValueError

			break
		except ValueError:
			print("--------------------------------------")
			print("Invalid Selection")

	if selection == 1:

		# loop through battle phase procedure
		while True:

			if turnPlayer.lifepoints == 0 or passivePlayer.lifepoints == 0:
				break

			# Retrieve the user monster selection
			while True:

				# check if all monsters have attacked
				global allAttacked
				allAttacked = 1

				# Check if any monsters have not attacked yet
				for monster in turnPlayer.monfield:
					if monster.attacked == 0:
						allAttacked = 0

				# If all monsters have attacked
				if allAttacked == 1:
					print("All Possible Monsters attacked, ending battle phase and turn...")
					time.sleep(1.5)
					return 0

				# Print all monsters on your field
				print("--------------------------------------")
				turnPlayer.checkFieldAtk()

				print("[0]  Return")
				print("--------------------------------------")
				target = input("~~Please select a monster to attack with")

				try:
					target = int(target) - 1
				except ValueError:
					pass
				except TypeError:
					pass

				if target == -1:
					return 1

				try:
					if turnPlayer.monfield[target].attacked == 0:
						atkMon = turnPlayer.monfield[target]
						atkMon.attacked = 1
						break
					else:
						print("--------------------------------------")
						print("Invalid Selection")
				except (ValueError, IndexError, TypeError):
					print("--------------------------------------")
					print("Invalid Selection")
					print("Group")

			# retrieve the user attack target
			if passivePlayer.monfield:
				while True:

					passivePlayer.checkField()

					print("--------------------------------------")
					target = input("~~Please select a monster to attack:")

					try:
						target = int(target) - 1
					except (TypeError, IndexError, ValueError):
						pass

					try:
						atkTarget = passivePlayer.monfield[target]
						break
					except (IndexError, TypeError):
						print("--------------------------------------")
						print("Invalid Selection")
						print("--------------------------------------")

				damage = atkMon.atkPoints - atkTarget.atkPoints
			else:
				print("Direct Attack!")
				damage = atkMon.atkPoints
				atkTarget = None

			# Monster Effect: Attacker (Returns Damage)
			try:
				if atkMon.trigger.name == "attack" or atkMon.trigger.name == "battle" and returnEffectChecker(atkMon):
					monster = atkMon
					if atkTarget is not None:
						oppmonster = atkTarget
						damage = monster.effect.resolve(turnPlayer, passivePlayer, monster,
														oppmonster, turnPlayer.gy, passivePlayer.gy, turnPlayer)
					else:
						damage = monster.effect.resolve(turnPlayer, passivePlayer, monster,
														None, turnPlayer.gy, passivePlayer.gy, turnPlayer)
			except AttributeError:
				pass
			except IndexError:
				pass

			# Monster Effect: Defender (Returns Damage)
			try:
				if atkTarget.trigger.name == "defend" or atkTarget.trigger.name == "battle" and returnEffectChecker(atkTarget):
					monster = atkTarget
					if atkTarget is not None:
						oppmonster = atkMon
						damage = monster.effect.resolve(passivePlayer, turnPlayer, monster,
														oppmonster, turnPlayer.gy, passivePlayer.gy, turnPlayer)
					else:
						damage = monster.effect.resolve(passivePlayer, turnPlayer, monster,
														None, turnPlayer.gy, passivePlayer.gy, turnPlayer)
			except AttributeError:
				pass
			except IndexError:
				pass

			if turnPlayer.lifepoints == 0 or passivePlayer.lifepoints == 0:
				break

			if damage is None:  # This occurs for effect returns that don't impact damage
				try:
					damage = atkMon.atkPoints - atkTarget.atkPoints
				except (UnboundLocalError, AttributeError):
					damage = atkMon.atkPoints

			if damage == -1:
				try:
					damage = atkMon.atkPoints
				except (UnboundLocalError, ValueError):
					damage = 0

			if damage > 0:

				passivePlayer.loseLP(damage)

				try:
					oppmonster = atkTarget
					if oppmonster.trigger.name == "destructionBat" and returnEffectChecker(oppmonster):
						result = oppmonster.effect.resolve(passivePlayer, turnPlayer, oppmonster, atkMon, passivePlayer.gy, turnPlayer.gy, turnPlayer)
						if result:
							pass
						else:
							result = 0

						if result == 0:
							passivePlayer.destroyMonsterBat(atkTarget, passivePlayer, turnPlayer, oppmonster, atkMon, passivePlayer.gy, turnPlayer.gy, turnPlayer)
						else:
							pass
					else:
						passivePlayer.destroyMonsterBat(atkTarget, passivePlayer, turnPlayer, oppmonster, atkMon, passivePlayer.gy, turnPlayer.gy, turnPlayer)
				except IndexError:
					pass
				except AttributeError:
					pass
				except UnboundLocalError:
					pass
				time.sleep(1)

			elif damage < 0:
				turnPlayer.loseLP(damage * -1)

				if atkTarget:
					pass
				else:
					atkTarget = object

				if atkMon.trigger.name == "destructionBat" and returnEffectChecker(atkMon):
					result = atkMon.effect.resolve(turnPlayer, passivePlayer, atkMon, atkTarget, turnPlayer.gy, passivePlayer.gy, turnPlayer)

					if result == 0:
						turnPlayer.destroyMonsterBat(atkMon, turnPlayer, passivePlayer, atkMon, atkTarget, turnPlayer.gy, passivePlayer.gy, turnPlayer)
					else:
						pass
				else:
					turnPlayer.destroyMonsterBat(atkMon, turnPlayer, passivePlayer, atkMon, atkTarget, turnPlayer.gy, passivePlayer.gy, turnPlayer)
				time.sleep(1)

			elif damage == 0:

				print("No Damage")

				# Check if the attack target is still on the field
				if atkTarget in passivePlayer.monfield:
					pass
				else:
					atkTarget = None

				# destroy both monsters if they exist
				try:
					if atkMon and atkTarget:

						if atkTarget.trigger.name == "destructionBat" and returnEffectChecker(atkTarget):
							result = atkTarget.effect.resolve(turnPlayer, passivePlayer, atkTarget, atkMon, turnPlayer.gy, passivePlayer.gy, turnPlayer)

							if result == 0:
								passivePlayer.destroyMonsterBat(atkTarget, turnPlayer, passivePlayer, atkTarget, atkMon, turnPlayer.gy, passivePlayer.gy, turnPlayer)
							else:
								pass
						else:
							passivePlayer.destroyMonsterBat(atkTarget, turnPlayer, passivePlayer, atkTarget, atkMon, turnPlayer.gy, passivePlayer.gy, turnPlayer)

						if atkMon.trigger.name == "destructionBat":
							result = atkMon.effect.resolve(turnPlayer, passivePlayer, atkMon, atkTarget, turnPlayer.gy, passivePlayer.gy, turnPlayer)

							if result == 0:
								turnPlayer.destroyMonsterBat(atkMon, turnPlayer, passivePlayer, atkMon, atkTarget, turnPlayer.gy, passivePlayer.gy, turnPlayer)
							else:
								pass
						else:
							turnPlayer.destroyMonsterBat(atkMon, turnPlayer, passivePlayer, atkMon, atkTarget, turnPlayer.gy, passivePlayer.gy, turnPlayer)
				except IndexError:
					pass
				time.sleep(1)

				pass
	elif selection == 0:
		return 1
	elif selection == 2:
		return 0
	else:
		raise NotImplementedError

# sets duelist and foe objects
_player = duelist("", 8000, [], [], [], [])  # (name, lifepoints, hand, monfield, deck, graveyard)

_foe = duelist("", 8000, [], [], [], [])  # (name, lifepoints, hand, monfield, deck, graveyard)

mainMenu()
