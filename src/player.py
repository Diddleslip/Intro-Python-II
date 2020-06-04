# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.list = []

    def __str__(self):
        return f"Player, '{self.name}' {self.list}"

    def gotItem(self, item):
        return f"You added {item} to your inventory!"

    def dropItem(self, item):
        return f"You dropped {item} from your inventory!"