import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health = self.health - damage
        pass


class Viking(Soldier):
    def __init__(self, name, health, strength):
        super(Viking, self).__init__(health, strength)
        self.name = name

    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return ("{} has received {} points of damage".format(self.name, damage))
        else:
            return ("{} has died in act of combat".format(self.name))

    def battleCry(self):
        return ("Odin Owns You All!")


class Saxon(Soldier):
    def __init__(self, health, strength):
        super(Saxon, self).__init__(health, strength)
        pass

    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return ("A Saxon has received {} points of damage".format(damage))
        else:
            return ("A Saxon has died in combat")


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, vikingo):
        self.vikingArmy.append(vikingo)

    def addSaxon(self, sajon):
        self.saxonArmy.append(sajon)

    def vikingAttack(self):
        sa = random.choice(self.saxonArmy)
        vi = random.choice(self.vikingArmy)
        sas = sa.receiveDamage(vi.attack())
        if sa.health <= 0:
            self.saxonArmy.remove(sa)
        return sas

    def saxonAttack(self):
        sa = random.choice(self.saxonArmy)
        vi = random.choice(self.vikingArmy)
        viv = vi.receiveDamage(sa.attack())
        if vi.health <= 0:
            self.vikingArmy.remove(vi)
        return viv

    def showStatus(self):
        if len(self.saxonArmy) and len(self.vikingArmy) > 0:
            return "Vikings and Saxons are still in the thick of battle."
        elif self.saxonArmy == []:
            return "Vikings have won the war of the century!"
        elif self.vikingArmy == []:
            return "Saxons have fought for their lives and survive another day..."
