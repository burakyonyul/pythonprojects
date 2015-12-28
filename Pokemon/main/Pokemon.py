import random


class Pokemon(object):
    def __init__(self, name, type, level=1, healthFactor=100, skills=[], state="active"):
        self.name = name
        self.type = type
        self.level = level
        self.health = healthFactor * level
        self.skills = skills
        self.state = state

    def __str__(self):
        return "name: %s, type: %s, level: %d, health: %d, skills: %s, state: %s" % (
            self.name, self.type, self.level, self.health, map(str, self.skills), self.state)

    def attack(self, targetPokemon, skill):
        if skill not in self.skills:
            return
        else:
            escaped = targetPokemon.defend(self, skill)
            if not escaped:
                damage = self.calculateMultiplication(skill, targetPokemon) * self.level * skill.power
                targetPokemon.hitHealth(damage)
                print "%s inflicted %d damage with %s attack to %s" % (self.name, damage, skill, targetPokemon.name)
                if targetPokemon.health <= 0:
                    targetPokemon.makePassive()
                    print "%s is unable to battle" % (targetPokemon.name)
            else:
                print "%s escaped from attack: %s" % (targetPokemon.name, skill)

    def calculateMultiplication(self, skill, targetPokemon):
        multiplicationFactor = 1
        if skill.weakerThan(targetPokemon.type):
            multiplicationFactor = 0.5
        elif skill.strongerThan(targetPokemon.type):
            multiplicationFactor = 1.5
        return multiplicationFactor

    def defend(self, attackingPokemon, skill):
        randomValue = random.randint(0, self.level)
        if skill.power * attackingPokemon.level < randomValue * self.level:
            return True

        return False

    def makePassive(self):
        self.state = "passive"
        return

    def hitHealth(self, hitValue):
        if hitValue <= self.health:
            self.health -= hitValue
        else:
            self.health = 0
        return


class Skill(object):
    def __init__(self, name, type, power):
        self.name = name
        self.type = type
        self.power = power

    def strongerThan(self, type):
        return type.name in self.type.strongnesses

    def weakerThan(self, type):
        return type.name in self.type.weaknesses

    def __str__(self):
        return "skillname: %s, skilltype: %s" % (self.name, self.type)


class Type(object):
    def __init__(self, name, weaknesses=(), strongnesses=()):
        self.name = name
        self.weaknesses = weaknesses
        self.strongnesses = strongnesses

    def __str__(self):
        return "%s, weakness: %s, strongness: %s" % (self.name, self.weaknesses, self.strongnesses)
