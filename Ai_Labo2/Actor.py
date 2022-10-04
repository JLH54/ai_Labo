import sys
import random

class actor:
    def __init__(self, name): 
        self.CarachterName = name
    CarachterName:str
    HealthPoints:int
    AttackPoint:int
    protected:bool
    dead:bool

    def TakeDamage(self, damage, protected):
        if(protected == False):
            self.HealthPoints -= damage
            if(self.HealthPoints <=0):
                self.dead = True
                self.HealthPoints = 0
    
    def ReturnProtect(self):
        return self.protected
