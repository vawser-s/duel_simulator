import time
import random
from enum import Enum
from settings import *


class effTrigger(Enum):
    n_a = 1
    summon = 2
    battle = 3
    graveyard = 4
    destructionBat = 5
    destructionEff = 6


class effect:
    def __init__(self, desc, extraParam):
        self.desc = desc
        self.extraParam = extraParam

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

            if oppMon.trigger.name == "destructionEff":
                eff = oppMon.effect.resolve(effplayer, opponent, oppMon, effectMon, effgy, oppgy, turnPlayer)

                if eff == 0:
                    opponent.destroyMonsterEff(oppMon, effplayer, opponent, oppMon, effectMon, effgy, oppgy, turnPlayer)
                else:
                    pass
            else:
                opponent.destroyMonsterEff(oppMon, effplayer, opponent, oppMon, effectMon, effgy, oppgy, turnPlayer)
        else:
                print("No Opponent monster to destroy")
                return
        return 0


class effectDamage(effect):
    def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
        print("{}'s Effect Activates!".format(effectMon.name))
        print("--------------------------------------")
        time.sleep(1)

        opponent.loseLP(self.extraParam)


class effectDamageSelf(effect):
    def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
        print("{}'s Effect Activates!".format(effectMon.name))
        print("--------------------------------------")
        time.sleep(1)

        effplayer.loseLP(self.extraParam)


class effectRestore(effect):
    def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
        print("{}'s Effect Activates!".format(effectMon.name))
        print("--------------------------------------")
        time.sleep(1)

        effplayer.gainLP(self.extraParam)


class effectCrash(effect):
    def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
        print("{}'s Effect Activates!".format(effectMon.name))
        print("--------------------------------------")
        time.sleep(1)

        print("{} Copies the opponents attack!".format(effectMon.name))

        time.sleep(0.5)

        return 0


class playerDraw(effect):
    def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
        print("{}'s Effect Activates!".format(effectMon.name))
        print("--------------------------------------")
        time.sleep(1)
        effplayer.draw(self.extraParam)


class siphonLife(effect):
    def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
        print("{}'s Effect Activates!".format(effectMon.name))
        print("--------------------------------------")
        time.sleep(1)

        opponent.loseLP(self.extraParam)
        effplayer.gainLP(self.extraParam)


class effectPlayerDiscard(effect):
    def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
        print("{}'s Effect Activates!".format(effectMon.name))
        print("--------------------------------------")
        time.sleep(1)

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
                if self.hand.__len__() == 0:
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
                if self.hand.__len__() == 0:
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

        effplayer.searchSpecificDeck(self.extraParam)


class extraNormalSummon(effect):
    def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
        print("{}'s Effect Activates!".format(effectMon.name))
        print("--------------------------------------")
        time.sleep(1)

        print("You get one extra normal summon")

        resetNormalSummon()


class gainAttack(effect):
    def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
        print("{}'s Effect Activates!".format(effectMon.name))
        print("--------------------------------------")
        time.sleep(1)

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
                print("No Opponent monster to destroy")
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

                effplayer.sendToGrave(monster)

                return
            elif selection == "N" or selection == "n":
                return


class specialHand(effect):
    def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
        print("{}'s Effect Activates!".format(effectMon.name))
        print("--------------------------------------")
        time.sleep(1)

        effplayer.specialHandEffect(effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer)


class specialSpecificHand(effect):
    def resolve(self, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer):
        print("{}'s Effect Activates!".format(effectMon.name))
        print("--------------------------------------")
        time.sleep(1)

        effplayer.specialHandSpecific(self.extraParam, effplayer, opponent, effectMon, oppMon, effgy, oppgy, turnPlayer)


# Define the effects used
PlayerDraw1 = playerDraw("Draw One Card", 1)
PlayerDraw2 = playerDraw("Draw Two Cards", 2)
Destroy = effectDestroy("Destroy Your Opponents Monster", 0)
Restore1000 = effectRestore("Restore Life Points by 1000", 1000)
Restore2000 = effectRestore("Restore Life Points by 2000", 2000)
Damage1000 = effectDamage("Damage Opponent by 1000", 1000)
DamageSelf = effectDamageSelf("Damage Player by 1000", 1000)
SiphonLife800 = siphonLife("Steal 800 Life points from opponent", 800)
SiphonLife1500 = siphonLife("Steal 1500 Life points from opponent", 1500)
playerDisc1 = effectPlayerDiscard("Player discards One Card", 1)
oppDisc1 = effectOpponentDiscard("Opponent Discards One Card", 1)
oppDisc2 = effectOpponentDiscard("Opponent Discards Two Cards", 2)
matchAttack = effectCrash("Copies Opponents Monsters Attack", 0)
battleImmune = noBattleDestruction("Cannot be Destroyed by Battle", 0)
effectImmune = noEffectDestruction("Cannot be Destroyed by Effects", 0)
effectSearch = searchDeck("Add a card from Deck to Hand", 0)
effectCodeSearch = searchSpecificDeck("Add a 'Code' card from Deck to hand", "Code")
effectVampSearch = searchSpecificDeck("Add a 'Vampire' card from Deck to hand", "Vampire")
effectHeraldSearch = searchSpecificDeck("Add a 'Herald' card from Deck to hand", "Herald")
effectAgentSearch = searchSpecificDeck("Add a 'Agent' card from Deck to hand", "Agent")
effectGishkiSearch = searchSpecificDeck("Add a 'Gishki' card from Deck to hand", "Gishki")
effectEvigishkiSearch = searchSpecificDeck("Add an 'Evigishki' card from Deck to hand", "Evigishki")
effectGishkiMirrorSearch = searchSpecificDeck("Add a 'Gishki Aquamirror' card from Deck to hand", "Gishki Aquamirror")
doubleSummon = extraNormalSummon("Gain an extra normal summon", 0)
gain500 = gainAttack("Gains 500 attack before battle. Loses attack upon destruction", 500)
gain1000 = gainAttack("Gains 1000 attack before battle. Loses attack upon destruction", 1000)
bounceMonster = fieldToHand("Bounce an Opponents Monster", 0)
GYToHand = gyToHand("Return a card from your Graveyard to your Hand", 0)
Trib_SS_GY = tributeTOSSGy("you can Tribute this card: Special Summon a monster from the Graveyard", 0)
specialAgentHand = specialSpecificHand("Special Summon an 'Agent' Monster from your hand", "Agent")
specialCyberseHand = specialSpecificHand("Special Summon a 'Cyberse' Monster from your hand", "Cyberse")
specialVampireHand = specialSpecificHand("Special Summon a 'Vampire' Monster from your hand", "Vampire")
specialGishkiHand = specialSpecificHand("Special Summon a 'Gishki' Monster from your hand", "Gishki")
gainDifference = gainAttackDifference("Gain Atk Points equal to the difference between your lifepoints", 0)
specialfromHand = specialHand("Special Summon a monster from your hand", 0)

