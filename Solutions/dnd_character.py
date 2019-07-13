import random


class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()

        self.hitpoints = 10 + modifier(self.constitution)

    @staticmethod
    def ability():
        rolls = []
        diceroll = random.randint(1, 6)
        for i in range(4):
            rolls.append(diceroll)
        rolls.remove(min(rolls))
        return sum(rolls)


def modifier(stat):
    if stat <= 3:
        return -4
    elif 6 > stat >= 4:
        return -3
    elif 8 > stat >= 6:
        return -2
    elif 10 > stat >= 8:
        return -1
    elif 12 > stat >= 10:
        return 0
    elif 14 > stat >= 12:
        return 1
    elif 16 > stat >= 14:
        return 2
    elif 18 > stat >= 16:
        return 3
    elif stat >= 18:
        return 4