from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mouth beckons"),

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

#Declare all the items
item = {
    'sword': Item("sword", "Long steel sword"),
    'wand': Item("wand", "Casts magic spells"),
    'rock': Item("rock", "A fist-sized rock"),
    'gold': Item("gold", "Pile of gold coins"),
    'crown': Item("crown", "Golden grown with gem stones"),
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

# Add items to rooms
room['outside'].items = [item['sword'], item['rock']]
room['treasure'].items = [item['gold'], item['crown']]
room['overlook'].items = [item['wand']]
#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player("Prince", room['outside'])

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

def show_current_room():
    print(player.room.name + " - " + player.room.description)
    print("Items:")
    for i in range(len(player.room.items)):
        print(player.room.items[i].name)


def get_user_input():
    return input('Choose a direction to move (n, s, e, w), or q to quit \n >> ')

def print_no_room_error():
    print("No room that way.")

def move_player(command):
    if command == 'n':
        if player.room.n_to:
            player.room = player.room.n_to
        else:
            print_no_room_error()
    if command == 's':
        if player.room.s_to:
            player.room = player.room.s_to
        else:
            print_no_room_error()
    if command == 'e':
        if player.room.e_to:
            player.room = player.room.e_to
        else:
            print_no_room_error()
    if command == 'w':
        if player.room.w_to:
            player.room = player.room.w_to
        else:
            print_no_room_error()
    
show_current_room()
command = get_user_input()

while command != 'q':
    move_player(command)
    show_current_room()
    command = get_user_input()

