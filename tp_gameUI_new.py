from tkinter import Label, Entry, StringVar, font
from tp_boardsquare import BoardSquare
from tp_diceroll import DiceRoll
import tp_gamesettings_UI as pg
from PIL import ImageTk, Image
import tp_player as pl
import tkinter as tk
import tp_rules_UI
import tp_victoryUI
import threading
import tp_settings
import tp_player
import tp_question
import random
import json
import os
import time

class GameUI:

    def __init__(self, settings):

        print('INITIALIZE GAME UI')
        # Settings from game settings UI
        self.settings = settings
        # Create list to store players
        self.players = []
        # Create list to keep player win order
        self.placement = []
        # list of directions
        dir_1 = ['cw', 'ccw', 'inner']
        exit_dir = ['up', 'down', 'left', 'right']
        # list of question categories
        ques_cat = ['Events', 'People', 'Places', 'Independence Day']
        # set current player turn
        self.currentPlayerIdx = 0
        # player num tracker
        self.player_num = {}
        # store player locations
        self.pieces = {}
        # create answer variable
        self.answer = ''
        # Distance remaning in current turn
        self.turnDistanceRemaining = 0
        # category colors
        self.cat_colors = {
                            'Events': 'white',
                            'People': 'red',
                            'Places': 'blue',
                            'Independence Day': 'green',
                            'Roll': 'grey',
                            'Free': 'orange',
                            'NONE': 'black'
                            }
        # Flag to determine if it's the last round or not
        self.lastRound = False
        # create player objects and store to list
        i = 1
        for name in list(self.settings['players'].values()):
            newPlayer = pl.Player(name)
            self.players.append(newPlayer)
            self.player_num[name] = i
            i += 1
            self.pieces[name] = (0, 0)

        # set font type and size in root window
        self.arial = font.Font(family = 'Arial', size = 14)
        self.arial_bold = font.Font(family = 'Arial', size = 14, weight = 'bold')

        # create tkinter window for game board
        self.gameBoardWindow = tk.Toplevel()
        self.gameBoardWindow.title('Trivial Purfruit')
        self.frame = tk.Frame(self.gameBoardWindow)

        # MICHAEL'S CODE       
        self.board = []
        self.initBoard()
        i = 0
        # for square in self.board:
        #     print(i)
        #     print(square)
        #     i+=1
        self.currentPlayerIdx = 0
        #########################################

        # create gameboard image
        self.rows = 7
        self.columns = 7
        self.size = 40

        self.canvas_width = self.columns*self.size
        self.canvas_height = self.rows*self.size
        self.canvas = tk.Canvas(
                                    self.gameBoardWindow,
                                    borderwidth = 3,
                                    highlightthickness = 0,
                                    width = self.canvas_width,
                                    height = self.canvas_height,
                                    background = 'black'
                                )
        self.canvas.grid(column = 0, row = 4, rowspan = 10, padx = 1, pady = 1)
        self.canvas.bind('<Configure>', self.refresh)

        self.temp_grid_loc = self.saveGridLoc()
        # store canvas locations of squares
        self.grid_loc = {
                        1: self.temp_grid_loc[1], 2: self.temp_grid_loc[2], 3: self.temp_grid_loc[3], 4: self.temp_grid_loc[4], 5: self.temp_grid_loc[5], 6: self.temp_grid_loc[6], 7: self.temp_grid_loc[7],
                        24: self.temp_grid_loc[8], 100: self.temp_grid_loc[9], 101: self.temp_grid_loc[10], 25: self.temp_grid_loc[11], 101: self.temp_grid_loc[12], 102: self.temp_grid_loc[13], 8: self.temp_grid_loc[14],
                        23: self.temp_grid_loc[15], 104: self.temp_grid_loc[16], 105: self.temp_grid_loc[17], 26: self.temp_grid_loc[18], 106: self.temp_grid_loc[19], 107: self.temp_grid_loc[20], 9: self.temp_grid_loc[21],
                        22: self.temp_grid_loc[22], 29: self.temp_grid_loc[23], 30: self.temp_grid_loc[24], 33: self.temp_grid_loc[25], 31: self.temp_grid_loc[26], 32: self.temp_grid_loc[27], 10: self.temp_grid_loc[28],
                        21: self.temp_grid_loc[29], 108: self.temp_grid_loc[30], 109: self.temp_grid_loc[31], 27: self.temp_grid_loc[32], 110: self.temp_grid_loc[33], 111: self.temp_grid_loc[34], 11: self.temp_grid_loc[35],
                        20: self.temp_grid_loc[36], 1112: self.temp_grid_loc[37], 113: self.temp_grid_loc[38], 28: self.temp_grid_loc[39], 114: self.temp_grid_loc[40], 115: self.temp_grid_loc[41], 12: self.temp_grid_loc[42],
                        19: self.temp_grid_loc[43], 18: self.temp_grid_loc[44], 17: self.temp_grid_loc[45], 16: self.temp_grid_loc[46], 15: self.temp_grid_loc[47], 14: self.temp_grid_loc[48], 13: self.temp_grid_loc[49]
                    }
        self.grid_conv_table = {
                        1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7,
                        8: 24, 9: 100, 10: 101, 11: 25, 12: 102, 13: 103, 14: 8,
                        15: 23, 16: 104, 17: 105, 18: 26, 19: 106, 20: 107, 21: 9,
                        22: 22, 23: 29, 24: 30, 25: 33, 26: 31, 27: 32, 28: 10,
                        29: 21, 30: 108, 31: 109, 32: 27, 33: 110, 34: 111, 35: 11,
                        36: 20, 37: 112, 38: 113, 39: 28, 40: 114, 41: 115, 42: 12,
                        43: 19, 44: 18, 45: 17, 46: 16, 47: 15, 48: 14, 49: 13    
                    }

        self.square_colors = {}
        for i in range(1, 50):
            if self.grid_conv_table[i] < 34:
                self.square_colors[i] = self.cat_colors[self.board[self.grid_conv_table[i]].category]
            else:
                self.square_colors[i] = 'black'

        # create player pieces and add to board
        count = 1
        for player in self.pieces.keys():
            if count == 1:
                self.player1_img = tk.PhotoImage(file = './res/player1_piece.png')
                self.addPiece(player, self.player1_img, self.players[count-1].location)
            elif count == 2:
                self.player2_img = tk.PhotoImage(file = './res/player2_piece.png')
                self.addPiece(player, self.player2_img, self.players[count-1].location)
            elif count == 3:
                self.player3_img = tk.PhotoImage(file = './res/player3_piece.png')
                self.addPiece(player, self.player3_img, self.players[count-1].location)
            elif count == 4:
                self.player4_img = tk.PhotoImage(file = './res/player4_piece.png')
                self.addPiece(player, self.player4_img, self.players[count-1].location)
            count += 1

        # place player names in UI
        if len(self.players) == 1:

            self.column = 0
            # add label for player one name
            self.player1_name = Label(self.gameBoardWindow, text = 'Player 1: ' + self.players[0].id, font = self.arial)
            self.player1_name.grid(row = 10, column = 2)
            # add label for player one chips
            self.player1_chips_label = Label(self.gameBoardWindow, text = 'Chips:', font = self.arial)
            self.player1_chips_label.grid(row = 12, column = 2)

        elif len(self.players) == 2:
            
            self.column_num = 0
            # add label for player one name
            self.player1_name = Label(self.gameBoardWindow, text = 'Player 1: ' + self.players[0].id, font = self.arial)
            self.player1_name.grid(row = 10, column = 2)
            # add label for player one chips
            self.player1_chips_label = Label(self.gameBoardWindow, text = 'Chips:', font = self.arial)
            self.player1_chips_label.grid(row = 12, column = 2)

            # create player two object
            self.p2 = pl.Player(self.settings['players']['player2'])
            # add label for player two name
            self.player2_name = Label(self.gameBoardWindow, text = 'Player 2: ' + self.players[1].id, font = self.arial)
            self.player2_name.grid(row = 10, column = 3)
            # add label for player two chips
            self.player2_chips_label = Label(self.gameBoardWindow, text = 'Chips:', font = self.arial)
            self.player2_chips_label.grid(row = 12, column = 3)

        elif len(self.players) == 3:
            
            self.column_num = 1
            # add label for player one name
            self.player1_name = Label(self.gameBoardWindow, text = 'Player 1: ' + self.players[0].id, font = self.arial)
            self.player1_name.grid(row = 10, column = 2)
            # add label for player one chips
            self.player1_chips_label = Label(self.gameBoardWindow, text = 'Chips:', font = self.arial)
            self.player1_chips_label.grid(row = 12, column = 2)

            # add label for player two name
            self.player2_name = Label(self.gameBoardWindow, text = 'Player 2: ' + self.players[1].id, font = self.arial)
            self.player2_name.grid(row = 10, column = 3)
            # add label for player two chips
            self.player2_chips_label = Label(self.gameBoardWindow, text = 'Chips:', font = self.arial)
            self.player2_chips_label.grid(row = 12, column = 3)

            # add label for player three name
            self.player3_name = Label(self.gameBoardWindow, text = 'Player 3: ' + self.players[2].id, font = self.arial)
            self.player3_name.grid(row = 10, column = 4)
            # add label for player three chips
            self.player3_chips_label = Label(self.gameBoardWindow, text = 'Chips:', font = self.arial)
            self.player3_chips_label.grid(row = 12, column = 4)

        elif len(self.players) == 4:
            
            self.column_num = 1
            # add label for player one name
            self.player1_name = Label(self.gameBoardWindow, text = 'Player 1: ' + self.players[0].id, font = self.arial)
            self.player1_name.grid(row = 10, column = 2)
            # add label for player one chips
            self.player1_chips_label = Label(self.gameBoardWindow, text = 'Chips:', font = self.arial)
            self.player1_chips_label.grid(row = 12, column = 2)

            # add label for player two name
            self.player2_name = Label(self.gameBoardWindow, text = 'Player 2: ' + self.players[1].id, font = self.arial)
            self.player2_name.grid(row = 10, column = 3)
            # add label for player two chips
            self.player2_chips_label = Label(self.gameBoardWindow, text = 'Chips:', font = self.arial)
            self.player2_chips_label.grid(row = 12, column = 3)

            # add label for player three name
            self.player3_name = Label(self.gameBoardWindow, text = 'Player 3: ' + self.players[2].id, font = self.arial)
            self.player3_name.grid(row = 10, column = 4)
            # add label for player three chips
            self.player3_chips_label = Label(self.gameBoardWindow, text = 'Chips:', font = self.arial)
            self.player3_chips_label.grid(row = 12, column = 4)

            # add label for player one name
            self.player4_name = Label(self.gameBoardWindow, text = 'Player 4: ' + self.players[3].id, font = self.arial)
            self.player4_name.grid(row = 10, column = 5)
            # add label for player four chips
            self.player4_chips_label = Label(self.gameBoardWindow, text = 'Chips:', font = self.arial)
            self.player4_chips_label.grid(row = 12, column = 5)

        # options for player to choose direction
        self.directionLabel = Label(self.gameBoardWindow, text = 'Choose Direction:', font = self.arial_bold)
        self.directionLabel.grid(row = 1, column = 1)
        self.clockwise = tk.Button(self.gameBoardWindow, text = 'Clockwise', command= lambda: self.setDirection('cw'), font = self.arial)
        self.clockwise.grid(row = 2, column = 1, sticky = 'EW')
        self.counter_clockwise = tk.Button(self.gameBoardWindow, text = 'Counter Clockwise', command= lambda: self.setDirection('ccw'), font = self.arial)
        self.counter_clockwise.grid(row = 3, column = 1, sticky = 'EW')
        self.inner = tk.Button(self.gameBoardWindow, text = 'Inner', command= lambda: self.setDirection('inner'), font = self.arial)
        self.inner.grid(row = 4, column = 1, sticky = 'EW')
        self.outer = tk.Button(self.gameBoardWindow, text = 'Outer', command= lambda: self.setDirection('outer'), font = self.arial)
        self.outer.grid(row = 5, column = 1, sticky = 'EW')

        # options for player to choose exit direction
        self.exitDirectionLabel = Label(self.gameBoardWindow, text = 'Choose Exit Direction:', font = self.arial_bold)
        self.exitDirectionLabel.grid(row = 6, column = 1)
        self.up = tk.Button(self.gameBoardWindow, text = 'Up', command = lambda: self.setExitDirection('up'), font = self.arial)
        self.up.grid(row = 7, column = 1, sticky = 'EW')
        self.down = tk.Button(self.gameBoardWindow, text = 'Down', command = lambda: self.setExitDirection('down'), font = self.arial)
        self.down.grid(row = 8, column = 1, sticky = 'EW')
        self.left = tk.Button(self.gameBoardWindow, text = 'Left', command = lambda: self.setExitDirection('left'), font = self.arial)
        self.left.grid(row = 9, column = 1, sticky = 'EW')
        self.right = tk.Button(self.gameBoardWindow, text = 'Right', command = lambda: self.setExitDirection('right'), font = self.arial)
        self.right.grid(row = 10, column = 1, sticky = 'EW')

        # options for player to choose question category
        self.catLabel = Label(self.gameBoardWindow, text = 'Choose Question Category:', font = self.arial_bold)
        self.catLabel.grid(row = 12, column = 1)
        self.event = tk.Button(self.gameBoardWindow, text = 'Events', command = lambda: self.submitCategory('Events'), font = self.arial)
        self.event.grid(row = 13, column = 1, sticky = 'EW')
        self.people = tk.Button(self.gameBoardWindow, text = 'People', command = lambda: self.submitCategory('People'), font = self.arial)
        self.people.grid(row = 14, column = 1, sticky = 'EW')
        self.places = tk.Button(self.gameBoardWindow, text = 'Places', command = lambda: self.submitCategory('Places'), font = self.arial)
        self.places.grid(row = 15, column = 1, sticky = 'EW')
        self.ind_day = tk.Button(self.gameBoardWindow, text = 'Independence Day', command = lambda: self.submitCategory('Independence Day'), font = self.arial)
        self.ind_day.grid(row = 16, column = 1, sticky = 'EW')

        # current player
        self.player_in_turn = tk.Label(self.gameBoardWindow, text = 'Current Player:', font = self.arial_bold)
        self.player_in_turn.grid(column = 2, row = 1)
        self.current_player = tk.Label(self.gameBoardWindow, text = self.players[self.currentPlayerIdx].id, font = self.arial)
        self.current_player.grid(column = 3, row = 1)

        # current action
        self.currentactionLabel = tk.Label(self.gameBoardWindow, text = 'Current Action:', font = self.arial_bold)
        self.currentactionLabel.grid(column = 2, row = 2)
        self.action = StringVar()
        self.actionLabel = Label(self.gameBoardWindow, text = self.action, font = self.arial)
        self.actionLabel.grid(column = 3, row = 2, columnspan = 3)
        self.actionLabel.configure(text = 'Player 1 Roll Die')

        # roll die
        self.rolldieText = tk.Label(self.gameBoardWindow, text = 'Dice Roll:', font = self.arial_bold)
        self.rolldieText.grid(column = 2, row = 3)
        self.roll = StringVar()
        self.rolldieResult = tk.Label(self.gameBoardWindow, text = self.roll, font = self.arial)
        self.rolldieResult.grid(column = 3, row = 3, columnspan = 3)
        self.rollButton = tk.Button(self.gameBoardWindow, text = 'Roll Die', command = self.startTurn, font = self.arial_bold)
        self.rollButton.grid(column = 3, row = 4, sticky = 'EW')
        self.rolldieResult.configure(text = '')

        # player question
        self.playerLabel = tk.Label(self.gameBoardWindow, text = 'Question:', font = self.arial_bold)
        self.playerLabel.grid(column = 2, row = 5, columnspan = 4)
        self.question = 'No Question Available'
        self.questionText = Label(self.gameBoardWindow, text = '', wraplength = 500, font = self.arial)
        self.questionText.grid(column = 2, row = 6, columnspan = 4)
        # player answer
        self.answerLabel = tk.Label(self.gameBoardWindow, text = 'Answer:', font = self.arial_bold)
        self.answerLabel.grid(column = 2, row = 7, columnspan = 4)
        self.answerEntry = Entry(self.gameBoardWindow)
        self.answerEntry.grid(column = 2, row = 8, columnspan = 4)

        # submit answer
        self.submitAnswer = tk.Button(self.gameBoardWindow, command = self.checkAnswer, text = 'Submit Answer', font = self.arial_bold)
        self.submitAnswer.grid(row = 9, column = 2, columnspan = 4)

        # add button to access dice roll
        self.rulesButton = tk.Button(self.gameBoardWindow, command = self.viewRules, text = 'View Game Rules', font = self.arial_bold)
        self.rulesButton.grid(row = 15, column = 3)

        # add button to access dice roll
        self.gameExitButton = tk.Button(self.gameBoardWindow, command = self.close, text = 'Exit Game Board', font = self.arial_bold)
        self.gameExitButton.grid(row = 16, column = 3)

        # temporary button to view victory UI
        self.victoryButton = tk.Button(self.gameBoardWindow, command = self.victory, text = 'Open Victory UI', font = self.arial_bold)
        self.victoryButton.grid(row = 17, column = 3)


    def submitCategory(self, category):

        print('Category Chosen: ', category)
        self.category = category
        self.askQuestion(category)

    def checkAnswer(self):
        print('Check answer')
        self.onSubmitAnswer(str(self.answerEntry.get()))

    def setDirection(self, direction):
        
        self.move_direction = direction
        print(self.move_direction)
        # Move the Player off the decision tile 
        currentPlayer = self.players[self.currentPlayerIdx]
        currentPlayer.location = self.board[currentPlayer.location].nextSquare[direction]
        self.distance -= 1
        self.movePlayer(self.distance, direction, currentPlayer)
        
    def setExitDirection(self, exit_direction):
        self.exit_direction = exit_direction
        # Next
        currentPlayer = self.players[self.currentPlayerIdx]
        # Move the appropriate square
        if exit_direction == 'up':
            currentPlayer.location = 26
        elif exit_direction == 'down':
            currentPlayer.location = 27
        elif exit_direction == 'left':
            currentPlayer.location = 30
        elif exit_direction == 'right':
            currentPlayer.location = 31
        self.distance -= 1
        self.movePlayer(self.distance, 'outer', currentPlayer)

    def startTurn(self):

        print('DOING A TURN')
        currentPlayer = self.players[self.currentPlayerIdx]
        hackercount = 0
        # Check if current player is active otherwise increment the index
        while (not currentPlayer.active):
            if (self.currentPlayerIdx >= len(self.players) - 1):
                self.currentPlayerIdx = 0
            else:
                self.currentPlayerIdx += 1
            currentPlayer = self.players[self.currentPlayerIdx]
            hackercount += 1
            #Infiniate loops are bad
            if (hackercount > 10):
                return
        self.current_player.configure(text = currentPlayer.id)
        print('Player ' + str(currentPlayer.id) + "'s turn")
        # Roll the Dice
        self.distance = DiceRoll.rollDice()
        self.rolldieResult.configure(text = str(self.distance))

        # Set the direction Buttons up for The beginning of the move
        self.setValidDirections(currentPlayer.location)
        return
    
    def getCategory(self):
        # Get category for upcoming question
        currentPlayer = self.players[self.currentPlayerIdx]
        
        category = ''
        if currentPlayer.location == 33:
            # Enable the category buttons with the proper message
            # If chips < 4, choose the category, 4 or more, opponent chooses
            if (len(currentPlayer.chips) < 4):
                # category = input('Choose a Category: Events, Places, Independence Day, People: ')
                # Wait for category callback
                self.actionLabel.configure(text = 'Choose a Category: Events, Places, Independence Day, People')
                self.disableDirectionButtons()
                return
            else:
                # category = input('(Opponent) Choose final question Category:  Events, Places, Independence Day, People: ')
                # Wait for category callback
                self.actionLabel.configure(text = 'Choose a Category: Events, Places, Independence Day, People')
                self.disableDirectionButtons()
                return
        else:
            category = self.board[currentPlayer.location].category
            print('Category Chosen: ', category)
            self.askQuestion(category)
    
    def askQuestion(self, category):

        questionGenerator = tp_question.QuestionGenerator()
        question = {}
        if category == 'Roll':
            # Need to Update the UI and display roll again message here
            print('ROLL AGAIN')
            self.actionLabel.configure(text = 'Roll Again')
            self.action.set('Roll Again')
            self.disableDirectionButtons()
            return
        else:
            self.actionLabel.configure(text = 'Answer Question')
            question = questionGenerator.getRandomQuestion(category)

        # Display Question and Prompt for Answer
        # needs to be replaced by with UI loop integration
        self.actionLabel.configure(text = 'Answer Question')
        self.disableAllButtons()
        self.currentquestion = question
        self.questionText.configure(text = question['question'])
        print(question['question'])
        
    def onSubmitAnswer(self, ans):

        currentPlayer = self.players[self.currentPlayerIdx]
        correct = (ans == self.currentquestion['answer'])
        #  Below is so one can mash enter to test, uncomment for testing:
        # correct = True
        if (correct):
            
            print('Correct')
            self.actionLabel.configure(text = 'Answer Correct, Roll Again')
            self.questionText.configure(text = '')
            self.answerEntry.delete(0, 'end')
            # Check if this was the player's final question
            if (currentPlayer.location == 33 and len(currentPlayer.chips) == 4):
            # Below for testing, removes the last square condition to speed to victory logic
            #if (len(currentPlayer.chips) == 1):
                # Add player to the placement array, set them inactive
                self.placement.append(self.players[self.currentPlayerIdx])
                self.players[self.currentPlayerIdx].active = False
                text = currentPlayer.id + ' obtained all chips. Next player roll die.'
                self.actionLabel.configure(text = text)
                # Set the last turn round
                self.lastRound = True
                if self.player_num[currentPlayer.id] == 1:
                    # remove player 1 from UI
                    self.player1_name.destroy()
                    self.player1_chips_label.destroy()
                    self.chip1_img.destroy()
                    self.canvas.delete(currentPlayer.id)
                elif self.player_num[currentPlayer.id] == 2:
                    # remove player 2 from UI
                    self.player2_name.destroy()
                    self.player2_chips_label.destroy()
                    self.chip2_img.destroy()
                    self.canvas.delete(currentPlayer.id)
                elif self.player_num[currentPlayer.id] == 3:
                    # remove player 3 from UI
                    self.player3_name.destroy()
                    self.player3_chips_label.destroy()
                    self.chip3_img.destroy()
                    self.canvas.delete(currentPlayer.id)
                elif self.player_num[currentPlayer.id] == 4:
                    # remove player 4 from UI
                    self.player4_name.destroy()
                    self.player4_chips_label.destroy()
                    self.chip4_img.destroy()
                    self.canvas.delete(currentPlayer.id)
            #Otherwise add chip
            else:
                currentPlayer.addChip(self.currentquestion['category'])
        else:
            print('Incorrect')
            if len(self.players) == 2:
                if self.player_num[currentPlayer.id] == 1:
                    next_player = self.players[1].id
                elif self.player_num[currentPlayer.id] == 2:
                    next_player = self.players[0].id
            elif len(self.players) == 3:
                if self.player_num[currentPlayer.id] == 1:
                    next_player = self.players[1].id
                elif self.player_num[currentPlayer.id] == 2:
                    next_player = self.players[2].id
                elif self.player_num[currentPlayer.id] == 3:
                    next_player = self.players[0].id
            elif len(self.players) == 4:
                if self.player_num[currentPlayer.id] == 1:
                    next_player = self.players[1].id
                elif self.player_num[currentPlayer.id] == 2:
                    next_player = self.players[2].id
                elif self.player_num[currentPlayer.id] == 3:
                    next_player = self.players[3].id
                elif self.player_num[currentPlayer.id] == 4:
                    next_player = self.players[0].id
            text = "Answer Incorrect, " + next_player + " Roll Die"
            self.actionLabel.configure(text = text)
            self.questionText.configure(text = '')
            self.current_player.configure(text = '')
            self.answerEntry.delete(0, 'end')
            # Move the player off the center square if this was a final attempt
            if (currentPlayer.location == 33 and len(currentPlayer.chips) == 4):
                self.distance = 1
                self.setValidDirections(33)
            # If this is the last round and the player got it wrong, then they are done
            if (self.lastRound):
                self.players[self.currentPlayerIdx].active = False
            # Move to the next player before starting the next turn if we got the wrong answer
            if (self.currentPlayerIdx >= len(self.players) - 1):
                self.currentPlayerIdx = 0
            else:
                self.currentPlayerIdx += 1
        # Check if there are no more active players to end the game
        endCheck = False
        for player in self.players:
            if player.active:
                endCheck = True
        if (not endCheck):
            self.actionLabel.configure(text = 'GAME OVER, VICTORY UI OPENS')
            self.rolldieResult.configure(text = '')
            self.disableAllButtons()
            self.showVictoryScreen()
            return
        #Update the UI State
        if self.player_num[currentPlayer.id] == 1:
            # update player 1 in UI
            for file in os.listdir('./res'):
                if file.endswith(".jpg") or file.endswith(".png"):
                    filename, file_extension = os.path.splitext(file)
                    filename = filename.split('_')
                    filename = ['Independence Day' if word == 'IndependenceDay' else word for word in filename]
                    if sorted(filename) == sorted(self.players[0].chips):
                        self.img1 = Image.open('./res/' + file)
                        self.photo1 = ImageTk.PhotoImage(self.img1)
                        self.chip1_img = Label(self.gameBoardWindow, image = self.photo1)
                        self.chip1_img.grid(row = 13, column = 1)
        elif self.player_num[currentPlayer.id] == 2:
            # update player 2 in UI
            for file in os.listdir('./res'):
                if file.endswith(".jpg") or file.endswith(".png"):
                    filename, file_extension = os.path.splitext(file)
                    filename = filename.split('_')
                    filename = ['Independence Day' if word == 'IndependenceDay' else word for word in filename]
                    if sorted(filename) == sorted(self.players[1].chips):
                        self.img2 = Image.open('./res/' + file)
                        self.photo2 = ImageTk.PhotoImage(self.img2)
                        self.chip2_img = Label(self.gameBoardWindow, image = self.photo2)
                        self.chip2_img.grid(row = 13, column = 2)
        elif self.player_num[currentPlayer.id] == 3:
            # update player 3 in UI
            for file in os.listdir('./res'):
                if file.endswith(".jpg") or file.endswith(".png"):
                    filename, file_extension = os.path.splitext(file)
                    filename = filename.split('_')
                    filename = ['Independence Day' if word == 'IndependenceDay' else word for word in filename]
                    if sorted(filename) == sorted(self.players[2].chips):
                        self.img3 = Image.open('./res/' + file)
                        self.photo3 = ImageTk.PhotoImage(self.img3)
                        self.chip3_img = Label(self.gameBoardWindow, image = self.photo3)
                        self.chip3_img.grid(row = 13, column = 3)
        elif self.player_num[currentPlayer.id] == 4:
            # update player 4 in UI
            for file in os.listdir('./res'):
                if file.endswith(".jpg") or file.endswith(".png"):
                    filename, file_extension = os.path.splitext(file)
                    filename = filename.split('_')
                    filename = ['Independence Day' if word == 'IndependenceDay' else word for word in filename]
                    if sorted(filename) == sorted(self.players[3].chips):
                        self.img4 = Image.open('./res/' + file)
                        self.photo4 = ImageTk.PhotoImage(self.img4)
                        self.chip4_img = Label(self.gameBoardWindow, image = self.photo4)
                        self.chip4_img.grid(row = 13, column = 4)

        self.rolldieResult.configure(text = '')
        self.rollButton.configure(state = 'normal')
        # time.sleep(1)

    def setValidDirections(self, currlocation, exiting=False):

        # enable buttons
        self.enableAllButtons()
        # Return the valid directions given a location
        # Disable invalid buttons in the UI
        if currlocation < 25:
            if currlocation in [4,10,16,22]:
                self.actionLabel.configure(text = 'Choose Direction (cw, ccw, inner)')
                self.outer.configure(state = 'disabled')
                self.up.configure(state = 'disabled')
                self.down.configure(state = 'disabled')
                self.left.configure(state = 'disabled')
                self.right.configure(state = 'disabled')
                return ['cw','ccw','inner']
            else:
                self.actionLabel.configure(text = 'Choose Direction (cw, ccw)')
                self.inner.configure(state = 'disabled')
                self.outer.configure(state = 'disabled')
                self.up.configure(state = 'disabled')
                self.down.configure(state = 'disabled')
                self.left.configure(state = 'disabled')
                self.right.configure(state = 'disabled')
                return ['cw','ccw']
        elif currlocation < 33:
            self.actionLabel.configure(text = 'Choose Direction (inner, outer)')
            self.clockwise.configure(state = 'disabled')
            self.counter_clockwise.configure(state = 'disabled')
            self.up.configure(state = 'disabled')
            self.down.configure(state = 'disabled')
            self.left.configure(state = 'disabled')
            self.right.configure(state = 'disabled')
            return ['inner','outer']
        else:
            self.actionLabel.configure(text = 'Choose Exit Direction (up, down, left, right)')
            self.clockwise.configure(state = 'disabled')
            self.counter_clockwise.configure(state = 'disabled')
            self.inner.configure(state = 'disabled')
            self.outer.configure(state = 'disabled')
            return ['up','down','left','right']

    def onExitSelect(self):
        currentPlayer = self.players[self.currentPlayerIdx]
        return 0
    
    def onDirectionSelect(self, distance, direction, player):
        return 0
        
    def movePlayer(self, distance, direction, player):

        # Moves the Player  certain distance
        for i in range (0, distance):
            # Increment Player Location
            print('At' + str(player.location))
            print('To Move: ' + str(distance - i))
            currsquare = self.board[player.location]
            if (player.location in [4,10,16,22,33]):
                if direction == 'outer':
                    self.setValidDirections(player.location, True)
                    return
                else:
                    self.setValidDirections(player.location)
                    return
            else:
                player.location = currsquare.nextSquare[direction]
            self.lastSquare = self.board.index(currsquare) # Record the last sqaure
            self.distance -= 1
        print('Final Player Location ' + str(player.location))

        # move player piece on game board
        self.placePiece(player.id, player.location)

        # Continue the turn logic
        self.getCategory()

    def initBoard(self):
        # Bad hard coded board init
        cats = ['Events','Places','Independence Day', 'People']
        self.board.append(BoardSquare('NONE', -1, -1, -1))
        self.board.append(BoardSquare(cats[1%4], 2, 24))
        for i in range (2,24):
            self.board.append(BoardSquare(cats[i%4], i+1, i-1))
        self.board.append(BoardSquare(cats[24%4], 1, 23))
        # Now add the central squares and set up the paths
        self.board.append(BoardSquare(cats[25%4], -1, -1, 26, 4))
        self.board.append(BoardSquare(cats[26%4], -1, -1, 33, 25))
        self.board.append(BoardSquare(cats[27%4], -1, -1, 33, 28))
        self.board.append(BoardSquare(cats[28%4], -1, -1, 27, 11))
        self.board.append(BoardSquare(cats[29%4], -1, -1, 30, 22))
        self.board.append(BoardSquare(cats[30%4], -1, -1, 33, 29))
        self.board.append(BoardSquare(cats[31%4], -1, -1, 33, 32))
        self.board.append(BoardSquare(cats[32%4], -1, -1, 31, 10))
        
        self.board[4].nextSquare['inner'] = 25
        self.board[10].nextSquare['inner'] = 32
        self.board[16].nextSquare['inner'] = 28
        self.board[22].nextSquare['inner'] = 29
        # Add the final square
        finalsquare = BoardSquare('Free', 33, 33, 33)
        finalsquare.isFinal = True
        self.board.append(finalsquare)
        # Now adjust for the roll again squares/categories, etc
        # Roll again on 3, 5, 8, 11, 14, 17, 21, 23
        self.board[3].category = 'Roll'
        self.board[5].category = 'Roll'
        self.board[8].category = 'Roll'
        self.board[11].category = 'Roll'
        self.board[14].category = 'Roll'
        self.board[17].category = 'Roll'
        self.board[21].category = 'Roll'
        self.board[23].category = 'Roll'
        
        # 10 Becomes category 3, 16 becomes Cat 1 
        self.board[10].category = cats[3]
        self.board[16].category = cats[1]

    def showUI(self):
        # Text based State UI for now
        for player in self.players:
            print(player)

    def refresh(self, event):

        xsize = int((event.width-1)/self.columns)
        ysize = int((event.height-1)/self.rows)
        self.size = min(xsize, ysize)
        self.canvas.delete('square')
        i = 1
        for row in range(self.rows):
            for col in range(self.columns):
                x1 = (col * self.size)
                y1 = (row * self.size)
                x2 = x1 + self.size
                y2 = y1 + self.size
                self.canvas.create_text(x1+30, y1+30, text = str(self.grid_conv_table[i]))
                self.canvas.create_rectangle(x1, y1, x2, y2, outline = 'black', fill = self.square_colors[i], tags = 'square')
                i += 1
        self.canvas.tag_raise('piece')
        self.canvas.tag_lower('square')
        self.saveGridLoc()

    def saveGridLoc(self):

        grid_loc = {}
        i = 1
        for row in range(self.rows):
            for col in range(self.columns):
                x1 = (col * self.size)
                y1 = (row * self.size)
                x2 = x1 + self.size
                y2 = y1 + self.size
                grid_loc[i] = (x1, y1)
                i += 1

        return grid_loc

    def placePiece(self, name, location):

        # place piece at row/column
        self.pieces[name] = (self.grid_loc[location][0], self.grid_loc[location][1])

        if self.player_num[name] == 1:
            self.canvas.coords(name, self.grid_loc[location][0] + 10, self.grid_loc[location][1] + 10)
        elif self.player_num[name] == 2:
            self.canvas.coords(name, self.grid_loc[location][0] + 30, self.grid_loc[location][1] + 10)
        elif self.player_num[name] == 3:
            self.canvas.coords(name, self.grid_loc[location][0] + 10, self.grid_loc[location][1] + 30)
        elif self.player_num[name] == 4:
            self.canvas.coords(name, self.grid_loc[location][0] + 30, self.grid_loc[location][1] + 30)

    def addPiece(self, name, image, location):

        # add player piece to board
        print('Adding Player {} to Board'.format(name))
        self.canvas.create_image(20, 20, image = image, tags = (name, 'piece'), anchor = 'c')
        self.placePiece(name, location)

    def disableCatButtons(self):

        self.event.configure(state = 'disabled')
        self.people.configure(state = 'disabled')
        self.places.configure(state = 'disabled')
        self.ind_day.configure(state = 'disabled')

    def disableDirectionButtons(self):

        self.clockwise.configure(state = 'disabled')
        self.counter_clockwise.configure(state = 'disabled')
        self.outer.configure(state = 'disabled')
        self.inner.configure(state = 'disabled')
        self.up.configure(state = 'disabled')
        self.down.configure(state = 'disabled')
        self.left.configure(state = 'disabled')
        self.right.configure(state = 'disabled')

    def disableAllButtons(self):

        self.rollButton.configure(state = 'disabled')
        self.clockwise.configure(state = 'disabled')
        self.counter_clockwise.configure(state = 'disabled')
        self.outer.configure(state = 'disabled')
        self.inner.configure(state = 'disabled')
        self.up.configure(state = 'disabled')
        self.down.configure(state = 'disabled')
        self.left.configure(state = 'disabled')
        self.right.configure(state = 'disabled')
        self.event.configure(state = 'disabled')
        self.people.configure(state = 'disabled')
        self.places.configure(state = 'disabled')
        self.ind_day.configure(state = 'disabled')

    def enableAllButtons(self):

        self.rollButton.configure(state = 'normal')
        self.clockwise.configure(state = 'normal')
        self.counter_clockwise.configure(state = 'normal')
        self.outer.configure(state = 'normal')
        self.inner.configure(state = 'normal')
        self.up.configure(state = 'normal')
        self.down.configure(state = 'normal')
        self.left.configure(state = 'normal')
        self.right.configure(state = 'normal')
        self.event.configure(state = 'normal')
        self.people.configure(state = 'normal')
        self.places.configure(state = 'normal')
        self.ind_day.configure(state = 'normal')
            
    def showVictoryScreen(self):
        # Text based State UI for now, add real screen later
        print('Game Over')
        print('Rankings')
        i = 0
        for player in self.placement:
            print('No ' + str(i) +': Player ' + str(player.id))
            i += 1
        self.victory()


    def victory(self):

        print('Close game board and proceed to Victory UI')
        self.gameBoardWindow.destroy()
        vic = tp_victoryUI.Victory(self.placement)

    def viewRules(self):
        rules_window = tp_rules_UI.RulesUI()

    def close(self):
        print('Close Game Board')
        self.gameBoardWindow.destroy()
        for player in self.players:
            del player

