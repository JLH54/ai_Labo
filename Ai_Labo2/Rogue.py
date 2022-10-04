import sys
from Ennemies import ennemies
from PlayerClasses import playerClasses

class Rogue(playerClasses):
    Invisibily:bool
    daggers:int
    AsUsedInvisibility:bool
    multiplier:int

    def RogueChoice(self):
        print("hp : " + str(self.HealthPoints))
        print("1 : dagger strike(deals 6 damage to 1 target)")
        print("2 : throw dagger(deals 2x the damage of the strike)")
        if(self.AsUsedInvisibility == True):
            print("3 : Becomes invisible(do 2x times damage to the target(stacks))")
            print("    the invisibility wears off after the attack(usable 1 once per fight)")
        print("4 : Run away like a coward")
        inGameChoice = input("")
        while(True):
            if(self.AsUsedInvisibility == True and int(inGameChoice) == 3):
                print("You have already used it, you can't even see the option >:(")
                self.RogueChoice()
            elif(self.AsUsedInvisibility == False):
                if(int(inGameChoice) != 1 and int(inGameChoice) != 2 and int(inGameChoice) != 3 and int(inGameChoice) != 4):
                    print("You have to make a choice")
            else:
                return int(inGameChoice)

    def Action(self, ennemis):
        playerChoice = self.RogueChoice()
        self.multiplier = 1
        if(self.Invisibily == True):
            self.multiplier *= 2
        if(playerChoice == 1):
            for i in range(len(ennemis)):
                if(ennemis[i].returnDead() == False):
                    ennemis[i].TakeDamage(self.AttackPoint * self.multiplier, ennemis[i].ReturnProtect())
                    print(ennemis[i].CarachterName + " has taken the hit")
                    self.Invisibily = False
                    self.protected = False
                break
            return False
        elif(playerChoice == 2):
            self.multiplier *= 2
            for i in range(len(ennemis)):
                if(ennemis[i].returnDead() == False):
                    ennemis[i].TakeDamage(self.AttackPoint * self.multiplier, ennemis[i].ReturnProtect())
                    print(ennemis[i].CarachterName + " has taken the hit")
                    self.Invisibily = False
                    self.protected = False
                break
            return False
        elif(playerChoice == 3 and self.AsUsedInvisibility == False):
            self.Invisibily = True
            self.AsUsedInvisibility = True
            self.protected = True
            return False
        elif(playerChoice == 5):
            return True

    def __init__(self, name, PlayerChoice):
        super().__init__(name, PlayerChoice)
        self.HealthPoints = 50
        self.AttackPoint = 12
        self.Invisibily = False