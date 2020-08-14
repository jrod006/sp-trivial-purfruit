from tkinter import Label, Entry, StringVar, font
from tp_boardsquare import BoardSquare
from tp_diceroll import DiceRoll
import tp_gamesettings_UI as pg
from PIL import ImageTk, Image
import tp_player as pl
import tkinter as tk
import tp_rules_UI
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

        # create player objects and store to list
        i = 1
        for name in list(self.settings['players'].values()):
            newPlayer = pl.Player(name)
            self.players.append(newPlayer)
            self.player_num[name] = i
            i += 1
            self.pieces[name] = (0, 0)

        print('List of player order:')
        print(self.player_num)
        print('List of player starting locations:')
        print(self.pieces)

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
        for square in self.board:
            print(i)
            print(square)
            i+=1
        self.currentPlayerIdx = 0
        #########################################

        # create gameboard image
        self.rows = 5
        self.columns = 5
        self.size = 60
        # hard coded colors for game board
        self.colors = {
                        1: 'blue', 2: 'green', 3: 'red', 4: 'white', 5: 'blue',
                        6: 'green', 7: 'black', 8: 'white', 9: 'black', 10: 'green',
                        11: 'red', 12: 'white', 13: 'orange', 14: 'green', 15: 'red',
                        16: 'white', 17: 'black', 18: 'green', 19: 'black', 20: 'white',
                        21: 'blue', 22: 'white', 23: 'red', 24: 'green', 25: 'blue'
        }
        # hard coded colors to get category based on Square color
        # the labels above need to match these
        self.color_names = {
                        1: 'Red', 2: 'Blue', 3: 'White', 4: 'Green', 5: 'Grey',
                        6: 'White', 7: 'Black', 8: 'Red', 9: 'Black', 10: 'White',
                        11: 'Blue', 12: 'Grey', 13: 'Orange', 14: 'Blue', 15: 'Green',
                        16: 'White', 17: 'Black', 18: 'Green', 19: 'Black', 20: 'Red',
                        21: 'Grey', 22: 'Green', 23: 'Red', 24: 'Grey', 25: 'Blue'
                    }

        self.canvas_width = self.columns*self.size
        self.canvas_height = self.rows*self.size
        self.canvas = tk.Canvas(
                                    self.gameBoardWindow,
                                    borderwidth = 5,
                                    highlightthickness = 0,
                                    width = self.canvas_width,
                                    height = self.canvas_height,
                                    background = 'black'
                                )
        self.canvas.grid(column = 0, padx = 2, pady = 2)
        self.canvas.bind('<Configure>', self.refresh)

        self.temp_grid_loc = self.saveGridLoc()
        print(self.temp_grid_loc)
        # store canvas locations of squares
        self.grid_loc = {
                        1: self.temp_grid_loc[1], 2: self.temp_grid_loc[2], 3: self.temp_grid_loc[3], 4: self.temp_grid_loc[4], 5: self.temp_grid_loc[5],
                        16: self.temp_grid_loc[6], 101: self.temp_grid_loc[7], 17: self.temp_grid_loc[8], 102: self.temp_grid_loc[9], 6: self.temp_grid_loc[10],
                        15: self.temp_grid_loc[11], 20: self.temp_grid_loc[12], 21: self.temp_grid_loc[13], 18: self.temp_grid_loc[14], 7: self.temp_grid_loc[15],
                        14: self.temp_grid_loc[16], 103: self.temp_grid_loc[17], 19: self.temp_grid_loc[18], 104: self.temp_grid_loc[19], 8: self.temp_grid_loc[20],
                        13: self.temp_grid_loc[21], 12: self.temp_grid_loc[22], 11: self.temp_grid_loc[23], 10: self.temp_grid_loc[24], 9: self.temp_grid_loc[25],
                    }
        self.grid_conv_table = {
                        1: '1', 2: '2', 3: '3', 4: '4', 5: '5',
                        6: '16', 7: '101', 8: '17', 9: '102', 10: '6',
                        11: '15', 12: '20', 13: '21', 14: '18', 15: '7',
                        16: '14', 17: '103', 18: '19', 19: '104', 20: '8',
                        21: '13', 22: '12', 23: '11', 24: '10', 25: '9'    
                    }

        # create player pieces and add to board
        print()
        count = 1
        for player in self.pieces.keys():
            if count == 1:
                self.player1_img = tk.PhotoImage(file = './res/player1_piece.png')
                self.addPiece(player, self.player1_img)
            elif count == 2:
                self.player2_img = tk.PhotoImage(file = './res/player2_piece.png')
                self.addPiece(player, self.player2_img)
            elif count == 3:
                self.player3_img = tk.PhotoImage(file = './res/player3_piece.png')
                self.addPiece(player, self.player3_img)
            elif count == 4:
                self.player4_img = tk.PhotoImage(file = './res/player4_piece.png')
                self.addPiece(player, self.player4_img)
            count += 1

        # place player names in UI
        if len(self.players) == 1:

            self.column = 0
            # add label for player one name
            self.player1_name = Label(self.gameBoardWindow, text = 'Player 1: ' + self.players[0].id, font = self.arial)
            self.player1_name.grid(row = 10, column = 1)
            # add label for player one chips
            self.player1_chips_label = Label(self.gameBoardWindow, text = 'Chips:', font = self.arial)
            self.player1_chips_label.grid(row = 12, column = 1)

        elif len(self.players) == 2:
            
            self.column_num = 0
            # add label for player one name
            self.player1_name = Label(self.gameBoardWindow, text = 'Player 1: ' + self.players[0].id, font = self.arial)
            self.player1_name.grid(row = 10, column = 1)
            # add label for player one chips
            self.player1_chips_label = Label(self.gameBoardWindow, text = 'Chips:', font = self.arial)
            self.player1_chips_label.grid(row = 12, column = 1)

            # create player two object
            self.p2 = pl.Player(self.settings['players']['player2'])
            # add label for player two name
            self.player2_name = Label(self.gameBoardWindow, text = 'Player 2: ' + self.players[1].id, font = self.arial)
            self.player2_name.grid(row = 10, column = 2)
            # add label for player two chips
            self.player2_chips_label = Label(self.gameBoardWindow, text = 'Chips:', font = self.arial)
            self.player2_chips_label.grid(row = 12, column = 2)

        elif len(self.players) == 3:
            
            self.column_num = 1
            # add label for player one name
            self.player1_name = Label(self.gameBoardWindow, text = 'Player 1: ' + self.players[0].id, font = self.arial)
            self.player1_name.grid(row = 10, column = 1)
            # add label for player one chips
            self.player1_chips_label = Label(self.gameBoardWindow, text = 'Chips:', font = self.arial)
            self.player1_chips_label.grid(row = 12, column = 1)

            # add label for player two name
            self.player2_name = Label(self.gameBoardWindow, text = 'Player 2: ' + self.players[1].id, font = self.arial)
            self.player2_name.grid(row = 10, column = 2)
            # add label for player two chips
            self.player2_chips_label = Label(self.gameBoardWindow, text = 'Chips:', font = self.arial)
            self.player2_chips_label.grid(row = 12, column = 2)

            # add label for player three name
            self.player3_name = Label(self.gameBoardWindow, text = 'Player 3: ' + self.players[2].id, font = self.arial)
            self.player3_name.grid(row = 10, column = 3)
            # add label for player three chips
            self.player3_chips_label = Label(self.gameBoardWindow, text = 'Chips:', font = self.arial)
            self.player3_chips_label.grid(row = 12, column = 3)

        elif len(self.players) == 4:
            
            self.column_num = 1
            # add label for player one name
            self.player1_name = Label(self.gameBoardWindow, text = 'Player 1: ' + self.players[0].id, font = self.arial)
            self.player1_name.grid(row = 10, column = 1)
            # add label for player one chips
            self.player1_chips_label = Label(self.gameBoardWindow, text = 'Chips:', font = self.arial)
            self.player1_chips_label.grid(row = 12, column = 1)

            # add label for player two name
            self.player2_name = Label(self.gameBoardWindow, text = 'Player 2: ' + self.players[1].id, font = self.arial)
            self.player2_name.grid(row = 10, column = 2)
            # add label for player two chips
            self.player2_chips_label = Label(self.gameBoardWindow, text = 'Chips:', font = self.arial)
            self.player2_chips_label.grid(row = 12, column = 2)

            # add label for player three name
            self.player3_name = Label(self.gameBoardWindow, text = 'Player 3: ' + self.players[2].id, font = self.arial)
            self.player3_name.grid(row = 10, column = 3)
            # add label for player three chips
            self.player3_chips_label = Label(self.gameBoardWindow, text = 'Chips:', font = self.arial)
            self.player3_chips_label.grid(row = 12, column = 3)

            # add label for player one name
            self.player4_name = Label(self.gameBoardWindow, text = 'Player 4: ' + self.players[3].id, font = self.arial)
            self.player4_name.grid(row = 10, column = 4)
            # add label for player four chips
            self.player4_chips_label = Label(self.gameBoardWindow, text = 'Chips:', font = self.arial)
            self.player4_chips_label.grid(row = 12, column = 4)

        # options for player to choose direction
        self.directionLabel = Label(self.gameBoardWindow, text = 'Choose Direction:', font = self.arial_bold)
        self.directionLabel.grid(row = 1, column = 0)
        self.clockwise = tk.Button(self.gameBoardWindow, text = 'Clockwise', command= lambda: self.setDirection('cw'), font = self.arial)
        self.clockwise.grid(row = 2, column = 0, sticky = 'EW')
        self.counter_clockwise = tk.Button(self.gameBoardWindow, text = 'Counter Clockwise', command= lambda: self.setDirection('ccw'), font = self.arial)
        self.counter_clockwise.grid(row = 3, column = 0, sticky = 'EW')
        self.inner = tk.Button(self.gameBoardWindow, text = 'Inner', command= lambda: self.setDirection('inner'), font = self.arial)
        self.inner.grid(row = 4, column = 0, sticky = 'EW')
        self.outer = tk.Button(self.gameBoardWindow, text = 'Outer', command= lambda: self.setDirection('outer'), font = self.arial)
        self.outer.grid(row = 5, column = 0, sticky = 'EW')

        # options for player to choose exit direction
        self.exitDirectionLabel = Label(self.gameBoardWindow, text = 'Choose Exit Direction:', font = self.arial_bold)
        self.exitDirectionLabel.grid(row = 6, column = 0)
        self.up = tk.Button(self.gameBoardWindow, text = 'Up', command = lambda: self.setExitDirection('up'), font = self.arial)
        self.up.grid(row = 7, column = 0, sticky = 'EW')
        self.down = tk.Button(self.gameBoardWindow, text = 'Down', command = lambda: self.setExitDirection('down'), font = self.arial)
        self.down.grid(row = 8, column = 0, sticky = 'EW')
        self.left = tk.Button(self.gameBoardWindow, text = 'Left', command = lambda: self.setExitDirection('left'), font = self.arial)
        self.left.grid(row = 9, column = 0, sticky = 'EW')
        self.right = tk.Button(self.gameBoardWindow, text = 'Right', command = lambda: self.setExitDirection('right'), font = self.arial)
        self.right.grid(row = 10, column = 0, sticky = 'EW')

        # button to submit move
        # self.submitMove = tk.Button(self.gameBoardWindow, text = 'Submit Move', command = self.func, font = self.arial)
        # self.submitMove.grid(row = 11, column = 0, sticky = 'EW')
        # self.submitMove.bind(<Return>, self.func)

        # options for player to choose question category
        self.catLabel = Label(self.gameBoardWindow, text = 'Choose Question Category:', font = self.arial_bold)
        self.catLabel.grid(row = 12, column = 0)
        self.event = tk.Button(self.gameBoardWindow, text = 'Events', command = lambda: self.submitCategory('Events'), font = self.arial)
        self.event.grid(row = 13, column = 0, sticky = 'EW')
        self.people = tk.Button(self.gameBoardWindow, text = 'People', command = lambda: self.submitCategory('People'), font = self.arial)
        self.people.grid(row = 14, column = 0, sticky = 'EW')
        self.places = tk.Button(self.gameBoardWindow, text = 'Places', command = lambda: self.submitCategory('Places'), font = self.arial)
        self.places.grid(row = 15, column = 0, sticky = 'EW')
        self.ind_day = tk.Button(self.gameBoardWindow, text = 'Independence Day', command = lambda: self.submitCategory('Independence Day'), font = self.arial)
        self.ind_day.grid(row = 16, column = 0, sticky = 'EW')

        # current player
        self.player_in_turn = tk.Label(self.gameBoardWindow, text = 'Current Player:', font = self.arial_bold)
        self.player_in_turn.grid(column = 1, row = 1)
        self.current_player = tk.Label(self.gameBoardWindow, text = self.players[self.currentPlayerIdx].id, font = self.arial)
        self.current_player.grid(column = 2, row = 1)

        # current action
        self.currentactionLabel = tk.Label(self.gameBoardWindow, text = 'Current Action:', font = self.arial_bold)
        self.currentactionLabel.grid(column = 1, row = 2)
        self.action = StringVar()
        self.actionLabel = Label(self.gameBoardWindow, text = self.action, font = self.arial)
        self.actionLabel.grid(column = 2, row = 2, columnspan = 3)

        # roll die
        self.rolldieText = tk.Label(self.gameBoardWindow, text = 'Dice Roll:', font = self.arial_bold)
        self.rolldieText.grid(column = 1, row = 3)
        self.roll = StringVar()
        self.rolldieResult = tk.Label(self.gameBoardWindow, text = self.roll, font = self.arial)
        self.rolldieResult.grid(column = 2, row = 3, columnspan = 3)
        self.rollButton = tk.Button(self.gameBoardWindow, text = 'Roll Die', command = self.startTurn, font = self.arial_bold)
        self.rollButton.grid(column = 2, row = 4, sticky = 'EW')

        # player question
        self.playerLabel = tk.Label(self.gameBoardWindow, text = 'Question:', font = self.arial_bold)
        self.playerLabel.grid(column = 1, row = 5, columnspan = 4)
        self.question = 'No Question Available'
        self.questionText = Label(self.gameBoardWindow, text = '', wraplength = 400, font = self.arial)
        self.questionText.grid(column = 1, row = 6, columnspan = 4)
        # player answer
        self.answerLabel = tk.Label(self.gameBoardWindow, text = 'Answer:', font = self.arial_bold)
        self.answerLabel.grid(column = 1, row = 7, columnspan = 4)
        self.answerEntry = Entry(self.gameBoardWindow)
        self.answerEntry.grid(column = 1, row = 8, columnspan = 4)

        # submit answer
        self.submitAnswer = tk.Button(self.gameBoardWindow, command = self.checkAnswer, text = 'Submit Answer', font = self.arial_bold)
        self.submitAnswer.grid(row = 9, column = 1, columnspan = 4)

        # add button to access dice roll
        self.rulesButton = tk.Button(self.gameBoardWindow, command = self.viewRules, text = 'View Game Rules', font = self.arial_bold)
        self.rulesButton.grid(row = 15, column = 2)

        # add button to access dice roll
        self.gameExitButton = tk.Button(self.gameBoardWindow, command = self.close, text = 'Exit Game Board', font = self.arial_bold)
        self.gameExitButton.grid(row = 16, column = 2)

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
                self.canvas.create_text(x1+30, y1+30, text = self.grid_conv_table[i])
                self.canvas.create_rectangle(x1, y1, x2, y2, outline = 'black', fill = self.colors[i], tags = 'square')
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

        print('Moving player: ', name)

        # place piece at row/column
        self.pieces[name] = (self.grid_loc[location][0], self.grid_loc[location][1])

        if self.player_num[name] == 1:
            # print('Place in quadrant 1 of square')
            self.canvas.coords(name, self.grid_loc[location][0] + 20, self.grid_loc[location][1] + 20)
        elif self.player_num[name] == 2:
            # print('Place in quadrant 2 of square')
            self.canvas.coords(name, self.grid_loc[location][0] + 50, self.grid_loc[location][1] + 20)
        elif self.player_num[name] == 3:
            # print('Place in quadrant 3 of square')
            self.canvas.coords(name, self.grid_loc[location][0] + 20, self.grid_loc[location][1] + 50)
        elif self.player_num[name] == 4:
            # print('Place in quadrant 4 of square')
            self.canvas.coords(name, self.grid_loc[location][0] + 50, self.grid_loc[location][1] + 50)

    def addPiece(self, name, image):
        # add player piece to board
        print('Adding Player {} to Board'.format(name))
        self.canvas.create_image(20, 20, image = image, tags = (name, 'piece'), anchor = 'c')
        # self.placePiece(name, row, column)
        self.placePiece(name, 21)

    def submitCategory(self, category):

        print('Category Chosen: ', category)
        self.category = category
        press('enter')
        
    def checkAnswer(self):
        print('Check answer')

    def setDirection(self, direction):
        
        self.move_direction = direction
        print(self.move_direction)
        # Move the Player off the decision tile 
        currentPlayer = self.players[self.currentPlayerIdx]
        currentPlayer.location = self.board[currentPlayer.location].nextSquare[direction]
        self.distance -= 1
        self.movePlayer(self.distance, direction, currentPlayer)

        
    def func(self):
        print("You've hit return!")

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
        self.current_player.configure(text = currentPlayer.id)
        # print('Player ' + str(currentPlayer.id) + "'s turn")
        # Roll the Dice
        self.distance = DiceRoll.rollDice()
        self.rolldieResult.configure(text = str(self.distance))      
        # Set the direction Buttons up for The beginning of the move
        self.setValidDirections(currentPlayer.location)
        return

    #def askQuestion():
        # Question Answering and Chip Logic
        questionGenerator = tp_question.QuestionGenerator()
        question = {}
        category = ''
        if currentPlayer.location == 33:
            # If chips < 4, choose the category, 4 or more, opponent chooses
            if (len(currentPlayer.chips) < 4):
                category = input('Choose a Category: Events, Places, Independence Day, People: ')
            else:
                category = input('(Opponent) Choose final question Category:  Events, Places, Independence Day, People: ')
        else:
            category = self.board[currentPlayer.location].category
        if category == 'Roll':
            # Need to Update the UI and display roll again message here
            print('ROLL AGAIN')
            return
        else:
            question = questionGenerator.getRandomQuestion(category)

        # Display Question and Prompt for Answer
        # needs to be replaced by with UI loop integration
        self.questionText.configure(text = question['question'])
        print(question['question'])
    #def onSubmitAnswer():
        ans = input('Input Answer:')
        correct = (ans == question['answer'])

        #  Below is so one can mash enter to test, uncomment for testing:
        # correct = True
        if (correct): 
            print('Correct')
            # Check if this was the player's final question
            if (currentPlayer.location == 33 and len(currentPlayer.chips) == 4):
            # Below for testing, removes the last square condition to speed to victory logic
            #if (len(currentPlayer.chips) == 4):
                # Add player to the placement array, remove them from the players array, immediately end the turn
                self.placement.append(self.players.pop(self.currentPlayerIdx))
                self.current_player.configure(text = '')
                if self.player_num[currentPlayer.id] == 1:
                    # remove player 1 from UI
                    self.player1_name.destroy()
                    self.player1Num.destroy()
                    self.player1_chips_label.destroy()
                    self.chip1_img.destroy()
                    self.canvas.delete(currentPlayer.id)
                elif self.player_num[currentPlayer.id] == 2:
                    # remove player 2 from UI
                    self.player2_name.destroy()
                    self.player2Num.destroy()
                    self.player2_chips_label.destroy()
                    self.chip2_img.destroy()
                    self.canvas.delete(currentPlayer.id)
                elif self.player_num[currentPlayer.id] == 3:
                    # remove player 3 from UI
                    self.player3_name.destroy()
                    self.player3Num.destroy()
                    self.player3_chips_label.destroy()
                    self.chip3_img.destroy()
                    self.canvas.delete(currentPlayer.id)
                elif self.player_num[currentPlayer.id] == 4:
                    # remove player 4 from UI
                    self.player4_name.destroy()
                    self.player4Num.destroy()
                    self.player4_chips_label.destroy()
                    self.chip4_img.destroy()
                    self.canvas.delete(currentPlayer.id)
            #Otherwise add chip
            else:
                currentPlayer.addChip(category)
        else:
            print('Incorrect')
            # Move the player off the center square if this was a final attempt
            if (currentPlayer.location == 33 and len(currentPlayer.chips) == 4):
                self.movePlayer(1, currentPlayer)
            # Move to the next player before starting the next turn if we got the wrong answer
            if (self.currentPlayerIdx >= len(self.players) - 1):
                    self.currentPlayerIdx = 0
            else:
                self.currentPlayerIdx += 1
        #Update the UI State
        if self.player_num[currentPlayer.id] == 1:
            # update player 1 in UI
            # print('Update player 1: {} chip image'.format(self.player_num[currentPlayer.id]))
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
            # print('Update player 2: {} chip image'.format(self.player_num[currentPlayer.id]))
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
            # print('Update player 3: {} chip image'.format(self.player_num[currentPlayer.id]))
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
            # print('Update player 4: {} chip image'.format(self.player_num[currentPlayer.id]))
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
        self.actionLabel.configure(text = 'Next Player Rolls')
        # time.sleep(1)

    def setValidDirections(self, currlocation, exiting=False):
        # Return the valid directions given a location
        # Disable invalid buttons in the UI
        if currlocation < 25:
            if currlocation in [4,10,16,22]:
                self.actionLabel.configure(text = 'Choose Direction (cw, ccw, inner)')
                return ['cw','ccw','inner']
            else:
                self.actionLabel.configure(text = 'Choose Direction (cw, ccw)')
                return ['cw','ccw']
        elif currlocation < 33:
            self.actionLabel.configure(text = 'Choose Direction (inner, outer)')
            return ['inner','outer']
        else:
            self.actionLabel.configure(text = 'Choose Exit Direction (up, down, left, right)')
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
        # self.placePiece(player.id, player.location)

    def questionWindow(self, name, question):

        self.questionWindow = tk.Tk()
        self.questionWindow.title('TP Question')
        self.frame = tk.Frame(self.questionWindow)

        # options for player to choose direction
        self.playerLabel = Label(self.questionWindow, text = 'Current Player:', font = self.arial_bold)
        self.playerLabel.grid(row = 0, column = 0)
        self.playerName = Label(self.questionWindow, text = name, font = self.arial)
        self.playerName.grid(row = 1, column = 0)
        self.questionLabel = Label(self.questionWindow, text = 'Question', font = self.arial_bold)
        self.questionLabel.grid(row = 2, column = 0)
        self.question = Label(self.questionWindow, text = question, wraplength = 400, font = self.arial)
        self.question.grid(row = 3, column = 0)
        self.answerLabel = Label(self.questionWindow, text = 'Enter Answer:', font = self.arial_bold)
        self.answerLabel.grid(row = 4, column = 0)
        self.answerEntry = Entry(self.questionWindow)
        self.answerEntry.grid(row = 5, column = 0, columnspan = 8)
        self.submitAnswer = tk.Button(self.questionWindow, text = 'Submit Answer', command = lambda: self.submit(self.answerEntry.get()), font = self.arial)
        self.submitAnswer.grid(row = 6, column = 0, columnspan = 2)

    def submit(self, answer):

        print('Submit answer and close question window')
        print('Answer created from window:', answer)
        self.answer = answer
        self.questionWindow.destroy()

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
            
    def showVictoryScreen(self):
        # Text based State UI for now, add real screen later
        print('Game Over')
        print('Rankings')
        i = 1
        for player in self.placement:
            print('No ' + str(i) +': Player ' + str(player.id))
            i += 1

    def viewRules(self):
        rules_window = tp_rules_UI.RulesUI()

    def close(self):
        print('Close Game Board')
        self.gameBoardWindow.destroy()
        for player in self.players:
            del player
