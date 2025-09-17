import random
game_input = int(input("Terminal hunter: Hunt the beasts in terminal\nTo start game enter a number\nEnter 1. to start the game \nEnter 2. to exit\nEnter here: "))
xp = 0
inp = 0
dmg = 0
if game_input == 1:
    name = input("what's your name: ")
    print(f"In the dungeon full of monsters, you {name} chose to bravely attack\nand kill monsters here's your weapon")
    print("======wooden sword acquired: atk dmg = 8")
    dmg = 8
    print("Oh! look a monster\n\n")
    print("Skeleton: HP = 5, level = slave\npress 1 to attack")
    inp = int(input("->: "))
    if inp == 1:
        print(f"{name} slained a Skeleton\n +3xp")
        xp += 3
        game_input = 3
    else:
        game_input = 1
else:
    exit()
if game_input == 3:
    print("Tutorial completed!")
    print("Now slain monsters gain xp")
    print("press 9 to exit")
    while inp != 9:
        rand = random.randint(1, 6)
        if rand == 1:
            print("Skeleton: HP = 5 class = slave\n press 1 to attack")
            inp = int(input("->: "))
            xp += 3
        elif rand == 2:
            print("Magician: HP = 8 class = magic\n press 1 to attack")
            inp = int(input("->: "))
            xp += 5
        elif rand == 3:
            print("Ghoul: HP = 15 class = ghost\n press 1 to attack")
            hp = 15
            while hp > dmg:
                inp = int(input("->: "))
                hp = hp - dmg
            xp += 7
        elif rand == 4:
            print("Dragon Cub: HP = 17 class = mighty\n press 1 to attack")
            hp = 17
            while hp > dmg:
                inp = int(input("->: "))
                hp = hp - dmg
            xp += 8
        elif rand == 5:
            print("Butcher: HP = 20 class = epic\n press 1 to attack")
            hp = 20
            while hp > dmg:
                inp = int(input("->: "))
                hp = hp - dmg
            xp += 10
        elif rand == 6:
            print("Pheonix: HP = 25 class = unique\n press 1 to attack")
            hp = 25
            while hp > dmg:
                inp = int(input("->: "))
                hp = hp - dmg
            xp += 20