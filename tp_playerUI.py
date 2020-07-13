class playerUI:

    def __init__(self, player):
        print("INIT PLYAER UI")
        self.myplayer = player

    def updateUI(self):
            print("Player" + str(self.myplayer.id) + "CHIPS:")
            print(self.myplayer.chips)
