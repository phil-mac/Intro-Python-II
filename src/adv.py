from room import Room
from player import Player
from item import Item
from lightSource import LightSource

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mouth beckons", True),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", True),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", True),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", False),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", False),
}

#Declare all the items
item = {
    'sword': Item("sword", "Long steel sword"),
    'wand': Item("wand", "Casts magic spells"),
    'rock': Item("rock", "A fist-sized rock"),
    'gold': Item("gold", "Pile of gold coins"),
    'crown': Item("crown", "Golden grown with gem stones"),
    'lamp': LightSource("lamp", "provides light")
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
room['narrow'].items = [item['lamp']]
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

def room_is_lit():
    if player.room.is_light:
        return True
    elif any(isinstance(x, LightSource) for x in player.room.items):
        return True
    elif any(isinstance(x, LightSource) for x in player.inventory):
        return True


def show_current_room():
    if room_is_lit():
        print(player.room.name + " - " + player.room.description)
        print("Room items:")
        for i in range(len(player.room.items)):
            print(player.room.items[i].name)
    else:
        print("It's pitch black!")

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

def interact_item(verb, noun):
    if verb == "get" or verb == "take":
        if not room_is_lit:
            print("Good luck finding that in the dark!")
        elif (noun in item) and (item[noun] in player.room.items):
            player.pickup_item(item[noun])
            player.room.items.remove(item[noun])
        else:
            print("item not found in room")
    if verb == "drop":
        if (noun in item) and (item[noun] in player.inventory):
            player.drop_item(item[noun])
            player.room.items.append(item[noun])
        else:
            print("item not found in inventory")

def show_inventory():
    print("Inventory items:")
    for i in range(len(player.inventory)):
        print(player.inventory[i].name)

def parse_command(command):
    command_array = command.split(' ')
    if (command == 'i' or command == 'inventory'):
        show_inventory()
    elif len(command_array) == 1:
        move_player(command)
    elif len(command_array) == 2:
        interact_item(command_array[0],command_array[1])

show_current_room()
command = get_user_input()

while command != 'q':
    parse_command(command)
    show_current_room()
    command = get_user_input()

