name = input(f"Before we start, what is your name? ")
setup = input(f"Welcome, {name}. You will now be transported to the Game. You have been selected to be sent to year 3027. You will be sent with few supplies. If you die, we will not be able to transport you back. You will deal with danger beyond our imagination. Prepare for departure. Oh! I almost forgot. There is one more thing you must know about. You will be renamed a player. When and if you get back, you will have your name back. Good luck. (press enter to contiue.) ")
commentary1 = print(f"The light and sounds as I entered the transport was overwhelming. Tingles ripped across my body. My memory was fading. The last thing I thought before all was forgotten, was {name}. My name is {name}.")
rename = (f"Player 31")
game = input(f"Welcome to the year 3027, {rename}. We need your help. The only thing that you can do is to move forwards. Press W to walk. Press I for inventory. When you leave the transport, you will be on your own. All you need to do is survive. To check your inventory, press i (I). To walk, press w (W). Press enter to start.")


# import random

# player_health = 100
# enemy_health = 100

# def attack_enemey():
#     while True:
#         if player_health > 0:
#             your_attack = random.randint(10,100)
#             print(f"You attacked the enemy for {your_attack} damage!")
#             enemy_health -= your_attack

#     if enemy_health > 0:
#         enemy_attack = random.randint(10,100)
#         print(f"The enemy has attacked you for {enemy_attack} damage!")
#         enemy_health -= your_attack