from room import Room
from player import Player
# Declare all the rooms


room = {'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
        'foyer':    Room("Foyer", """Dim light filters in from the south. Dust, passages run north and east."""),
        'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling,into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),
        'narrow':   Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air."""),
        'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""),
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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
user_name = input("What is your name? ")

#user starts outside
location = "outside"
user = Player(room[location],user_name)

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
prompt = "Where do you wish to go? Valid Inputs: N W E S (type 'q' to quit)"
intro = True

while game_on:
    if intro:
        print("Welcome to Rob Quest!")
        intro = False
    print("You are in: ", user.location.name)
    print("You see: ", user.location.description)
    path = input(prompt)
    if path == "q":
        game_on = False
    if path == "N":
        if hasattr(user.location, 'n_to'):
            user.location = user.location.n_to
        else:
            print("You can't go that way!")
    if path == "S":
        if hasattr(user.location, 's_to'):
            user.location = user.location.s_to
        else:
            print("You can't go that way!")
    if path == "E":
        import pdb; pdb.set_trace()
        if hasattr(user.location, 'e_to'):
            user.location = user.location.e_to
        else:
            print("You can't go that way!")
    if path == "W":
        if hasattr(user.location, 'w_to'):
            user.location = user.location.w_to
        else:
            print("You can't go that way!")
    else:
        print("That is not a direction!")
    

