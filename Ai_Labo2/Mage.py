import sys
from Ennemies import ennemies
from PlayerClasses import playerClasses

class Mage(playerClasses):
    Mana:int
    protected = False
    FireBallDamage:int
    incenerateDamage:int
    stickDamage:int
    
    #fireball can only target 1 person
    #Incinerate targets all ennemies
    def MageChoice(self):
        print("hp : " + str(self.HealthPoints))
        print("1 : Fire ball(deals 5 damage to 1 target)")
        print("2 : Incinerate(deals 3 damage to everyone)")
        print("3 : Use your stick as a blundge weapon(deals 3 damage to 1 target)")
        print("3 : Protect yourself")
        print("4 : Run away like a coward")
        inGameChoice = input("")
        while(True):
            if(int(inGameChoice) != 1 and int(inGameChoice) == 2 and int(inGameChoice) == 3 and int(inGameChoice) == 4):
                print("You have to make a choice")
            else:
                return int(inGameChoice)

    def Action(self, ennemis):
        playerChoice = self.MageChoice()
        if(playerChoice == 1):
            for i in range(len(ennemis)):
                if(ennemis[i].returnDead() == False):
                    ennemis[i].TakeDamage(self.FireBallDamage, ennemis[i].ReturnProtect())
                    print(ennemis[i].CarachterName + " has taken the hit")
                break
            return False
        elif(playerChoice == 2):
            for i in range(len(ennemis)):
                if(ennemis[i].returnDead() == False):
                    ennemis[i].TakeDamage(self.incenerateDamage, ennemis[i].ReturnProtect())
                    print(str(len(ennemis)) + " goblins took some damages")
            return False
        elif(playerChoice == 3):
            for i in range(len(ennemis)):
                if(ennemis[i].returnDead() == False):
                    ennemis[i].TakeDamage(self.stickDamage, ennemis[i].ReturnProtect())
                    print(ennemis[i].CarachterName + " has taken the hit")
                break
            return False
        elif(playerChoice == 4):
            self.protected = True
            return False
        elif(playerChoice == 5):
            return True

    def __init__(self, name, PlayerChoice):
        super().__init__(name, PlayerChoice)
        self.HealthPoints = 50
        self.FireBallDamage = 5
        self.incenerateDamage = 3
        self.stickDamage = 3