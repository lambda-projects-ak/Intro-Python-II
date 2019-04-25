# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item


class Room:
    def __init__(self, name, description, end=False):
        self.name = name
        self.description = description
        self.isEnd = end
        self.is_lit = True
        self.items = []
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def add_item(self, new_item):
        self.items.append(new_item)

    # define how we want the output to look when you print the object
    # repr is meant for developer to see as you're developing
    def __repr__(self):
        return f"{self.name}"

    # str is used when you are expecting user to see the output
    def __str__(self):
        room_information = f"Room information: \n"
        room_information += f"  {self.name} \n"
        room_information += f"  {self.description} \n"
        return room_information

    def get_possible_directions(self):
        possible_directions = []
        if self.n_to is not None:
            possible_directions.append('[N] Move North  ')
        if self.w_to is not None:
            possible_directions.append('[W] Move West  ')
        if self.s_to is not None:
            possible_directions.append('[S] Move South  ')
        if self.e_to is not None:
            possible_directions.append('[E] Move East  ')
        return ' '.join(possible_directions)
