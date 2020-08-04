import tp_settings
import tp_player
import tp_gameUI
import tp_startScreen
import tp_question
from tp_diceroll import DiceRoll
from tp_boardsquare import BoardSquare
import time

class Game:

    def __init__(self):
        print("GAME INIT")
        #Init global UI/objects here
        self.players = []
        self.placement = []
        self.UI = tp_gameUI.GameUI()
        self.startScreen = tp_startScreen.StartScreen(self)
        self.board = []
        self.initBoard()
        for square in self.board:
            print(square)
        self.currentPlayerIdx = 0


    def processTurn(self):
        print('DOING A TURN')
        currentPlayer = self.players[self.currentPlayerIdx]
        # Roll the Dice
        print('ROLL DICE: ')
        distance = DiceRoll.rollDice()
        print('ROLLED ' + str(distance))
        #dire = input('Choose Direction (cw, ccw)')
        #if dire not in ['cw','ccw']: # Test code so I can mash enter
         #   dire = 'cw'
        # Move the player that far
        self.movePlayer(distance, currentPlayer)
        # Question Answering and Chip Logic
        questionGenerator = tp_question.QuestionGenerator()
        question = questionGenerator.getRandomQuestion(self.board[currentPlayer.location].category)
        # question = {'question':'Blah', 'answer':'Blah'}
        # Display Question and Prompt for Answer
        # needs to be replaced by with UI loop integration
        print(question['question'])
        ans = input('Input Answer:')
        correct = (ans == question['answer'])
        if (correct): # This is so I can mash enter to test, remove later
            currentPlayer.addChip(self.board[currentPlayer.location].category)
        

        #Updat the UI State
        self.showUI()
        time.sleep(2)
        # Move to the next player before starting the next turn if we got the wrong answer
        if (not correct):
            if (self.currentPlayerIdx >= len(self.players) - 1):
                    self.currentPlayerIdx = 0
            else:
                self.currentPlayerIdx += 1

        

    def movePlayer(self, distance, player):
        # Bad Code Reqplication but it's almost 10 PM and I can't figure out how to rework it off the top of my head
        direction =''
        lastSquare = 0 # None
        if player.location < 17:
            if player.location in [3,7,11,15]:
                direction = input('Choose Direction (cw, ccw, inner)')
            else:
                direction = input('Choose Direction (cw, ccw)')
        elif player.location < 21:
            direction = input('Choose Direction (inner, outer)')
        else:
            direction = input('Choose Exit direction')
            if direction == 'up':
                player.location = 17
            elif direction == 'down':
                player.location = 19
            elif direction == 'left':
                player.location = 20
            elif direction == 'right':
                player.location = 18
            distance -= 1 # This logic auto moves you by one square
            direction = 'outer'
        for i in range (0, distance):
            # Increment Player Location
            print(player.location)
            currsquare = self.board[player.location]
            if (currsquare.isFinal):
                while (player.location == 21):
                    dire = ''
                    dire = input('Choose Exit direction: ')
                    if dire == 'up':
                        if lastSquare != 17:
                            player.location = 17
                        else:
                            print('Cannot go backwards')
                    elif dire == 'down':
                        player.location = 19
                        if (lastSquare != 19):
                            player.location = 19
                        else:
                            print('Cannot go backwards')
                    elif dire == 'left':
                        if (lastSquare != 20):
                            player.location = 20
                        else:
                            print('Cannot go backwards')
                    elif dire == 'right':
                        if (lastSquare != 18):
                            player.location = 18
                        else:
                            print('Cannot go backwards')
                    else:
                        print('Invalid Input')
                direction = 'outer'
            elif (currsquare.nextSquare['inner'] != -1): 
                if (direction in ['cw','ccw']): # A square that leads inwards moving aroudn board
                    center = input('Head towards the center (y/n)?')
                    if center == 'y':
                        player.location = currsquare.nextSquare['inner']
                        direction = 'inner'
                    else:
                        player.location = currsquare.nextSquare[direction]
                elif (player.location < 17 and i != 0): # Just came out
                    direction = input('Choose Direction (cw, ccw)')
                    player.location = currsquare.nextSquare[direction]
                else: # Moving along inner path
                    player.location = currsquare.nextSquare[direction]
            else:
                player.location = currsquare.nextSquare[direction]
            lastSquare = self.board.index(currsquare) # Record the last sqaure
            
            print(player.location)
            print('-----------------------------')
            
        

    def showUI(self):
        # Text based State UI for now
        for player in self.players:
            print(player)
        
        
    def displayStartupScreen(self):
        self.startScreen.show()
        self.startGame()

    def startGame(self):
        print("Starting Game with Settings")
        print(self.currentSettings)
        #Init Players
        for i in range(0, int(self.currentSettings["players"])):
            newPlayer = tp_player.Player(i)
            newPlayer.location = 21
            self.players.append(newPlayer)
            
        for j in range(10):
            self.processTurn()
            
            
    def run(self):
        #Load Settings
        self.displayStartupScreen()

    def initBoard(self):
        # Bad hard coded board init
        cats = ['Events','Places','Independence Day', 'People']
        self.board.append(BoardSquare('NONE', -1, -1, -1))
        self.board.append(BoardSquare(cats[1%4], 2, 16))
        for i in range (2,16):
            self.board.append(BoardSquare(cats[i%4], i+1, i-1))
        self.board.append(BoardSquare(cats[16%4], 1, 15))
        # Now add the central squares and set up the paths
        # cw becomes towards center, ccw is outward
        self.board.append(BoardSquare(cats[17%4], -1, -1, 21, 3))
        self.board.append(BoardSquare(cats[18%4], -1, -1, 21, 7))
        self.board.append(BoardSquare(cats[19%4], -1, -1, 21, 11))
        self.board.append(BoardSquare(cats[20%4], -1, -1, 21, 15))
        self.board[3].nextSquare['inner'] = 17
        self.board[7].nextSquare['inner'] = 18
        self.board[11].nextSquare['inner'] = 19
        self.board[15].nextSquare['inner'] = 20
        # Add the final square
        finalsquare = BoardSquare('Free', 21, 21, 21)
        finalsquare.isFinal = True
        self.board.append(finalsquare)


def testGame():
    print('Testing Game Module')
    game = Game()
    game.run()

if (__name__=="__main__"):
        testGame()
