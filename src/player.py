# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.max_health = 10
        self.current_health = 10
        self.inventory = []
        self.carry_limit = 10
        self.carry_weight = 0

    def pickup(self, item):
        self.inventory.append(item)

    def drop(self, item):
        self.inventory.remove(item)

    def print_current_room(self):
        return self.current_room.name

    def check_stats(self):
        return (f"Player Status: \n  Health: {self.current_health}/{self.max_health} \n  Inventory: {self.inventory} \n  Carry Limit: {self.carry_weight}/{self.carry_limit}")
