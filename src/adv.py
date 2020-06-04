from room import Room
from player import Player
from color import Color
import textwrap 

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

# print(room['foyer'].values)
#
# Main
#
# Make a new player object that is currently in the 'outside' room.
newPlayer = Player("Sir Cornelius the 3rd", "outside")
# newPlayer.current_room = "inside" ## Changing location 
print(f"{Color.CYAN} {newPlayer} {Color.END}")
userInput = input(f"{Color.YELLOW}Move commands: [w] up, [a] left, [d] right, [s] down   Your input: {Color.END}")

# commands()
# userInput = commands
# print(userInput) Doesn't work -- answer: <function commands at 0x0000015287563948>

## Command shortcuts:
# w = 
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.


def checkMove(direction):
    val = getattr(room[newPlayer.current_room], direction)
    if not val == None:
        for key, value in room.items():
            if value == val:
                newPlayer.current_room = key
                print(f"{Color.CYAN}{newPlayer}{Color.END}{Color.GREEN} is in room: {val.name} -- Description: {textwrap.wrap(val.description)}{Color.END}")
    else: 
        print(f"{Color.RED}Player can't go there!{Color.END}")

while not userInput == "q":
    if userInput == "w":
        checkMove("n_to")
    elif userInput == "a":
        checkMove("w_to")
    elif userInput == "s":
        checkMove("s_to")
    elif userInput == "d":
        checkMove("e_to")
    else:
        print(f"{Color.RED}Wrong input, try again.{Color.END}")
    
    userInput = input(f"{Color.YELLOW}Move commands: [w] up, [a] left, [d] right, [s] down   Your input: {Color.END}")

print("Game quit, play again later!")

#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
