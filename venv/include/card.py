from enum import Enum
from effect import *


class card:
    def __init__(self, name, atkPoints, tribute=0, cardEffect: object = [],
                 trigger=effTrigger.n_a, effectText="N/A", attacked=0):
        # Parameters
        self.name = name
        self.atkPoints = atkPoints
        self.effect = cardEffect
        self.trigger = trigger
        self.effectText = effectText
        self.attacked = attacked
        self.tribute = tribute
        self.origAtk = atkPoints
