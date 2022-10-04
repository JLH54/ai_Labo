import sys
from Actor import actor

class playerClasses(actor):
    def __init__(self, name, PlayerChoice):
        super().__init__(name)
        self.ClassName = PlayerChoice
    ClassName:int
    Purse:int
    Fame:int
    class_id:int