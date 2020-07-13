import tp_playerUI


class Player:
#Basic Player Class
    def __init__(self, ID):
        self.chips = 0
        self.id = ID
        self.UI = tp_playerUI.playerUI(self)
    

    def addChip(self, number):
        self.chips += number

    def updateUI(self):
        self.UI.updateUI()
    
