

class Player:
#Basic Player Class
    def __init__(self, ID):
        self.chips = []
        self.id = ID
        self.location = 0

    def addChip(self, category):
        if (category not in self.chips):
            self.chips.append(category)

    def updateLocation(location):
        self.location=location
    
    def __str__(self):
        outstr = ''
        outstr += 'Player ' + str(self.id) + ':\n'
        outstr += 'Location = ' + str(self.location) + '\n'
        outstr += 'Chips: ' + str(self.chips)
        return outstr
