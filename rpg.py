import random

name = input(f"Before we start, what is your name? ")
setup = input(f"Welcome, {name}. You will now be transported to the game. You have been selected to be sent to year 3027. You will be sent with few supplies. If you die, we will not be able to transport you back. You will deal with danger beyond our imagination. Prepare for departure. Oh! I almost forgot. There is one more thing you must know about. You will be renamed a player. When and if you get back, you will have your name back. Good luck. (press enter to contiue.) ")
commentary1 = print(f"The light and sounds as I entered the transport was overwhelming. Tingles ripped across my body. My memory was fading. The last thing I thought before all was forgotten, was {name}. My name is {name}.")
rename =(f"Player 31")
game = input(f"Welcome to the year 3027, {rename}. We need your help. The only thing that you can do is to move forwards. Press W to walk. Press I for inventory. When you leave the transport, you will be on your own. All you need to do is survive. Press enter to start.")

player_health = 100
enemy_health = 100
inventory = (f"{rename}'s inventory: You have a {player_health} HP, some food, and a journal.")

def attack_enemey(player_health, enemy_health):
    while True:
        if player_health > 0:
            your_attack = random.randint(10,100)
            print(f"You attacked the enemy for {your_attack} damage!")
            enemy_health -= your_attack

        if enemy_health > 0:
            enemy_attack = random.randint(10,100)
            print(f"The enemy has attacked you for {enemy_attack} damage!")
            player_health -= enemy_attack
        
        if player_health <=0:
            print("You died. You will be terminated from the game immediately.")
            exit()

        if enemy_health <=0:
            print("You killed the enemy!")
            break


while True:
    choice = input("To check you inventory, press I (i), to walk, press W (w). ")
    if choice == "I" or choice == "i":
        print (inventory)
        input ("To close out of inventory, press enter. ")
    elif choice == "W" or choice == "w":
        print ("You have chosen to walk. Good luck.")
        enemy_chance = random.randint(1,3)
        if enemy_chance == 1:
            print("Oh no! You've encountered a cyborg!")
        elif enemy_chance == 2:
            print("Oh no! You've encountered a virus!")
        elif enemy_chance == 3:
            print("Oh no! You've encountered a rouge glitch!")
        fight_or_run = input("Would you like to f-fight or r-run? ")
        if fight_or_run == 'f':
            attack_enemey(player_health, enemy_health)
        elif fight_or_run == 'r':
            run_chance = random.randint(1,2)
            if run_chance == 1:
                print("You got away!")
            else:
                attack_enemey(player_health, enemy_health)



