# https://docs.python.org/3/library/enum.html <-- FOR ENUM INFO
import copy
import time
import random
import effect
import sys
from effect import effTrigger
from duelist import duelist
from card import *
from settings import *

# Method to setup the card database and runs player_deck_setup()
def card_player_deck_setup():

	# The card template is as follows:
	# card(Name, Atk Points, Effect Name, Effect Trigger Enum, Effect Derscription)

	DoubleSummon = {"effect"       : effect.doubleSummon,
	                "effectTrigger": effTrigger.summon}
	SpecialCodeDeck = {"effect"       : effect.specialCodeDeck,
	                       "effectTrigger": effTrigger.summon}
	SpecialCodeHand = {"effect"       : effect.specialCodeHand,
	                   "effectTrigger": effTrigger.graveyard}
	PlayerDraw1Grav = {"effect"       : effect.playerDraw1,
	                   "effectTrigger": effTrigger.graveyard}
	EffectCyberseSearch = {"effect"       : effect.effectCyberseSearch,
	                    "effectTrigger": effTrigger.summon}
	SpecialCyberseHand = {"effect"       : effect.specialCyberseHand,
	                      "effectTrigger": effTrigger.summon}
	SpecialCyberseHandDest = {"effect"       : effect.specialCyberseHand,
	                      "effectTrigger": effTrigger.destructionBat}
	DestroySum = {"effect"       : effect.Destroy,
	              "effectTrigger": effTrigger.summon}
	OppDisc1 = {"effect"       : effect.oppDisc1,
	            "effectTrigger": effTrigger.summon}
	OppDisc2 = {"effect"       : effect.oppDisc2,
	            "effectTrigger": effTrigger.battle}
	SelfDisc1 = {"effect"       : effect.playerDisc1,
	             "effectTrigger": effTrigger.graveyard}
	EffectSearch = {"effect"       : effect.effectSearch,
	                "effectTrigger": effTrigger.summon}
	# SpecialFromHand = {"effect"       : effect.specialfromHand,
	#                    "effectTrigger": effTrigger.battle}
	MonsterBounce = {"effect"       : effect.bounceMonster,
	                 "effectTrigger": effTrigger.summon}
	# GrantFloat1Sum = {"effect"       : effect.GrantFloat1,
	#                   "effectTrigger": effTrigger.summon}
	GrantDisc1Cyberse = {"effect"       : effect.GrantDisc1Cyberse,
	                         "effectTrigger": effTrigger.summon}

	# Cyber Deck
	# global microCoder
	# global microCoder2
	# global codeGenerator
	# global codeGenerator2
	# global codeRadiator
	# global codeRadiator2
	# global ladyDebug
	# global ladyDebug2
	global cyberseGadget
	# global cyberseGadget2
	# global cyberseAccelerator
	# global cyberseAccelerator2
	# global cyberseWhiteHat
	# global cyberseWhiteHat2
	# global excodeTalker
	# global excodeTalker2
	# global dualAssembwurm
	# global dualAssembwurm2
	# global cyberseDriver
	# global cyberseDriver2

	microCoder = card("Micro Coder", 300, 0, [SpecialCodeDeck, PlayerDraw1Grav])
	codeGenerator = card("Code Generator", 1300, 0, [EffectCyberseSearch, SpecialCodeHand])
	codeRadiator = card("Code Radiator", 1600, 0, [DoubleSummon, PlayerDraw1Grav])
	ladyDebug = card("Lady Debug", 1000, 0, [SpecialCyberseHand])
	cyberseGadget = card("Cyberse Gadget", 1400, 0, [DestroySum, SpecialCyberseHandDest])
	cyberseAccelerator = card("Cyberse Accelerator", 2000, 0, [OppDisc1, SelfDisc1])
	cyberseWhiteHat = card("Cyberse White Hat", 2100, 1, [EffectSearch])
	excodeTalker = card("Excode Talker", 2300, 1, [GrantDisc1Cyberse, OppDisc1])
	cyberseAssembwurm = card("Cyberse Assembwurm", 2800, 1, [OppDisc2])
	cyberseDriver = card("Cyberse Driver", 2200, 1, [MonsterBounce])
	microCoder2 = copy.deepcopy(microCoder)
	codeGenerator2 = copy.deepcopy(codeGenerator)
	codeRadiator2 = copy.deepcopy(codeRadiator)
	cyberseDriver2 = copy.deepcopy(cyberseDriver)
	ladyDebug2 = copy.deepcopy(ladyDebug)
	cyberseGadget2 = copy.deepcopy(cyberseGadget)
	cyberseAccelerator2 = copy.deepcopy(cyberseAccelerator)
	cyberseWhiteHat2 = copy.deepcopy(cyberseWhiteHat)
	excodeTalker2 = copy.deepcopy(excodeTalker)
	cyberseAssembwurm2 = copy.deepcopy(cyberseAssembwurm)

	EffectVampSearch = {"effect"       : effect.effectVampSearch,
	                "effectTrigger": effTrigger.graveyard}
	DiscSpecVampHand = {"effect"       : effect.discSpecVampHand,
	                "effectTrigger": effTrigger.summon}
	BattleImmune = {"effect"       : effect.battleImmune,
	                "effectTrigger": effTrigger.destructionBat}
	SiphonLifeAndMill800 = {"effect"       : effect.siphonLifeAndMill800,
	                "effectTrigger": effTrigger.summon}
	SiphonLifeAndMill1500 = {"effect"       : effect.siphonLifeAndMill1500,
	                "effectTrigger": effTrigger.battle}
	ShuffleToSSGraveyard = {"effect": effect.shuffleToSSGraveyard,
	                        "effectTrigger": effTrigger.graveyard}
	GYToHand = {"effect"       : effect.gyToHand,
	                    "effectTrigger": effTrigger.summon}
	Siphon800 = {"effect"       : effect.siphonLife800,
	            "effectTrigger": effTrigger.summon}
	Grant800 = {"effect"       : effect.grant800,
	          "effectTrigger": effTrigger.summon}
	Millie = {"effect"       : effect.Mill,
	            "effectTrigger": effTrigger.summon}

	# # Vampire Deck
	# global vampireFamiliar
	# global vampireFamiliar2
	# global vampireSucker
	# global vampireSucker2
	# global vampireFraulein
	# global vampireFraulein2
	# global vampireGrace
	# global vampireGrace2
	# global vampireGenesis
	# global vampireGenesis2
	# global mezuki
	# global mezuki2
	# global unizombie
	# global unizombie2
	# global shiranuiSolitare
	# global shiranuiSolitare2
	# global armageddonKnight
	# global armageddonKnight2
	# global zombieMaster
	# global zombieMaster2

	vampireFamiliar = card("Vampire Familiar", 300, 0, [EffectVampSearch, Siphon800])
	vampireFamiliar2 = copy.deepcopy(vampireFamiliar)
	vampireSucker = card("Vampire Sucker", 1600, 0, [DiscSpecVampHand])
	vampireSucker2 = copy.deepcopy(vampireSucker)
	vampireFraulein = card("Vampire Fraulein", 800, 0, [BattleImmune, Grant800])
	vampireFraulein2 = copy.deepcopy(vampireFraulein)
	vampireGrace = card("Vampire Grace", 2200, 1, [SiphonLifeAndMill800])
	vampireGrace2 = copy.deepcopy(vampireGrace)
	vampireGenesis = card("Vampire Genesis", 2800, 1, [SiphonLifeAndMill1500])
	# vampireGenesis2 = copy.deepcopy(vampireGenesis)
	mezuki = card("Mezuki", 1600, 0, [ShuffleToSSGraveyard])
	mezuki2 = copy.deepcopy(mezuki)
	unizombie = card("Uni-Zombie", 1500, 0, [GYToHand])
	unizombie2 = copy.deepcopy(unizombie)
	shiranuiSolitare = card("Shiranui Solitare", 1300, 0, [PlayerDraw1Grav, Siphon800])
	shiranuiSolitare2 = copy.deepcopy(shiranuiSolitare)
	armageddonKnight = card("Armageddon Knight", 1400, 0, [Millie])
	armageddonKnight2 = copy.deepcopy(armageddonKnight)
	zombieMaster = card("Zombie Master", 1800, 0, [DestroySum])
	zombieMaster2 = copy.deepcopy(zombieMaster)

	Battle500 = {"effect"       : effect.gain500,
	                    "effectTrigger": effTrigger.battle}
	PlayerDraw2Battle = {"effect"       : effect.playerDraw2,
	                    "effectTrigger": effTrigger.battle}
	EvigishkiSearch = {"effect": effect.effectEvigishkiSearch,
	                "effectTrigger": effTrigger.summon}
	MatchAttack = {"effect": effect.matchAttack,
	               "effectTrigger": effTrigger.battle}
	SpecialGishkiDeck = {"effect"       : effect.specialGishkiDeck,
	                    "effectTrigger": effTrigger.battle}
	SearchGishkiAquamirror = {"effect": effect.effectGishkiMirrorSearch,
	                          "effectTrigger": effTrigger.summon}
	Battle1000 = {"effect"       : effect.gain1000,
	             "effectTrigger": effTrigger.battle}
	EvigishkiGain400 = {"effect": effect.evigishkiGain400,
	                    "effectTrigger": effTrigger.summon}
	DestroyBat = {"effect": effect.Destroy,
	              "effectTrigger": effTrigger.battle}

	# # Gishki Deck
	# global gishkiBeast
	# global gishkiBeast2
	# global gishkiAbyss
	# global gishkiAbyss2
	# global gishkiAquamirror
	# global gishkiAquamirror2
	# global gishkiShadow
	# global gishkiShadow2
	# global visionGishki
	# global visionGishki2
	# global gishkiAriel
	# global gishkiAriel2
	# global evigishkiLevianima
	# global evigishkiLevianima2
	# global evigishkiSoulOgre
	# global evigishkiSoulOgre2
	# global evigishkiGustKraken
	# global evigishkiGustKraken2
	# global evigishkiPsychlone
	# global evigishkiPsychlone2

	gishkiBeast = card("Gishki Beast", 1500, 0, [Battle500])
	gishkiBeast2 = copy.deepcopy(gishkiBeast)
	gishkiAbyss = card("Gishki Abyss", 800, 0, [PlayerDraw2Battle])
	gishkiAbyss2 = copy.deepcopy(gishkiAbyss)
	gishkiAquamirror = card("Gishki Aquamirror", 0, 0, [DoubleSummon])
	gishkiAquamirror2 = copy.deepcopy(gishkiAquamirror)
	gishkiShadow = card("Gishki Shadow", 1200, 0, [EvigishkiSearch, MatchAttack])
	gishkiShadow2 = copy.deepcopy(gishkiShadow)
	visionGishki = card("Vision Gishki ", 1800, 0, [SpecialGishkiDeck])
	visionGishki2 = copy.deepcopy(visionGishki)
	gishkiAriel = card("Gishki Ariel", 1200, 0, [MonsterBounce])
	gishkiAriel2 = copy.deepcopy(gishkiAriel)
	evigishkiLevianima = card("Evigishki Levianima", 2200, 1, [SearchGishkiAquamirror, Battle500])
	evigishkiLevianima2 = copy.deepcopy(evigishkiLevianima)
	evigishkiSoulOgre = card("Evigishki Soul Ogre", 2800, 1, [Battle1000])
	# evigishkiSoulOgre2 = copy.deepcopy(evigishkiSoulOgre)
	evigishkiGustKraken = card("Evigishki Gustkraken", 2500, 1, [EvigishkiGain400])
	evigishkiGustKraken2 = copy.deepcopy(evigishkiGustKraken)
	evigishkiPsychlone = card("Evigishki Psychlone", 2000, 1, [DestroyBat])
	evigishkiPsychlone2 = copy.deepcopy(evigishkiPsychlone)

	SpecialHeraldDeck = {"effect": effect.specialHeraldDeck,
	                     "effectTrigger": effTrigger.summon}
	SearchHeraldDeck = {"effect": effect.effectHeraldSearch,
	                    "effectTrigger": effTrigger.summon}
	SearchAgentDeck = {"effect": effect.effectAgentSearch ,
	                   "effectTrigger": effTrigger.summon}
	SpecialAgentDeck = {"effect": effect.specialAgentDeck,
	                    "effectTrigger": effTrigger.graveyard}
	Restore2000 = {"effect": effect.restore2000,
	               "effectTrigger": effTrigger.graveyard}
	HeraldGain400 = {"effect": effect.heraldGain400,
	                 "effectTrigger": effTrigger.summon}
	DrawForDiff = {"effect": effect.DifferenceDraw,
	               "effectTrigger": effTrigger.summon}
	Gain1000forHand = {"effect": effect.RestoreLPForHand1000,
	                 "effectTrigger": effTrigger.summon}
	GainDifference = {"effect": effect.gainDifference,
	                  "effectTrigger": effTrigger.summon}
	SpecialHand = {"effect": effect.specialfromHand,
	               "effectTrigger": effTrigger.summon}

	# Herald Deck
	# global orangeHerald
	# global orangeHerald2
	# global purpleHerald
	# global purpleHerald2
	# global arcHerald
	# global arcHerald2
	# global dawnHerald
	# global dawnHerald2
	# global agentEarth
	# global agentEarth2
	# global agentVenus
	# global agentVenus2
	# global agentMars
	# global agentMars2
	# global agentSaturn
	# global agentSaturn2
	# global heraldPerfection
	# global heraldPerfection2
	# global masterHyperion
	# global masterHyperion2

	orangeHerald = card("Herald of Orange Light", 1000, 0, [SpecialHeraldDeck])
	orangeHerald2 = copy.deepcopy(orangeHerald)
	purpleHerald = card("Herald of Purple Light", 1800, 0, [HeraldGain400, PlayerDraw1Grav])
	purpleHerald2 = copy.deepcopy(purpleHerald)
	arcHerald = card("Herald of Arc Light", 800, 0, [SearchAgentDeck, Restore2000])
	arcHerald2 = copy.deepcopy(arcHerald)
	dawnHerald = card("Herald of the Dawn", 0, 0, [DoubleSummon])
	dawnHerald2 = copy.deepcopy(dawnHerald)
	agentEarth = card("Agent of Mystery: Earth", 1200, 0, [SearchHeraldDeck, SpecialAgentDeck])
	agentEarth2 = copy.deepcopy(agentEarth)
	agentVenus = card("Agent of Creation: Venus", 1600, 0, [DrawForDiff])
	agentVenus2 = copy.deepcopy(agentVenus)
	agentMars = card("Agent of Force: Mars", 1800, 0, [DestroySum])
	agentMars2 = copy.deepcopy(agentMars)
	agentSaturn = card("Agent of Judgment: Saturn", 2400, 1, [Gain1000forHand])
	agentSaturn2 = copy.deepcopy(agentSaturn)
	heraldPerfection = card("Herald of Perfection", 2800, 1, [GainDifference])
	# heraldPerfection2 = copy.deepcopy(heraldPerfection)
	masterHyperion = card("Master Hyperion", 2800, 1, [SpecialHand])
	# masterHyperion2 = copy.deepcopy(masterHyperion)

	EffectImmune = {"effect": effect.effectImmune,
	                "effectTrigger": effTrigger.destructionEff}
	DarkMagicianGain400 = {"effect": effect.darkMagicianGain400,
	                "effectTrigger": effTrigger.summon}
	SpecialDarkMagicianHand = {"effect": effect.specialDarkMagicianHand,
	                "effectTrigger": effTrigger.summon}
	SpecialMagicianGirlHand = {"effect": effect.specialMagicianGirlHand,
	                "effectTrigger": effTrigger.summon}
	HalfAtk = {"effect": effect.halfAtk,
	                "effectTrigger": effTrigger.defend}
	HalfAtkMsg = {"effect": effect.halfAtkMsg,
	                "effectTrigger": effTrigger.defend}
	PlayerDraw2Defend = {"effect": effect.playerDraw2,
	                "effectTrigger": effTrigger.defend}
	SpecialGirlLess2000 = {"effect": effect.specialGirlLess2000,
	                "effectTrigger": effTrigger.summon}
	SpecialDarkMagicianDeck = {"effect": effect.specialDarkMagicianDeck,
	                "effectTrigger": effTrigger.summon}
	Atk0 = {"effect": effect.atk0,
	        "effectTrigger": effTrigger.defend}

	# # Magician Deck
	# global darkMagician
	# global darkMagician2
	# global darkGMagician
	# global darkGMagician2
	# global lemonGirl
	# global lemonGirl2
	# global magicianRobe
	# global magicianRobe2
	# global chocolateGirl
	# global chocolateGirl2
	# global appleGirl
	# global appleGirl2
	# global kiwiGirl
	# global kiwiGirl2
	# global berryGirl
	# global berryGirl2
	# global ebonIllusion
	# global ebonIllusion2
	# global magiMagiGirl
	# global magiMagiGirl2

	darkMagician = card("Dark Magician", 2500, 1, [EffectImmune])
	darkMagician2 = copy.deepcopy(darkMagician)
	darkGMagician = card("Dark Magician Girl", 2300, 1, [DarkMagicianGain400])
	darkGMagician2 = copy.deepcopy(darkGMagician)
	lemonGirl = card("Lemon Magician Girl", 1600, 0, [SpecialMagicianGirlHand])
	lemonGirl2 = copy.deepcopy(lemonGirl)
	magicianRobe = card("Magician's Robe", 800, 0, [DoubleSummon])
	magicianRobe2 = copy.deepcopy(magicianRobe)
	chocolateGirl = card("Chocolate Magician Girl", 1800, 0, [SpecialDarkMagicianHand])
	chocolateGirl2 = copy.deepcopy(chocolateGirl)
	appleGirl = card("Apple Magician Girl", 600, 0, [PlayerDraw2Defend, HalfAtk])
	appleGirl2 = copy.deepcopy(appleGirl)
	berryGirl = card("Berry Magician Girl", 1200, 0, [SpecialGirlLess2000])
	berryGirl2 = copy.deepcopy(berryGirl)
	kiwiGirl = card("Kiwi Magician Girl", 300, 0, [DestroySum, HalfAtkMsg])
	kiwiGirl2 = copy.deepcopy(kiwiGirl)
	ebonIllusion = card("Ebon Illusion Magician", 2000, 1, [SpecialDarkMagicianDeck])
	ebonIllusion2 = copy.deepcopy(ebonIllusion)
	magiMagiGirl = card("Magi Magician Girl", 2600, 1, [Atk0])
	magiMagiGirl2 = copy.deepcopy(magiMagiGirl)

	SpecialStormBirdHand = {"effect": effect.specialStormBirdHand,
	                        "effectTrigger": effTrigger.summon}
	SpecialStormRiderDeck = {"effect": effect.specialStormRiderDeck,
	                        "effectTrigger": effTrigger.summon}
	DiscSpecStormGY = {"effect": effect.discSpecStormGY,
	                        "effectTrigger": effTrigger.summon}
	ControlStormriderDraw2 = {"effect": effect.controlStormriderDraw2,
	                        "effectTrigger": effTrigger.summon}
	ControlStormriderDestroy = {"effect": effect.controlStormriderDestroy,
	                        "effectTrigger": effTrigger.summon}
	GrantStormriderAttack = {"effect": effect.grantStormriderAttack,
	                        "effectTrigger": effTrigger.summon}
	TribToSpecialStormBird = {"effect": effect.tribToSpecialStormBird,
	                        "effectTrigger": effTrigger.summon}
	StormBirdGain400 = {"effect": effect.stormBirdGain400,
	                        "effectTrigger": effTrigger.summon}
	StormRiderGain400 = {"effect": effect.stormRiderGain400,
	                        "effectTrigger": effTrigger.summon}

	# # Storm Deck
	# global stormRiderAllyson
	# global stormRiderAllyson2
	# global stormBirdZephris
	# global stormBirdZephris2
	# global stormRiderHellion
	# global stormRiderHellion2
	# global stormBirdHellDiver
	# global stormBirdHellDiver2
	# global stormRiderCanto
	# global stormRiderCanto2
	# global stormBirdSkylar
	# global stormBirdSkylar2
	# global stormRiderNess
	# global stormRiderNess2
	# global stormBirdGale
	# global stormBirdGale2
	# global stormRiderMason
	# global stormRiderMason2
	# global stormBirdAce
	# global stormBirdAce2

	stormRiderAllyson = card("Allyson: Storm Rider", 800, 0, [SpecialStormBirdHand])
	stormRiderAllyson2 = copy.deepcopy(stormRiderAllyson)
	stormRiderHellion = card("Hellion: Storm Rider", 900, 0, [SpecialStormRiderDeck])
	stormRiderHellion2 = copy.deepcopy(stormRiderHellion)
	stormRiderCanto = card("Canto: Storm Rider", 500, 0, [DoubleSummon])
	stormRiderCanto2 = copy.deepcopy(stormRiderCanto)
	stormRiderNess = card("Ness: Storm Rider", 750, 0, [DiscSpecStormGY])
	stormRiderNess2 = copy.deepcopy(stormRiderNess)
	stormRiderMason = card("Mason: Storm Rider", 2000, 1, [StormRiderGain400])
	stormRiderMason2 = copy.deepcopy(stormRiderMason)
	stormBirdZephris = card("Zephris: Storm Bird", 1600, 0, [ControlStormriderDraw2])
	stormBirdZephris2 = copy.deepcopy(stormBirdZephris)
	stormBirdHellDiver = card("Hell Diver: Storm Bird", 1800, 0, [ControlStormriderDestroy])
	stormBirdHellDiver2 = copy.deepcopy(stormBirdHellDiver)
	stormBirdSkylar = card("Skylar: Storm Bird", 1000, 0, [GrantStormriderAttack])
	stormBirdSkylar2 = copy.deepcopy(stormBirdSkylar)
	stormBirdGale = card("Gale: Storm Bird", 1500, 0, [TribToSpecialStormBird])
	stormBirdGale2 = copy.deepcopy(stormBirdGale)
	stormBirdAce = card("Ace: Storm Bird", 2000, 1, [StormBirdGain400])
	stormBirdAce2 = copy.deepcopy(stormBirdAce)

	Atk100Grave = {"effect": effect.atk100GrantAll,
	               "effectTrigger": effTrigger.graveyard}
	SpecialFireKingGrave = {"effect": effect.specialFireKingGrave,
	               "effectTrigger": effTrigger.summon}
	SpecialEffectDestruction = {"effect": effect.specialEffDestruction,
	                            "effectTrigger": effTrigger.otherCardEffDestruction}
	DestroyInHand = {"effect"       : effect.destroyInHand,
	                  "effectTrigger": effTrigger.summon}
	FireSearchDest = {"effect": effect.effectFireSearch,
	                  "effectTrigger": effTrigger.destructionEff}
	SpecialFormationDeck = {"effect": effect.specialFormationDeck,
	                  "effectTrigger": effTrigger.summon}
	SpecialFormationDeckDest = {"effect": effect.specialFormationDeck,
	                  "effectTrigger": effTrigger.destructionEff}
	Atk500Summon = {"effect": effect.atk500GrantAll,
	                  "effectTrigger": effTrigger.summon}
	SpecialFistDeck = {"effect": effect.specialFistDeckLess2000,
	                   "effectTrigger": effTrigger.destroyBattle}
	Atk500Kill = {"effect"       : effect.atk500GrantAll,
	                "effectTrigger": effTrigger.destroyBattle}
	TribDraw2 = {"effect": effect.tribDisc1Draw2,
	             "effectTrigger": effTrigger.summon}
	SearchFireDeck = {"effect": effect.effectFireSearch,
	                  "effectTrigger": effTrigger.summon}
	MillieGrav = {"effect"       : effect.Mill,
	          "effectTrigger": effTrigger.graveyard}
	MillieBat = {"effect"       : effect.Mill,
	          "effectTrigger": effTrigger.destructionBat}
	DestroyGrav = {"effect": effect.Destroy,
	               "effectTrigger": effTrigger.graveyard}
	PheonixResurrection = {"effect": effect.PhoenixResurrection,
	                       "effectTrigger": effTrigger.destructionEff}
	FFCheckSummon = {"effect": effect.FFSummon,
	                 "effectTrigger": effTrigger.summon}

	# global fireKingArvata
	# global fireKingArvata2
	# global fireKingYaksha
	# global fireKingYaksha2
	# global fireKingGarunix
	# global fireKingGarunix2
	# global fireKingBarong
	# global fireKingBarong2
	# global fireFistBear
	# global fireFistBear2
	# global fireFistHawk
	# global fireFistHawk2
	# global fireFistKarin
	# global fireFistKarin2
	# global fireFistGorilla
	# global fireFistGorilla2
	# global fireFormationTensu
	# global fireFormationTensu2
	# global fireFormationTenki
	# global fireFormationGyokkou
	# global fireFormationSeito

	fireKingArvata = card("Fire King Arvata", 1800, 0, [SpecialFistDeck, SpecialEffectDestruction])  # Special monster from Grave | Draw Card
	fireKingArvata2 = copy.deepcopy(fireKingArvata)
	fireKingYaksha = card("Fire King Yaksha", 1900, 0, [SpecialEffectDestruction, FireSearchDest])  # Special Summons itself from hand | Destroys a card on field
	fireKingYaksha2 = copy.deepcopy(fireKingYaksha)
	fireKingGarunix = card("Fire King High Avatar Garunix", 2700, 1, [PheonixResurrection, MillieBat])  # Destroys all monsters on board, summons next turn
	# fireKingGarunix2 = copy.deepcopy(fireKingGarunix)
	fireKingBarong = card("Fire King Barong", 1800, 0, [DestroyInHand, DestroyGrav])  # Special Summons itself from hand, then destroy a card | Searches
	fireKingBarong2 = copy.deepcopy(fireKingBarong)
	fireFistBear = card("Fire Fist Bear", 1200, 0, [SpecialFormationDeck, SpecialFormationDeckDest])  # Special Summons a Formation
	fireFistBear2 = copy.deepcopy(fireFistBear)
	fireFistHawk = card("Fire Fist Hawk", 200, 0, [Atk500Summon, SpecialEffectDestruction])  # Grants all Fire monsters 500 Atk | Draw
	fireFistHawk2 = copy.deepcopy(fireFistHawk)
	fireFistGorilla = card("Fire Fist Gorilla", 1800, 0, [SpecialFireKingGrave, PlayerDraw1Grav])  # When destroy monster by battle, Special Fire Fist from deck
	fireFistGorilla2 = copy.deepcopy(fireFistGorilla)
	fireFistKarin = card("Fire Fist Karin", 2600, 1, [Atk500Kill, MillieGrav])  # When destroy monster by battle, grant all Fire monsters on field 500 Atk | Mill a card
	fireFistKarin2 = copy.deepcopy(fireFistKarin)
	fireFormationTensu = card("Fire Formation Tensu", 0, 0, [DoubleSummon, Atk100Grave])
	fireFormationTensu2 = copy.deepcopy(fireFormationTensu)
	fireFormationTenki = card("Fire Formation Tenki", 0, 0, [SearchFireDeck, Atk100Grave]) # Search a fire Fist | Grant ATK in grave
	fireFormationGyokkou = card("Fire Formation Gyokkou", 0, 0, [TribDraw2, Atk100Grave]) # tribute to draw 2 | Grant ATK in grave
	fireFormationSeito = card("Fire Formation Seito", 0, 1, [FFCheckSummon, Atk100Grave])  # if 4 fire different fire fist monsters in grave, Special summon 4 fire fists for Tribute | Grant ATK in grave

	SpecialJungleGrave = {"effect": effect.specialJungleGrave,
	                      "effectTrigger": effTrigger.summon}
	GrantBattleImmune = {"effect": effect.GrantBattleDestructionKarliah,
	                     "effectTrigger": effTrigger.summon}
	EffectJungleSearch = {"effect": effect.effectJungleSearch,
	                     "effectTrigger": effTrigger.summon}
	EffectKarliahSearch = {"effect": effect.effectKarliahSearch,
	                       "effectTrigger": effTrigger.graveyard}
	grantSelfFloat = {"effect": effect.GrantSelfFloat,
	                     "effectTrigger": effTrigger.graveyard}
	KarliahDoubleAttack = {"effect": effect.karliahDoubleAttack,
	                       "effectTrigger": effTrigger.summon}
	ControlKarliahDestroy = {"effect": effect.controlKarliahDestroy,
	                         "effectTrigger": effTrigger.summon}
	Grant800Grav = {"effect": effect.grant800,
	                "effectTrigger": effTrigger.graveyard}
	SpecialJungleDeck = {"effect": effect.specialJungleDeck,
	                     "effectTrigger": effTrigger.summon}
	SpecialKarliahDeck = {"effect": effect.specialKarliahDeck,
	                      "effectTrigger": effTrigger.summon}
	GrantEffectImmune = {"effect": effect.GrantEffectImmuneKarliah,
	                     "effectTrigger": effTrigger.summon}
	JungleDiscDefense = {"effect": effect.jungleDiscDefense,
	                     "effectTrigger": effTrigger.discardDest}
	KarliahJungleDefenseBat = {"effect": effect.JungleDefense,
	                        "effectTrigger": effTrigger.destructionBat}
	KarliahJungleDefenseEff = {"effect": effect.JungleDefense,
	                        "effectTrigger": effTrigger.destructionEff}
	CannotBeAttacked = {"effect": effect.cannotBeAttacked,
	                    "effectTrigger": effTrigger.n_a}

	global jungleTravellerKarliah  # Searches a Jungle on Summon / Double Summon
	global mimicMeercat  # grants Karliah float eff to return herself to hand / copies atk
	global duckDucker  # grants Karliah OPT battle destruction / cannot be targetted for an attack
	global wokeWombat  # SS a Jungle from Grave / gy: search a Karliah
	global divingOsprey  # grants Karliah double atk / Float: draw 1
	global crouchingTiger  # if you control Karliah, destroy 1 monster / Float: Grant a Karliah 800 Atk
	global tentativeTurtle  # if Karliah would be destroyed by Card Effects; You can discard this card instead / Summon: Bounce a Monster
	global bushTourGuide  # SS a Jungle from Deck
	global squishySquid  # if Karliah would be returned to Hand; You can discard this card Instead / Summon: discard 1 draw 2
	global followMeFalcon  # Summon: Search karliah

	jungleTravellerKarliah = card("Jungle Traveller: Karliah", 1300, 0, [EffectJungleSearch, DoubleSummon, KarliahJungleDefenseBat, KarliahJungleDefenseEff])
	mimicMeercat = card("Jungle Companion: Mimic Meercat!", 0, 0, [grantSelfFloat, MatchAttack])
	duckDucker = card("Jungle Companion: Duck Ducker!", 0, 0, [GrantBattleImmune, CannotBeAttacked], False)
	wokeWombat = card("Jungle Companion: Woke Wombat!?", 1200, 0, [SpecialJungleGrave, EffectKarliahSearch])
	divingOsprey = card("Jungle Companion: Diving Osprey!", 1600, 0, [KarliahDoubleAttack, PlayerDraw1Grav])
	crouchingTiger = card("Jungle Companion: Crouching Tiger!!", 1800, 0, [ControlKarliahDestroy, Grant800Grav])
	tentativeTurtle = card("Jungle Companion: Totalitarian Turtle!?", 1000, 0, [JungleDiscDefense, TribDraw2])
	bushTourGuide = card("Bush Tour Guide", 2500, 1, [SpecialJungleDeck])
	squishySquid = card("Jungle Companion: Squishy Squid!", 2300, 1, [GrantEffectImmune, MonsterBounce])
	followMeFalcon = card("Jungle Companion: Follow Me Falcon!", 2700, 1, [SpecialKarliahDeck])
	jungleTravellerKarliah2 = copy.deepcopy(jungleTravellerKarliah)
	jungleTravellerKarliah3 = copy.deepcopy(jungleTravellerKarliah)
	mimicMeercat2 = copy.deepcopy(mimicMeercat)
	duckDucker2 = copy.deepcopy(duckDucker)
	wokeWombat2 = copy.deepcopy(wokeWombat)
	divingOsprey2 = copy.deepcopy(divingOsprey)
	crouchingTiger2 = copy.deepcopy(crouchingTiger)
	tentativeTurtle2 = copy.deepcopy(tentativeTurtle)
	bushTourGuide2 = copy.deepcopy(bushTourGuide)
	squishySquid2 = copy.deepcopy(squishySquid)
	# followMeFalcon2 = copy.deepcopy(followMeFalcon)

	CyberDeck = []
	VampireDeck = []
	GishkiDeck = []
	HeraldDeck = []
	MagicianDeck = []
	StormDeck = []
	FireDeck = []
	JungleDeck = []

	PlayerList = []

	pass

	CyberDeck.append(microCoder)
	CyberDeck.append(microCoder2)
	CyberDeck.append(codeGenerator)
	CyberDeck.append(codeGenerator2)
	CyberDeck.append(codeRadiator)
	CyberDeck.append(codeRadiator2)
	CyberDeck.append(cyberseDriver)
	CyberDeck.append(cyberseDriver2)
	CyberDeck.append(ladyDebug)
	CyberDeck.append(ladyDebug2)
	CyberDeck.append(cyberseGadget)
	CyberDeck.append(cyberseGadget2)
	CyberDeck.append(cyberseAccelerator)
	CyberDeck.append(cyberseAccelerator2)
	CyberDeck.append(cyberseWhiteHat)
	CyberDeck.append(cyberseWhiteHat2)
	CyberDeck.append(excodeTalker)
	CyberDeck.append(excodeTalker2)
	CyberDeck.append(cyberseAssembwurm)
	CyberDeck.append(cyberseAssembwurm2)

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
	GishkiDeck.append(evigishkiGustKraken2)
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
	MagicianDeck.append(lemonGirl)
	MagicianDeck.append(lemonGirl2)
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
	StormDeck.append(stormRiderMason)
	StormDeck.append(stormRiderMason2)
	StormDeck.append(stormBirdAce)
	StormDeck.append(stormBirdAce2)

	FireDeck.append(fireKingArvata)
	FireDeck.append(fireKingArvata2)
	FireDeck.append(fireKingYaksha)
	FireDeck.append(fireKingYaksha2)
	FireDeck.append(fireKingBarong)
	FireDeck.append(fireKingBarong2)
	FireDeck.append(fireFistBear)
	FireDeck.append(fireFistBear2)
	FireDeck.append(fireFistHawk)
	FireDeck.append(fireFistHawk2)
	FireDeck.append(fireKingGarunix)
	FireDeck.append(fireFistKarin)
	FireDeck.append(fireFistKarin2)
	FireDeck.append(fireFistGorilla2)
	FireDeck.append(fireFormationTensu)
	FireDeck.append(fireFormationTensu2)
	FireDeck.append(fireFormationTenki)
	FireDeck.append(fireFormationGyokkou)
	FireDeck.append(fireFormationSeito)

	JungleDeck.append(jungleTravellerKarliah)
	JungleDeck.append(jungleTravellerKarliah2)
	JungleDeck.append(jungleTravellerKarliah3)
	JungleDeck.append(mimicMeercat)
	JungleDeck.append(mimicMeercat2)
	JungleDeck.append(duckDucker)
	JungleDeck.append(duckDucker2)
	JungleDeck.append(wokeWombat)
	JungleDeck.append(wokeWombat2)
	JungleDeck.append(divingOsprey)
	JungleDeck.append(divingOsprey2)
	JungleDeck.append(crouchingTiger)
	JungleDeck.append(crouchingTiger2)
	JungleDeck.append(tentativeTurtle)
	JungleDeck.append(tentativeTurtle2)
	JungleDeck.append(bushTourGuide)
	JungleDeck.append(bushTourGuide2)
	JungleDeck.append(squishySquid)
	JungleDeck.append(squishySquid2)
	JungleDeck.append(followMeFalcon)

	random.shuffle(CyberDeck)
	random.shuffle(VampireDeck)
	random.shuffle(GishkiDeck)
	random.shuffle(HeraldDeck)
	random.shuffle(MagicianDeck)
	random.shuffle(StormDeck)
	random.shuffle(FireDeck)
	random.shuffle(JungleDeck)

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

	for monster in FireDeck:
		monster.attacked = 0

	for monster in JungleDeck:
		monster.attacked = 0

	CyberPlayer = {
		"name"      : "Playmaker",
		"desc"      : "      " + settings.darkcyan + "A tech-savvy kid, who knows his way around a computer. Plays to undermine his opponents strategy from the roots" + settings.end,
		"deck"      : CyberDeck,
		"deckName"  : "Cyberse",
		"deckDesc"  : "Discarding / SS Hand",
		"voicelines": []
	}

	VampirePlayer = {
		"name"      : "Count Klaric",
		"desc"      : "      " + settings.darkcyan + "A skilled player with an obsession with vampire mythology. Focuses on sacrificing her own cards to drain his opponents' life dry" + settings.end,
		"deck"      : VampireDeck,
		"deckName"  : "Vampire",
		"deckDesc"  : "Stealing Life / Graveyard Effects",
		"voicelines": []
	}

	GishkiPlayer = {
		"name"      : "Gishki Avance",
		"desc"      : "      " + settings.darkcyan + "A distant traveler who has seen all walks of life. His deck mercilessely attacks his opponent, growing stronger each battle" + settings.end,
		"deck"      : GishkiDeck,
		"deckName"  : "Gishki",
		"deckDesc"  : "Attack Boosts / Battling",
		"voicelines": []
	}

	HeraldPlayer = {
		"name"      : "Arch Priest Xero",
		"desc"      : "      " + settings.darkcyan + "A high ranking official within a church he is devoted to. His deck aims to  restore his own life and gain power as he does so" + settings.end,
		"deck"      : HeraldDeck,
		"deckName"  : "Herald Agents",
		"deckDesc"  : "Benefitting in difference in Life Points",
		"voicelines": []
	}

	MagicianPlayer = {
		"name"      : "Dennis",
		"desc"      : "      " + settings.darkcyan + "A sidewalk performer with a nack of delivering a spectacle. his deck focuses on defending himself until his best magician is ready" + settings.end,
		"deck"      : MagicianDeck,
		"deckName"  : "Magicians",
		"deckDesc"  : "Defending / Summoning Dark Magician",
		"voicelines": []
	}

	StormPlayer = {
		"name"      : "Ventus",
		"desc"      : "      " + settings.darkcyan + "A professional Speed Duelist who like to ride the wind on his hoverboard. His deck focuses on swarming Riders which power up his Stormbirds" + settings.end,
		"deck"      : StormDeck,
		"deckName"  : "Stormriders",
		"deckDesc"  : "Swarming / Stealing Monsters",
		"voicelines": []
	}

	FirePlayer = {
		"name"      : "Soulburner",
		"desc"      : "      " + settings.darkcyan + "A professional Speed Duelist with an explosive attitude. Isn't afraid to destroy his own monsters to burn his opponents down" + settings.end,
		"deck"      : FireDeck,
		"deckName"  : "Fire Kings/Fists",
		"deckDesc"  : "Self Destruction / Fire Formations",
		"voicelines": []
	}

	JunglePlayer = {
		"name": "Karliah",
		"desc": "      " + settings.darkcyan + "A Duelist with a Wild side. She has a mismatch of cards that will protect her no matter what" + settings.end,
		"deck": JungleDeck,
		"deckName": "Jungle Beasts",
		"deckDesc": "Protecting Karliah / Granting Effects",
		"voicelines": []
	}

	PlayerList.append(CyberPlayer)
	PlayerList.append(VampirePlayer)
	PlayerList.append(GishkiPlayer)
	PlayerList.append(HeraldPlayer)
	PlayerList.append(MagicianPlayer)
	PlayerList.append(StormPlayer)
	PlayerList.append(FirePlayer)
	PlayerList.append(JunglePlayer)

	# Get the user's chosen Player
	while True:

		print("--------------------------------------")
		print("Player Select:")

		maxPlayerName = findDictLength(PlayerList, "name")
		maxDeckName = findDictLength(PlayerList, "deckName")

		maxDeckDesc = findDictLength(PlayerList, "deckDesc")

		i = 0
		for player in PlayerList:
			print("[{}] Name: {} | Deck: {} | Theme: {}".format(i + 1, player.get("name").ljust(maxPlayerName, ),
			                                                    player.get("deckName").ljust(maxDeckName, ),
			                                                    player.get("deckDesc").ljust(maxDeckDesc, )))
			i = i + 1

		selection = input("~~Please Select a character:")

		try:
			selection = int(selection) - 1

			if selection < 0:
				print("--------------------------------------")
				print("Invalid Selection")
				continue

			_player.name = PlayerList[selection].get("name")
			_player.deck = PlayerList[selection].get("deck")

			print("--------------------------------------")
			print("You have selected {} as your player character".format(_player.name))
			print(settings.darkcyan + "{}".format(PlayerList[selection].get("desc")) + settings.end)

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

	print("\n" * 100)

	# Get the user's chosen Opponent
	while True:
		print("--------------------------------------")
		print("Opponent Select:")

		maxPlayerName = findDictLength(PlayerList, "name")
		maxDeckName = findDictLength(PlayerList, "deckName")

		maxDeckDesc = findDictLength(PlayerList, "deckDesc")

		i = 0
		for opponent in PlayerList:
			print("[{}] Name: {} | Deck: {} | Theme: {}".format(i + 1, opponent.get("name").ljust(maxPlayerName, ),
			                                                    opponent.get("deckName").ljust(maxDeckName, ),
			                                                    opponent.get("deckDesc").ljust(maxDeckDesc, )))
			i = i + 1

		selection = input("~~Please Select a character to play against:")

		try:
			selection = int(selection) - 1

			if selection < 0:
				print("--------------------------------------")
				print("Invalid Selection")
				continue

			_foe.name = PlayerList[selection].get("name")
			_foe.deck = PlayerList[selection].get("deck")

			print("--------------------------------------")
			print("You have selected {} as your opposition character".format(_foe.name))

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

	print("\n" * 100)

# Prints Deck List before they are assigned to a player
def printDeckList(DeckList: list):
	print("Deck List:")

	tempList = []

	if DeckList.__len__() != 0:
		i = 0

		#  Create a list with only one instance of each card
		for monster in DeckList:
			existing = False
			for monsterTemp in tempList:
				if monster.name == monsterTemp.name:
					existing = True
					continue

			if existing:
				continue
			else:
				tempList.append(monster)


		max_len = _player.getMaxLength(DeckList)

		for monster in tempList:
			if i >= 9:
				print(settings.green + "[{}] {}x {} | ATK: {} | Tributes: {} ".format((i + 1), countInstances(DeckList, monster) , monster.name.ljust(max_len, ), str(monster.atkPoints).ljust(4, ), monster.tribute) + settings.end +  settings.darkcyan + "| Effect: {}".format(monster.effectText) + settings.end)
			else:
				print(settings.green + "[{}]  {}x {} | ATK: {} | Tributes: {} ".format((i + 1), countInstances(DeckList, monster) , monster.name.ljust(max_len, ), str(monster.atkPoints).ljust(4, ), monster.tribute) + settings.end +  settings.darkcyan + "| Effect: {}".format(monster.effectText) + settings.end)
			i = i + 1

	input("Press Enter to Continue...")

	return

def countInstances(array: list, monster: card):
	i = 0

	for entry in array:
		if entry.name == monster.name:
			i = i + 1

	return i

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

# Reset Gamestate
def reset():

	print("Resetting Gamestate: ")
	_player.monfield = []
	_foe.monfield = []

	_player.gy = []
	_foe.gy = []

	_player.hand = []
	_foe.hand = []



	_player.lifepoints = 8000
	_foe.lifepoints = 8000

	global turnCount
	turnCount = 0

	global firstTurn
	firstTurn = 0

	resetNormalSummon()

	print("\n" * 100)

	pass

# Method to contain the main menu and all its options
def mainMenu():
	reset()

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
				turnOrder = 0

				card_player_deck_setup()

				# Die Roll Loop
				while True:
					# Decide who is going first
					foe_roll = random.randint(1,6)

					override = input("Press enter to roll the dice to see who goes first:")
					if override == "f":
						turnOrder = 1
						break

					print("\n" * 100)
					print("Rolling.")
					time.sleep(0.75)
					print("\n" * 100)
					print("Rolling..")
					time.sleep(0.75)
					print("\n" * 100)
					print("Rolling...")
					time.sleep(0.75)
					print("\n" * 100)

					player_roll = random.randint(1,6)

					print("{}'s Roll: {}".format(_foe.name, foe_roll))
					print("Your Roll: {}".format(player_roll))
					print("--------------------------------------")

					if player_roll > foe_roll:
						while True:
							print("[1] First")
							print("[2] Second")
							selection = input("~~You won the die roll, will you go first or second: ")

							try:
								selection = int(selection)
							except TypeError:
								pass

							try:
								if selection == 1:
									print("You chose to go First")
									turnOrder = 1  # Sets the turn counter to make the player go first
									break
								elif selection == 2:
									print("You chose to go Second")
									turnOrder = 2 # Sets the turn counter to make the opponent go first
									break
								else:
									print("--------------------------------------")
									print("Invalid Selection")
									continue
							except (TypeError, ValueError):
								print("--------------------------------------")
								print("Invalid Selection")
								continue
					elif player_roll < foe_roll:

						foe_roll = random.randint(1,2)
						if foe_roll == 1:
							print("You lost the die roll, the opponent will go first")
							turnOrder = 2
							break
						elif foe_roll == 2:
							print("You lost the die roll, the opponent will go second")
							turnOrder = 1
							break
					elif player_roll == foe_roll:
						print("Tie result, roll again")
						continue

					if turnOrder:
						break

				time.sleep(1)

				print("\n" * 100)

				print("--------------------------------------")
				print("Duel Begin")
				time.sleep(1)

				# -- Main loop from which the duels run --
				while True:
					if turnOrder == 2:
						exitProg = turnMenu(_foe, _player)
						turnOrder = 1
					elif turnOrder == 1:
						exitProg = turnMenu(_player, _foe)
						turnOrder = 2
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

				card_player_deck_setup()

				_player.draw(4)
				_foe.draw(4)

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
	except (IndexError, AttributeError):
		pass
	try:
		for monster in passivePlayer.monfield:
			monster.attacked = 0
	except (IndexError, AttributeError):
		pass

	# resetting attacked values in graveyard

	try:
		for monster in currentPlayer.gy:
			monster.attacked = 0
	except (IndexError, AttributeError):
		pass

	try:
		for monster in passivePlayer.gy:
			monster.attacked = 0
	except (IndexError, AttributeError):
		pass

	# Retrieve the global variables and set up rest of needed variables
	global turnCount
	global firstTurn
	global destination
	destination = ""

	resetNormalSummon()

	resetEffectChecker()

	# Move the turn count and announce the turn
	turnCount = turnCount + 1
	print("--------------------------------------")
	print("Turn {}: {}'s Turn".format(turnCount, currentPlayer.name))

	time.sleep(0.7)

	# DRAW PHASE
	if firstTurn == 0:
		currentPlayer.draw(4)
		# currentPlayer.draw(0)

		## NAVI: Placeholder to move to Card Add
		# -------------vv-Add Cards here to Test-vv---------------------------------------------------------------------
		# -------------vv-Add Cards here to Test-vv---------------------------------------------------------------------
		# -------------vv-Add Cards here to Test-vv---------------------------------------------------------------------
		# -------------vv-Add Cards here to Test-vv---------------------------------------------------------------------
		# _player.hand.append()
		# _player.gy.append()
		# _foe.hand.append()
		# _foe.monfield.append(jungleTravellerKarliah)
		# _foe.gy.append()
		# -------------^^-Add Cards here to Test-^^---------------------------------------------------------------------
		# -------------^^-Add Cards here to Test-^^---------------------------------------------------------------------
		# -------------^^-Add Cards here to Test-^^---------------------------------------------------------------------
		# -------------^^-Add Cards here to Test-^^---------------------------------------------------------------------
		# -------------^^-Add Cards here to Test-^^---------------------------------------------------------------------

		passivePlayer.draw(3)

	else:
		currentPlayer.draw(1)

	# Print current field status
	print("--------------------------------------")
	currentPlayer.checkField()

	# STANDBY PHASE
	settings.resolveStandbyEffects(currentPlayer, passivePlayer)

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

			print("[6] Attack with a Monster")

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

					tributedCard.ResolveEffect(effTrigger.graveyard, currentPlayer, passivePlayer, tributedCard,
							                    None, currentPlayer.gy, passivePlayer.gy, currentPlayer)

				# Check if the monster has an on-summon effect effect, and activate it if it hasn't used it yet
				playedCard.ResolveEffect(effTrigger.summon, currentPlayer, passivePlayer, playedCard,
				                           None, currentPlayer.gy, passivePlayer.gy, currentPlayer)

		elif selection == 2:  # [2] Check Hand
			currentPlayer.checkHand()
			pass

		elif selection == 3:  # [3] Check Field
			print("{}'s Field:".format(currentPlayer.name))
			currentPlayer.checkField()
			print("{}'s Field:".format(passivePlayer.name))
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

		# Reset atk in grave
		for monster in currentPlayer.gy:
			monster.atkPoints = monster.origAtk

		for monster in passivePlayer.gy:
			monster.atkPoints = monster.origAtk

		if firstTurn == 0:
			firstTurn = 1

		exitProg = "false"

		# Check hand size limit

		if currentPlayer.hand.__len__() > 6:
			while currentPlayer.hand.__len__() > 6:
				print("--------------------------------------")
				print("You have too many card in your hand ({}), the hand size limit is 6".format(currentPlayer.hand.__len__()))
				currentPlayer.effectdiscardCard(currentPlayer, passivePlayer, None, None, currentPlayer.gy, passivePlayer.gy, currentPlayer)

		print("\n" * 100)


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
						break
					else:
						print("--------------------------------------")
						print("Invalid Selection")
				except (ValueError, IndexError, TypeError):
					print("--------------------------------------")
					print("Invalid Selection")
					print("Group")

			# retrieve the user attack target
			if passivePlayer.monfield and passivePlayer.checkFieldDef():
				while True:

					# Replace with a Specific attack selection

					i = 0
					tempListNum = []
					print("{}s Field:".format(passivePlayer.name))

					max_len = passivePlayer.getMaxLength(passivePlayer.monfield)

					# Loop through the hand and display each card fitting the namespace
					for monster in passivePlayer.monfield:
						if monster.canBeAttacked:
							if i >= 9:
								print(settings.green + "[{}] {} | ATK: {} | Tributes: {} ".format((i + 1),
								                                                                  monster.name.ljust(
									                                                                  max_len, ),
								                                                                  str(
									                                                                  monster.atkPoints).ljust(
									                                                                  4, ),
								                                                                  monster.tribute) + settings.end + settings.darkcyan + "| Effect: {}".format(
									monster.effectText) + settings.end)
							else:
								print(settings.green + "[{}]  {} | ATK: {} | Tributes: {} ".format((i + 1),
								                                                                   monster.name.ljust(
									                                                                   max_len, ),
								                                                                   str(
									                                                                   monster.atkPoints).ljust(
									                                                                   4, ),
								                                                                   monster.tribute) + settings.end + settings.darkcyan + "| Effect: {}".format(
									monster.effectText) + settings.end)
							tempListNum.append(i)
						else:
							pass

						i = i + 1

					print("[0] Return")
					print("--------------------------------------")
					target = input("~~Please select a monster to attack:")


					try:
						target = int(target) - 1
					except (TypeError, IndexError, ValueError):
						pass

					try:
						if target == -1:
							return 1

						atkTarget = passivePlayer.monfield[target]

						if passivePlayer.checkArrayLoc(passivePlayer.monfield, atkTarget) in tempListNum:
							break
						else:
							print("--------------------------------------")
							print("Invalid Selection")
							print("--------------------------------------")
					except (IndexError, TypeError):
						print("--------------------------------------")
						print("Invalid Selection")
						print("--------------------------------------")

				damage = atkMon.atkPoints - atkTarget.atkPoints
			else:
				print("Direct Attack!")
				damage = atkMon.atkPoints
				atkTarget = None

			##TODO Fix logic here for damage calculation
			# Monster Effect: Attacker (Returns Damage)
			if atkMon.checkResolve(effTrigger.attack):
				damage = atkMon.ResolveEffect(effTrigger.attack, turnPlayer, passivePlayer, atkMon, atkTarget, turnPlayer.gy, passivePlayer.gy, turnPlayer)

			if atkMon.checkResolve(effTrigger.battle):
				damage = atkMon.ResolveEffect(effTrigger.battle, turnPlayer, passivePlayer, atkMon, atkTarget, turnPlayer.gy, passivePlayer.gy, turnPlayer)


			# Monster Effect: Defender (Returns Damage)
			try:
				if atkTarget.checkResolve(effTrigger.defend):
					damage = atkTarget.ResolveEffect(effTrigger.defend, passivePlayer, turnPlayer, atkTarget, atkMon, passivePlayer.gy, turnPlayer.gy, turnPlayer)

				if atkTarget.checkResolve(effTrigger.battle):
					damage = atkTarget.ResolveEffect(effTrigger.battle, passivePlayer, turnPlayer, atkTarget, atkMon, passivePlayer.gy, turnPlayer.gy, turnPlayer)
			except (AttributeError, TypeError, UnboundLocalError):
				pass

			if turnPlayer.lifepoints == 0 or passivePlayer.lifepoints == 0:
				break

			if damage is None:  # This occurs for effect returns that don't impact damage
				atkMon.attacked = 1

				try:
					damage = atkMon.atkPoints - atkTarget.atkPoints
				except (UnboundLocalError, AttributeError):
					damage = atkMon.atkPoints

			if damage == -1:
				atkMon.attacked = 1

				damage = 0

			if damage > 0:
				atkMon.attacked = 1

				passivePlayer.loseLP(damage)

				try:
					oppmonster = atkTarget
					if oppmonster.checkResolve(effTrigger.destructionBat) and returnEffectChecker(oppmonster, effTrigger.destructionBat):
						result = oppmonster.ResolveEffect(effTrigger.destructionBat, passivePlayer, turnPlayer, atkTarget, atkMon, passivePlayer.gy, turnPlayer.gy, turnPlayer)
						if result:
							pass
						else:
							result = 0

						if result == 0:
							passivePlayer.destroyMonsterBat(atkTarget, passivePlayer, turnPlayer, oppmonster, atkMon, passivePlayer.gy, turnPlayer.gy, turnPlayer)

							if atkMon.checkResolve(effTrigger.destroyBattle):
								atkMon.ResolveEffect(effTrigger.destroyBattle, turnPlayer, passivePlayer, atkMon, atkTarget, turnPlayer.gy, passivePlayer.gy, turnPlayer)

						else:
							pass
					else:
						passivePlayer.destroyMonsterBat(atkTarget, passivePlayer, turnPlayer, oppmonster, atkMon, passivePlayer.gy, turnPlayer.gy, turnPlayer)

						if atkMon.checkResolve(effTrigger.destroyBattle):
							atkMon.ResolveEffect(effTrigger.destroyBattle, turnPlayer, passivePlayer, atkMon, atkTarget, turnPlayer.gy, passivePlayer.gy, turnPlayer)
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

				if atkMon.checkResolve(effTrigger.destructionBat) and returnEffectChecker(atkMon, effTrigger.destructionBat):
					result = atkMon.ResolveEffect(effTrigger.destructionBat, turnPlayer, passivePlayer, atkMon, atkTarget, turnPlayer.gy, passivePlayer.gy, turnPlayer)

					if result == 0:
						turnPlayer.destroyMonsterBat(atkMon, turnPlayer, passivePlayer, atkMon, atkTarget, turnPlayer.gy, passivePlayer.gy, turnPlayer)
					else:
						pass
				else:
					turnPlayer.destroyMonsterBat(atkMon, turnPlayer, passivePlayer, atkMon, atkTarget, turnPlayer.gy, passivePlayer.gy, turnPlayer)
				time.sleep(1)

			elif damage == 0:
				atkMon.attacked = 1

				print("No Damage")

				# Check if the attack target is still on the field
				if atkTarget in passivePlayer.monfield:
					pass
				else:
					atkTarget = None

				# Check if the attacker is on the field
				if atkMon in turnPlayer.monfield:
					pass
				else:
					atkMon = None

				# destroy both monsters if they exist
				try:
					if atkMon and atkTarget:

						if atkTarget.checkResolve(effTrigger.destructionBat) and returnEffectChecker(atkTarget, effTrigger.destructionBat):
							result = atkTarget.ResolveEffect(effTrigger.destructionBat, passivePlayer, turnPlayer, atkTarget, atkMon, passivePlayer.gy, turnPlayer.gy, turnPlayer)

							if result == 0:
								passivePlayer.destroyMonsterBat(atkTarget, passivePlayer, turnPlayer , atkTarget, atkMon, turnPlayer.gy, passivePlayer.gy, turnPlayer)
							else:
								pass
						else:
							passivePlayer.destroyMonsterBat(atkTarget, passivePlayer, turnPlayer , atkTarget, atkMon, turnPlayer.gy, passivePlayer.gy, turnPlayer)

						if atkMon.checkResolve(effTrigger.destructionBat) and returnEffectChecker(atkMon, effTrigger.destructionBat):
							result = atkMon.ResolveEffect(effTrigger.destructionBat, turnPlayer, passivePlayer, atkMon, atkTarget, turnPlayer.gy, passivePlayer.gy, turnPlayer)

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
