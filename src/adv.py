from room import Room
from player import Player
from color import Color
from items import Item
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

    'desert': Room("Desert", """Very long quote about a spooky island..."""),
}

# Declare all the items

items = {
    "WOODEN_SWORD": Item("wooden sword", "Crusty ol' sword"),
    "TORCH": Item("torch", "Stay lit"),
    "5_GOLD": Item("5 gold", "Ching ching"),
    "OLD_ROCK": Item("rock", "Just gravel"),
    "SHARP_GLASS": Item("sharp glass", "Pointy! Be careful."),
    "FEATHER": Item("feather", "Soft like the wind up here."),
    "250_GOLD": Item("250 gold", "We're millionares!"),
    "DIAMOND_SWORD": Item("diamond sword", "Damage +7, 1.6 Attack Speed"),
    "DEAD_SKULL": Item("human skull", "Looks like it's been here for weeks")
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['desert'].e_to = room['foyer']
room['foyer'].w_to = room['desert']
room['foyer'].s_to = room['outside']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Add items to rooms

room["outside"].list.append(items["WOODEN_SWORD"])
room["outside"].list.append(items["TORCH"])
room["foyer"].list.append(items["SHARP_GLASS"])
room["foyer"].list.append(items["OLD_ROCK"])
room["overlook"].list.append(items["5_GOLD"])
room["overlook"].list.append(items["FEATHER"])
room["treasure"].list.append(items["250_GOLD"])
room["treasure"].list.append(items["DIAMOND_SWORD"])
room["desert"].list.append(items["DEAD_SKULL"])


#
# Main
#
# Make a new player object that is currently in the 'outside' room.
newPlayer = Player("Sir Cornelius the 3rd", "outside")

def addItem(item):
    value = room[newPlayer.current_room].list

    for i in value:
        if i.name == item:
            newPlayer.list.append(i) ## Adding i
            value.remove(i)
            print(f"{Color.CYAN}{newPlayer.gotItem(i.name)}{Color.END}")
            return

    print("Item not found")
    

            
def removeItem(item):
    value = room[newPlayer.current_room].list
    valueTwo = newPlayer.list
    for i in valueTwo:
        if i.name == item:
            valueTwo.remove(i) ## Adding i
            value.append(i)
            print(f"{Color.CYAN}{newPlayer.dropItem(i.name)}{Color.END}")
            return

    print(f"{Color.RED}No such item in inventory!{Color.END}")

# newPlayer.current_room = "inside" ## Changing location 
print(f"\n{Color.CYAN}{newPlayer} {Color.END}\n{Color.GREEN}Is in room: {newPlayer.current_room} -- Description: {room[newPlayer.current_room].description}{Color.END}")
print(f"\n{Color.PURPLE}Items Available: {Color.END}")
for i in room[newPlayer.current_room].list:
    print(f"{Color.PURPLE}{Room.getItems(i)}{Color.END}")
userInput = input(f"To pick up items type get [item]\nTo drop items, type drop [item]\n{Color.YELLOW}Move commands: [w] up, [a] left, [d] right, [s] down   Your input: {Color.END}").lower()


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
                print(f"\n{Color.PURPLE}Items Available: {Color.END}\n")
                for i in room[newPlayer.current_room].list:
                    print(f"{Color.PURPLE}{Room.getItems(i)}{Color.END}")
                print(f"\n{Color.CYAN}{newPlayer}\n{Color.END}{Color.GREEN}Is in room: {val.name} -- Description: {val.description}{Color.END}")
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
    elif "get" in userInput:
        addItem(userInput.split("get ")[1])
    elif "take" in userInput:
        addItem(userInput.split("take ")[1])
    elif "drop" in userInput:
        removeItem(userInput.split("drop ")[1])
    else:
        print(f"{Color.RED}Wrong input, try again.{Color.END}")
    
    userInput = input(f"To pick up items type: get [item]\nTo drop items, type: drop [item]\n{Color.YELLOW}Move commands: [w] up, [a] left, [d] right, [s] down   Your input: {Color.END}")

print("Game quit, play again later!")

#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
