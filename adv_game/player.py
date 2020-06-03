# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_location(self):
        return self.location

player1 = Player("Jack", 21, "Foyer")

print(player1.get_name())
print(player1.get_location())