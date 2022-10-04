import sys
from Ennemies import ennemies
from PlayerClasses import playerClasses

class Knight(playerClasses):
    ArmorPoint:int
    IsArmed:bool
    ThrowWeaponPoint:int

    def KnightChoice(self):
        print("hp : " + str(self.HealthPoints))
        print("1 : Sword Swipe(deals 6 damage to 1 target)")
        print("2 : Raise your shield(you get no damage from ennemies)")
        print("3 : Run away like a coward")
        inGameChoice = input("")
        while(True):
            if(int(inGameChoice) != 1 and int(inGameChoice) == 2 and int(inGameChoice) == 3 and int(inGameChoice) == 4):
                print("You have to make a choice")
            else:
                return int(inGameChoice)

    def Action(self, ennemis):
        playerChoice = self.KnightChoice()
        if(playerChoice == 1):
            for i in range(len(ennemis)):
                if(ennemis[i].returnDead() == False):
                    ennemis[i].TakeDamage(self.AttackPoint, ennemis[i].ReturnProtect())
                    print(ennemis[i].CarachterName + " has taken the hit")
                break
            return False
        elif(playerChoice == 2):
            self.protected = True
        elif(playerChoice == 3):
            return True

    def __init__(self, name, PlayerChoice):
        super().__init__(name, PlayerChoice)
        self.HealthPoints = 50
        self.AttackPoint = 8