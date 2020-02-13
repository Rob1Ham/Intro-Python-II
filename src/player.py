# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self,location,name,inventory):
        self.location = location
        self.name = name
        self.inventory = inventory
    def move(self,direction):
        next_room = getattr(self.location, f"{direction}_to")
        if next_room is not None:
            self.location = next_room
    def look(self):
        print("You are in: ", self.location.name)
        print("You see: ", self.location.description)
        print("You can take: ", self.location.objects)
    def take(self,item):
        if item is not None:
            if item in self.location.objects:
                print(f"You have taken {item}.")
                self.location.objects.remove(item)
                self.inventory.append(item)
        else:
            print("There is no " + str(item) + "to pick up...")
    def drop(self,item):
        if item is not None:              
            if item in self.inventory:
                print(f"You have dropped {item}.")
                self.inventory.remove(item)
                self.location.objects.append(item)
        else:
            print("You do not have"+str(item))