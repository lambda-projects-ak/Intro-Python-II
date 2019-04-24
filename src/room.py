# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, end=False):
        self.name = name
        self.description = description
        self.isEnd = end
        self.is_lit = True
        self.items = []
