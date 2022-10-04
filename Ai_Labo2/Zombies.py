import sys
from Ennemies import ennemies
import random

class Zombies(ennemies):
    HordeMultiplier:bool
    DamageDeMultiplier:int
    MaxHealthPoints:int

    def IsItInAHorde(self, numbersOfZombiesAround):
        if(numbersOfZombiesAround >= 3):
            HordeMultiplier = True
        else:
            HordeMultiplier = False

    def Decapitated(self):
        AttackPoint = AttackPoint - ((self.MaxHealthPoints - self.HealthPoints  / 2))

    def behaviour(self, player):
        self.protected = False
        actionDecider = random.randrange(0,101)
        if(self.dead == False):
            if(actionDecider >= 0 and actionDecider <= 50):
                self.zombieAttack(player)
            elif(actionDecider >= 51 and actionDecider <= 100):
                print(self.CarachterName + " is looking at you")

    def zombieAttack(self, player):
        if(player.ReturnProtect() == True):
            print(self.CarachterName +" tried to attack you")
        else:
            player.TakeDamage(self.AttackPoint, player.ReturnProtect())
            print(self.CarachterName +" attacked you and did " + str(self.AttackPoint) + " damage")
    
    def __init__(self, name, level):
        super().__init__(name, level)
        self.AttackPoint = 2
        self.HealthPoints = 8
        self.MaxHealthPoints = self.HealthPoints
        self.protected = False