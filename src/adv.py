from room import Room
from player import Player
# Declare all the rooms


room = {'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons",["Sword","Shield"]),
        'foyer':    Room("Foyer", """Dim light filters in from the south. Dust, passages run north and east.""",["Key"]),
        'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling,into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""",[]),
        'narrow':   Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air.""",[]),
        'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.""",[]),
}


# Link rooms together

room['outside'].N_to = room['foyer']
room['foyer'].S_to = room['outside']
room['foyer'].N_to = room['overlook']
room['foyer'].E_to = room['narrow']
room['overlook'].S_to = room['foyer']
room['narrow'].W_to = room['foyer']
room['narrow'].N_to = room['treasure']
room['treasure'].S_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
user_name = input("What is your name? ")

#user starts outside
location = "outside"
starting_inventory = []
user = Player(room[location],user_name,starting_inventory)

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

game_on = 1
prompt = "Where do you wish to go? Valid Movement Inputs: [N W E S], take (item), drop (item), q (to quit)"
intro = True

while game_on:
    if intro:
        print("Welcome to Rob Quest!")
        intro = False
        user.look()
    cmd = input(prompt)
    if cmd in ["N","S","E","W"]:
        user.move(cmd)
        user.look()
    elif cmd.startswith("take"):
        item = cmd.split(" ")[1]
        #import pdb; pdb.set_trace()
        user.take(item)
    elif cmd.startswith("drop"):
        item = cmd.split(" ")[1]
        user.drop(item)
    elif cmd == "q":
        game_on = False
        print("Goodbye!")
    elif cmd == "inventory":
        print("You have:" + str(user.inventory))
    else:
        print("That is not a valid action!")
    

