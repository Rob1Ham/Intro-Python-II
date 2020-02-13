# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self,name,description,objects):
        self.name = name
        self.description = description
        self.N_to = None
        self.E_to = None
        self.S_to = None
        self.W_to = None
        self.objects = objects