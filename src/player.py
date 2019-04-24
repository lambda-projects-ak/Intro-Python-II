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
        # if carry_weight exceeds carry_limit, prevent player movement

    def pickup(self, item_name):
        if len(self.current_room.items) == 0:
            print("There are no items to pick up. \n")
        else:
            for i in self.current_room.items:
                if i.name == item_name.capitalize():
                    self.inventory.append(i)
                    self.carry_weight += i.weight
                    print(f"You pick up {i.name} \n")
                elif i.name != item_name.capitalize():
                    print("The item you entered is not in this room. \n")

    def drop(self, item):
        # subtract item.weight from carry_weight
        self.inventory.remove(item)

    def check_inventory(self):
        if len(self.inventory) == 0:
            print("Your inventory is currently empty. \n")
        else:
            print("Player Inventory:")
            for i in self.inventory:
                print(f"  Item: {i.name}, Weight: {i.weight} \n")

    def check_stats(self):
        print(
            f"Player Status: \n  Health: {self.current_health}/{self.max_health}  \n  Carry Limit: {self.carry_weight}/{self.carry_limit}  \n  Location: {self.current_room.name} \n")

    def check_for_items(self):
        if len(self.current_room.items) == 0:
            print("You scan the room and see nothing. \n")
        else:
            print("You scan the room and see:")
            for i in self.current_room.items:
                print(
                    f"  Item: {i.name}, Description: {i.description} Weight: {i.weight}")
            print("\n")
