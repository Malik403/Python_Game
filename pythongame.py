#imports
import os
import random

#Entity class
class Entity:
    """ This class is for all the Player and Enemy Entities. """
    def __init__(self, health, damage=0):
        # Entity Class Initialization.
        self.health = health
        self.damage = damage

    def player(self, potions, super_attack):
        """ Player Initialization. """
        self.potions = potions
        self.super_attack = super_attack

    def enemy(self):
        """ Enemy Initialization. """
        while True:
            attack_dam = random.randint(1, 10)
            return attack_dam

#Instances of the classes
#Player Instance
player1 = Entity(100, 10) #Health, Damage
player1.player(3, 3) #Potions, Super_Attack

#Enemy1 Instances (3,1)
enemy1 = Entity(50)


#Enemy2 Instance
enemy2 = Entity(50)
enemy2.enemy()

#Enemy3 Instance
enemy3 = Entity(50)
enemy3.enemy()

#Health List 
health_list = [enemy1.health, enemy2.health, enemy3.health] #This is in a list. Use a for loop

#Gameplay Function
def gameplay():
    """ This functin is everything gameplay related (May add a few other functions). """
    print("Okay, Let's get to the gameplay")
    input("Press Enter to Continue.\n")
    print(f"Enemies are coming!!!.")
    input("Press Enter to Continue.\n")
    #enemy_count = 0 #This is an enemy count for the custom message for each
    for i in range(3): #Thie for loop is to count the health list
        enemy_count = i # Used so the program knows which enemy the user is on for those prints
        if enemy_count == 0:
            print(f"Enemy {1} is coming!")
            input("Press Enter to Continue")
        elif enemy_count == 1:
            print(f"Enemy {2} is coming!")
            input("Press Enter to Continue")
        elif enemy_count == 2:
            print(f"Enemy {3} is coming!")
            input("Press Enter to Continue")
        while True: #This while loop is for the game itself
            #Printing Messages
            print(f"Their health is: {health_list[i]}")
            input("Press Enter to Continue\n")
            if player1.super_attack != 0:
                #Players choice
                choice = input(f"Attack or Potion?\n")
                #If-Statements for players choice
                if choice == "Attack" or choice == "attack":
                    health_list[i] -= player1.damage
                    print(f"Attacked Them! Their health is now {health_list[i]}")
                    player1.super_attack -= 1
                    input("Press Enter to Continue\n")
                elif choice == "Potion" or choice == "potion":
                    if player1.potions == 0:
                        print("Sorry, no more potions!")
                    elif player1.potions > 0:
                        print("Potioning up!")
                        input("Press Enter to Continue\n")
                        player1.health = 100
                        player1.potions -= 1
                        print(f"Your health is now {player1.health}")
                        input("Press Enter to Continue\n")
                        print(f"You have {player1.potions} left!")
                    else:
                        print("Potioning Error")
                elif choice != "Potion" or choice != "potion" or choice != "Attack" or choice != "attack":
                    print("Sorry, invalid input, this will cost you!")
                    input("Press Enter to Continue.")
            elif player1.super_attack == 0:
                print("Super Attack is Ready!")
                input("Press Enter to Continue.\n")
                choice = input(f"Do you want to use it now? Super attack damage will be: {20} type: yes/no \n")
                if choice == "yes" or choice == "Yes":
                    print("Using super attack!")
                    input("Press Enter to Continue\n")
                    print(f"You did: {20} damage!")
                    input("Press Enter to Continue\n")
                    health_list[i] -= 20
                    print(f"Their health is now: {health_list[i]}")
                    player1.super_attack = 3
                elif choice == "no" or choice == "No":
                    player1.super_attack = 1
            #This if statement is for when the enemies health hits 0
            if health_list[i] <= 0:
                if health_list[2] <= 0:
                    print("Congraulations, you won!")
                    input("Press Enter to claim your prize!")
                    exit()
                print("Beat the Enemy! Next one is coming up")
                input("Press Enter to Continue.\n")
                print("Your health is now back to 100")
                input("Press Enter to Continue\n")
                print("Moving on to next opponent!")
                input("Press Enter to Continue\n")
                enemy_count += 1
                player1.health = 100
                break
            #Enemy Attacking player
            enemy_damage = enemy1.enemy()
            print(f"Enemy is attacking now. Their damage is: {enemy_damage}")
            input("Press Enter to Continue.\n")
            player1.health -= enemy_damage
            print(f"Your health is now: {player1.health}")
            #Dying or killing all of the opponents
            if player1.health <= 0:
                print("Sorry, you lose. Exiting game")
                input("Press Enter to Continue\n")
                exit()
#This code dont even look at - this is fine!
#User_Information Function
def user_information():
    """ This function is all about the users information. This section of
        code introduces the user by their name and asks if they want to change it. """
    try:
        with open("name.txt", "r") as myFile:
            global reading_name
            reading_name = myFile.read()
            myFile.close()
        print(f"Hello {reading_name}, Welcome back to the game.")
        input("Press Enter to Continue\n")
        print("If you want to change your name, now is the time to do so.")
        input("Press Enter to Continue\n")
        name_change = input("Type in Yes/No to change your name: ")
        if name_change == "Yes" or name_change == "yes":
            os.remove("name.txt")
        elif name_change == "No" or name_change == "no":
            gameplay()
    except FileNotFoundError:
        #This section of code gets to know the users name + saves it into a file called "name.txt"
        print("Hello User, Welcome to my Game!")
        input("Press Enter to Continue\n")
        print("Let's first start by getting your name.")
        input("Press Enter to Continue\n")
        name = input("Please Enter Your Name Here: ")
        print("Got it! Now, when you start the program again, it will no longer ask!")
        input("Press Enter to Continue\n")
        with open("name.txt", "w") as myFile:
            myFile.write(name)
            myFile.close()

while True: #While loop for for whole program. (Program will exit after player has killed all of the enemies OR dies)
    user_information() #Calling the user_information (This is the only call that needs to be done)
