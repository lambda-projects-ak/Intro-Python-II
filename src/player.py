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

    def pickup(self, action_input):
        z = 0
        if len(self.current_room.items) == 0:
            print("There are no items to pick up. \n")
        else:
            for i in action_input:
                for x in self.current_room.items:
                    if i.capitalize() == x.name:
                        self.inventory.append(x)
                        self.carry_weight += x.weight
                        self.current_room.items.remove(x)
                        print(f"You pick up {x.name} \n")
                        z = 1
            if z == 0:
                print("The item you entered is not in this room. \n")

    def drop(self, action_input):
        z = 0
        if len(self.inventory) == 0:
            print("You have no items to drop. \n")
        else:
            for i in action_input:
                for item in self.inventory:
                    if i.capitalize() == item.name:
                        self.inventory.remove(item)
                        self.carry_weight -= item.weight
                        self.current_room.items.append(item)
                        print(f"You dropped {item.name} \n")
                        z = 1
            if z == 0:
                print("The item you entered is not your bag. \n")

    def check_inventory(self):
        if len(self.inventory) == 0:
            print("Your inventory is currently empty. \n")
        else:
            print("Player Inventory:")
            for item in self.inventory:
                print(f"  Item: {item.name}, Weight: {item.weight} \n")

    def check_stats(self):
        print(
            f"Player Status: \n  Health: {self.current_health}/{self.max_health}  \n  Carry Limit: {self.carry_weight}/{self.carry_limit}  \n  Location: {self.current_room.name} \n")

    def check_for_items(self):
        if len(self.current_room.items) == 0:
            print("You scan the room and see nothing. \n")
        else:
            print("You scan the room and see:")
            for item in self.current_room.items:
                print(
                    f"  Item: {item.name}, Description: {item.description} Weight: {item.weight}")
            print("\n")

    def move_player(self, direction_input):
        if direction_input == "n":
            if self.current_room.n_to == None:
                print("You walked into a wall. \n")
            else:
                self.current_room = self.current_room.n_to
        elif direction_input == "e":
            if self.current_room.e_to == None:
                print("You walked into a wall. \n")
            else:
                self.current_room = self.current_room.e_to
        elif direction_input == "s":
            if self.current_room.s_to == None:
                print("You walked into a wall. \n")
            else:
                self.current_room = self.current_room.s_to
        elif direction_input == "w":
            if self.current_room.w_to == None:
                print("You walked into a wall. \n")
            else:
                self.current_room = self.current_room.w_to
