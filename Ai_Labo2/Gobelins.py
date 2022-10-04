import sys
from Ennemies import ennemies
import random

class Gobelins(ennemies): 
    Weapon:str
    HasShield:bool
    ShieldPoints:int

    def Shielded(self, HasShield):
        if HasShield:
            ShieldPoints = 5 * self.difficulty
        else:
            ShieldPoints = 0

    def behaviour(self, player):
        self.protected = False
        actionDecider = random.randrange(0,101)
        if(self.dead == False):
            if(actionDecider >= 0 and actionDecider <= 60):
                self.goblinAttack(player)
            elif(actionDecider >= 61 and actionDecider <= 80):
                self.goblinProtect()
            elif(actionDecider >= 81 and actionDecider <= 100):
                print(self.CarachterName + " is laughing at you")

    def goblinAttack(self, player):
        if(player.ReturnProtect() == True):
            print(self.CarachterName +" tried to attack you")
        else:
            player.TakeDamage(self.AttackPoint, player.ReturnProtect())
            print(self.CarachterName +" attacked you and did " + str(self.AttackPoint) + " damage")

    def goblinProtect(self):
        self.protected = True
        print(self.CarachterName + " decided to protect himself")

    def __init__(self, name, level):
        super().__init__(name, level)
        self.HealthPoints = 3 * level
        self.AttackPoint = random.randrange(1,4)
        self.className = "Gobelin"
        self.protected = False