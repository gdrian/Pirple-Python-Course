'''
Pirple Homework #8:
	Classes
'''

class Pet:
    def __init__(self, n, a, h, p):
        self.name = n
        self.age = a
        self.hunger = h
        self.playful = p

    # Getters
    def getName(self):
        return self.name
    
    # Setters
    def setName(self, newName):
        self.name = newName