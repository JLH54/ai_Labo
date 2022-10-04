import sys
from Actor import actor

class ennemies(actor):
    difficulty:int
    className:str
    def __init__(self, name, level):
        super().__init__(name)
        self.difficulty = level
        self.dead = False

    def returnDead(self):
        return self.dead

    
    