from room import Room
from player import Player
from item import Item
import os
import random

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


############################################################################################
######################################## GAME START ########################################
############################################################################################


os.system('cls' if os.name == 'nt' else 'clear')
# Make a new player object that is currently in the 'outside' room.
name = input("-> Enter your name: ")
os.system('cls' if os.name == 'nt' else 'clear')

# Generate player
player = Player(name, room['outside'])

# Generate items
sword = Item("Sword", "Made of iron", 2)
shield = Item("Shield", "Made of iron", 4)
key = Item("Key", "Made of gold", 1)

# Add items to room
room['outside'].add_item(sword)
room['outside'].add_item(shield)

# Generate Key - needs to prevent key from spawning inside of treasure room
random = random.choice(list(room.keys()))
room[random].add_item(key)

print("-- Adventure Game ---------------------------------- \n")
print(f"Welcome {player.name} \n\n")
print(player.current_room)

print("---------------------------------------------------- \n")
print(player.current_room.get_possible_directions())
print("[I] Check Inventory [C] Check Stats [R] Check Room  \n[P] Pickup Item  [D] Drop Item [Q] Quit Game")
selection = input("-> ").upper()

os.system('cls' if os.name == 'nt' else 'clear')

while not selection == "Q":
    print("-- Adventure Game ---------------------------------- \n")
    print(player.current_room)

    # if player input == "s"
    if selection == "C":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("-- Adventure Game ---------------------------------- \n")
        player.check_stats()

    elif selection == "N":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("-- Adventure Game ---------------------------------- \n")
        player.move_player("n")
        print(player.current_room)

    elif selection == "W":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("-- Adventure Game ---------------------------------- \n")
        player.move_player("w")
        print(player.current_room)

    elif selection == "S":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("-- Adventure Game ---------------------------------- \n")
        player.move_player("s")
        print(player.current_room)

    elif selection == "E":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("-- Adventure Game ---------------------------------- \n")
        player.move_player("e")
        print(player.current_room)

    elif selection == "I":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("-- Adventure Game ---------------------------------- \n")
        player.check_inventory()

    elif selection == "P":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("-- Adventure Game ---------------------------------- \n")
        item_name = input("Pick up: ")
        player.pickup(item_name)

    elif selection == "R":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("-- Adventure Game ---------------------------------- \n")
        player.check_for_items()

    elif selection == "D":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("-- Adventure Game ---------------------------------- \n")
        item_name = input("Drop item: ")
        player.drop(item_name)

    elif selection == "Q":
        break

    else:
        print(selection)
    # if player input == "check room"
    # player2.check_for_items()

    # if player input == name of item in a room
    # player2.pickup("sword")
    # player2.pickup("shield")

    # if player input == "inventory"
    # player2.check_inventory()

    # if player input == "status"
    # player2.check_stats()
    print("---------------------------------------------------- \n")
    print(player.current_room.get_possible_directions())
    print("[I] Check Inventory [C] Check Stats [R] Check Room  \n[P] Pickup Item  [D] Drop Item [Q] Quit Game")
    selection = input("-> ").upper()
    os.system('cls' if os.name == 'nt' else 'clear')
