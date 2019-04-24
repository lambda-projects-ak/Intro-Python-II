from room import Room
from player import Player
from item import Item

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
# from outside, player can move north into foyer
room['outside'].n_to = room['foyer']


# from foyer, player can move south to outside, north to overlook, east to narrow
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']

# from overlook, player can move south to foyer
room['overlook'].s_to = room['foyer']

room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']

room['treasure'].s_to = room['narrow']


# Notes:
# player moves north
# player.current_room = current_room.{n}_to # dynamic based on input
# player.current_room = room['foyer']


# Make a new player object that is currently in the 'outside' room.
player = Player("Alex", room['outside'])

print(player.current_room.name)
print(player.current_room.n_to.name)

if player.current_room.n_to is not None:
    pass

# generate items
sword = Item("Sword", "Made of iron", 2)
shield = Item("Shield", "Made of iron", 4)

room['outside'].add_item(sword)
# room['outside'].add_item(shield)


print("------------------------- \n")
# if player input == "status"
player.check_stats()


# if player input == "check room"
player.check_for_items()

# if player input == name of item in a room
player.pickup("sword")
# player.pickup("Shield")

# if player input == "inventory"
player.check_inventory()

# if player input == "status"
player.check_stats()

print("-------------------------")
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:
    cmd = input("-> ")
    print(cmd)
    if cmd == "q":
        print("Goodbye!")
        break
