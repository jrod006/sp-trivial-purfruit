import tp_settings
import tp_player
import tp_gameUI
import tp_startScreen
import tp_question
from tp_diceroll import DiceRoll
import time

class Game:

    def __init__(self):
        print("GAME INIT")
        #Init global UI/objects here
        self.players = []
        self.UI = tp_gameUI.GameUI()
        self.startScreen = tp_startScreen.StartScreen(self)


    def processTurn(self):
        print('DOING A TURN')
        print('ROLL DICE: ')
        DiceRoll.rollDice(self)
        tp_question.QuestionGenerator().retrieveQA()
        self.players[0].addChip(1)
        self.showUI()
        time.sleep(2)
        
        

    def showUI(self):
        # Text based State UI for now
        self.UI.updateUI("BLAH", self.players)
        
        
    def displayStartupScreen(self):
        self.startScreen.show()
        self.startGame()

    def startGame(self):
        print("Starting Game with Settings")
        print(self.currentSettings)
        #Init Players
        for i in range(0, int(self.currentSettings["players"])):
            self.players.append(tp_player.Player(i))
        for j in range(4):
            self.processTurn()
            
            
    def run(self):
        #Load Settings
        self.displayStartupScreen()  
        
        


def testGame():
    print('Testing Game Module')
    game = Game()
    game.run()

if (__name__=="__main__"):
        testGame()
