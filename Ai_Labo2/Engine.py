import random
import sys
from PlayerClasses import playerClasses
from Rogue import Rogue
from Knight import Knight
from Mage import Mage
from Gobelins import Gobelins
from Troll import Troll
from Zombies import Zombies

class engine():
    player:playerClasses
    ForestTaken = False
    SwampTaken = False
    CaveTaken = False

    def GameStarted(self):
        inGame = 1
        while(inGame == 1):
            print("Welcome to my rpg!")
            print("1 : start game")
            print("2 : close game")
            inGameChoice = input("")
            if (int(inGameChoice) == 1):
                return 1
            elif (int(inGameChoice) != 1):
                return 0  

    def PlayerChoice(self):
        print("What is your name?")
        Player_Name = input("")
        print("Choose your class:\n")
        print("1 : Knight\n")
        print("2 : Mage\n")
        print("3 : Rogue\n")
        inGameChoice = input("") 
        if (int(inGameChoice) == 1):
            self.player = Knight(Player_Name, int(inGameChoice))
        elif (int(inGameChoice) == 2):
            self.player = Mage(Player_Name, int(inGameChoice))
        elif(int(inGameChoice) == 3):
            self.player = Rogue(Player_Name, int(inGameChoice))
        elif(int(inGameChoice) != 1 or int(inGameChoice) != 2 or int(inGameChoice) != 3):
            print("You have made no choice")
            inGameChoice = self.PlayerChoice()

    def PlayerChooseThePlace(self):
        print("The king needs you to clean those places")
        while(True):
            if(self.ForestTaken == False):
                print("1 : forest of goblins")
            if(self.SwampTaken == False):
                print("2 : swamp of zombies")
            if(self.CaveTaken == False):
                print("3 : cave of trolls")
            inGameChoice = input("")
            if(int(inGameChoice) ==1):
                if(self.ForestTaken == True):
                    print("You have already been there it's clean")
                else:
                    self.ForestTaken = True
                    return 1
            if(int(inGameChoice) ==2):
                if(self.SwampTaken == True):
                    print("You have already been there it's clean")
                else:
                    self.SwampTaken = True
                    return 2
            if(int(inGameChoice) == 3):
                if(self.CaveTaken == True):
                    print("You have already been there it's clean")
                else:
                    self.CaveTaken = True
                    return 3

    def PlaceChosen(self, level):
        place_chosen = self.PlayerChooseThePlace()
        if(place_chosen == 1):
            how_many_goblins = random.randrange(2,3)
            goblins = []
            for i in range(how_many_goblins):
                goblin = Gobelins("Goblin" + str(i), level)
                goblins.append(goblin)
            return goblins
        if(place_chosen == 2):
            how_many_zombies = random.randrange(1,4 * level)
            zombies = []
            for i in range(how_many_zombies):
                zombie = Zombies("Zombie" + str(i), level)
                zombies.append(zombie)
            return zombies
        if(place_chosen == 3):
            how_many_trolls = random.randrange(1,2)
            trolls = []
            for i in range(how_many_trolls):
                troll = Troll("Troll" + str(i), level)
                trolls.append(troll)
            return trolls
            
    def TurnBaseCombat(self, ennemis):
        isOn = True
        numbersOfDeath = 0
        while(isOn):
            didThePlayerRan = self.player.Action(ennemis)
            # if(self.player.ClassName == 1):
            #     didThePlayerRan = self.player.MageAction(ennemis)
            # elif(self.player.ClassName == 2):
            #     didThePlayerRan = self.player.MageAction(ennemis)
            # elif(self.player.ClassName == 3):
            #     didThePlayerRan = self.player.MageAction(ennemis)
            if(didThePlayerRan == True):
                self.PlayerRan()
                isOn = False
            for i in range(len(ennemis)):
                if(ennemis[i].returnDead() == True):
                    numbersOfDeath += 1
                ennemis[i].behaviour(self.player)
            if(numbersOfDeath == len(ennemis)):
                print("You killed everybody")
                break

    def PlayerRan(self):
        print("You started to run towards the castle")
        print("The king is disappointed in you, you lost some fame")
        print("You take a rest for the next day")

    def GamePlus(self):
        print("You have clean the places the king asked, Bravo!")
        print("Do you want to start again(the levels are harder)")
        print("1 : yes")
        print("2 : no")
        inGameChoice = input("")
        if(int(inGameChoice) == 1):
            self.CaveTaken = False
            self.ForestTaken = False
            self.SwampTaken = False
            print("Good Luck.")
            return 1
        if(int(inGameChoice) == 2):
            print("Thank you for playing")
            return 2
        else:
            print("Dude you have to press 1 or 2, ONE OR TWO")
            self.GamePlus()
        
    def boast(self):
        print("what do you want to do?")
        print("1 : Continue on with your quest")
        print("2 : boast at the castle")
        inGameChoice = input("")
        if(int(inGameChoice) == 1):
            return 1
        if(int(inGameChoice) == 2):
            return 2
        else:
            print("Dude you have to press 1 or 2, ONE OR TWO")
            self.GamePlus()

    def start(self):
        started = self.GameStarted()
        self.PlayerChoice()
        placesDone = 0
        level = 1
        while(started == 1):
            ennemis = self.PlaceChosen(level)
            self.TurnBaseCombat(ennemis)
            placesDone += 1
            boasting = self.boast()
            while(boasting == 2):
                boasting = self.boast()
            if(placesDone == 3):
                started = self.GamePlus
            level += 1

    def __init__(self):
        self.start()