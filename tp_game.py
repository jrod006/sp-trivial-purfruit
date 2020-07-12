import tp_settings
import tp_player


class Game:

    def __init__(self):
        print("GAME INIT")
        #Init global UI/objects here
        self.players = []


    def processTurn(self):
        print('DOING A TURN')
        self.players[0].addChip(1)
        
        

    def showUI(self):
        print("DISPLAY GAME UI")
        # Text based State UI for now
        for player in self.players:
            print("Player" + str(player.id))
            print(player.chips)
        
    def displayStartupScreen(self):
        print("SHOWING STARTUP SCREEN EDIT/CONFIRM SETTINGS HERE")
        print(self.currentSettings)
        input("PRESS ENTER TO CONFIRM SETTINGS")
        self.startGame()

    def startGame(self):
        print("Starting Game with Settings")
        print(self.currentSettings)
        #Init Players
        for i in range(0, int(self.currentSettings["players"])):
            self.players.append(tp_player.Player(i))
        for j in range(4):
            self.processTurn()
            self.showUI()
            
    def run(self):
        #Load Settings
        settings = tp_settings.Settings()
        self.currentSettings = settings.getSettings()
        self.displayStartupScreen()
        

        
        
        


def testGame():
    print('Testing Game Module')
    game = Game()
    game.run()

if (__name__=="__main__"):
        testGame()
