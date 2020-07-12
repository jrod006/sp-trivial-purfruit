


class Player:
#Basic Player Class
    def __init__(self, ID):
        self.chips = 0
        self.id = ID
    

    def addChip(self, number):
        self.chips += number
    
