from PIL import ImageTk, Image
from tkinter import Label, Entry, StringVar, font
import json
import os
import tkinter as tk
import tp_gamesettings_UI as pg
import tp_player as pl
import tp_rules_UI
import tp_game

class GameUI:

    def __init__(self, settings):

        print('INITIALIZE GAME UI')
        self.settings = settings
        self.players = []

        for name in list(self.settings['players'].values()):
            newPlayer = pl.Player(name)
            self.players.append(newPlayer)

        # set font type and size in root window
        arial = font.Font(family = 'Arial', size = 14)
        arial_bold = font.Font(family = 'Arial', size = 14, weight = 'bold')

        self.gameBoardWindow = tk.Toplevel()
        self.gameBoardWindow.title('Trivial Purfruit')
        self.frame = tk.Frame(self.gameBoardWindow)

        # get player names
        if len(self.players) == 1:
            # add image for main screen
            self.tp_img = Image.open('./res/tp_temp_gameboard_1.png')
            self.tp_photo = ImageTk.PhotoImage(self.tp_img)
            self.tp_holder_img = Label(self.gameBoardWindow, image = self.tp_photo)
            self.tp_holder_img.grid(row = 0, columnspan = 4)

            self.column = 0
            # add label for player one name
            self.player1_name = Label(self.gameBoardWindow, text = 'Player: ' + self.players[0].id, font = arial)
            self.player1_name.grid(row = 1, column = 0)
            # add label for player one chips
            self.player1_chips_label = Label(self.gameBoardWindow, text = 'Chips:', font = arial)
            self.player1_chips_label.grid(row = 2, column = 0)
            self.player1_chips = Label(self.gameBoardWindow, text = self.players[0].chips, font = arial)
            self.player1_chips.grid(row = 3, column = 0)
            # add button to roll dice
            self.player1_rolldice = tk.Button(self.gameBoardWindow, text = 'P1 Roll Dice', font = arial_bold)
            self.player1_rolldice.grid(row = 4, column = 0, pady = 10)
            # dice roll result
            self.player1_dice_result = Label(self.gameBoardWindow, text = '0', font = arial)
            self.player1_dice_result.grid(row = 5, column = 0)

        elif len(self.players) == 2:

            # add image for main screen
            self.tp_img = Image.open('./res/tp_temp_gameboard_2.png')
            self.tp_photo = ImageTk.PhotoImage(self.tp_img)
            self.tp_holder_img = Label(self.gameBoardWindow, image = self.tp_photo)
            self.tp_holder_img.grid(row = 0, columnspan = 4)
            
            self.column_num = 0
            # add label for player one name
            self.player1_name = Label(self.gameBoardWindow, text = 'Player: ' + self.players[0].id, font = arial)
            self.player1_name.grid(row = 1, column = 0)
            # add label for player one chips
            self.player1_chips_label = Label(self.gameBoardWindow, text = 'Chips:', font = arial)
            self.player1_chips_label.grid(row = 2, column = 0)
            self.player1_chips = Label(self.gameBoardWindow, text = self.players[0].chips, font = arial)
            self.player1_chips.grid(row = 3, column = 0)
            # add button to roll dice
            self.player1_rolldice = tk.Button(self.gameBoardWindow, text = 'P1 Roll Dice', font = arial_bold)
            self.player1_rolldice.grid(row = 4, column = 0, pady = 10)
            # dice roll result
            self.player1_dice_result = Label(self.gameBoardWindow, text = '0', font = arial)
            self.player1_dice_result.grid(row = 5, column = 0)

            # create player two object
            self.p2 = pl.Player(self.settings['players']['player2'])
            # add label for player one name
            self.player2_name = Label(self.gameBoardWindow, text = 'Player: ' + self.players[0].id, font = arial)
            self.player2_name.grid(row = 1, column = 1)
            # add label for player one chips
            self.player2_chips_label = Label(self.gameBoardWindow, text = 'Chips:', font = arial)
            self.player2_chips_label.grid(row = 2, column = 1)
            self.player2_chips = Label(self.gameBoardWindow, text = self.players[0].chips, font = arial)
            self.player2_chips.grid(row = 3, column = 1)
            # add button to roll dice
            self.player2_rolldice = tk.Button(self.gameBoardWindow, text = 'P2 Roll Dice', font = arial_bold)
            self.player2_rolldice.grid(row = 4, column = 1, pady = 10)
            # dice roll result
            self.player2_dice_result = Label(self.gameBoardWindow, text = '0', font = arial)
            self.player2_dice_result.grid(row = 5, column = 1)

        elif len(self.players) == 3:
            
            # add image for main screen
            self.tp_img = Image.open('./res/tp_temp_gameboard_3.png')
            self.tp_photo = ImageTk.PhotoImage(self.tp_img)
            self.tp_holder_img = Label(self.gameBoardWindow, image = self.tp_photo)
            self.tp_holder_img.grid(row = 0, columnspan = 4)
            
            self.column_num = 1
            # add label for player one name
            self.player1_name = Label(self.gameBoardWindow, text = 'Player: ' + self.players[0].id, font = arial)
            self.player1_name.grid(row = 1, column = 0)
            # add label for player one chips
            self.player1_chips_label = Label(self.gameBoardWindow, text = 'Chips:', font = arial)
            self.player1_chips_label.grid(row = 2, column = 0)
            self.player1_chips = Label(self.gameBoardWindow, text = self.players[0].chips, font = arial)
            self.player1_chips.grid(row = 3, column = 0)
            # add button to roll dice
            self.player1_rolldice = tk.Button(self.gameBoardWindow, text = 'P1 Roll Dice', font = arial_bold)
            self.player1_rolldice.grid(row = 4, column = 0, pady = 10)
            # dice roll result
            self.player1_dice_result = Label(self.gameBoardWindow, text = '0', font = arial)
            self.player1_dice_result.grid(row = 5, column = 0)

            # add label for player one name
            self.player2_name = Label(self.gameBoardWindow, text = 'Player: ' + self.players[1].id, font = arial)
            self.player2_name.grid(row = 1, column = 1)
            # add label for player one chips
            self.player2_chips_label = Label(self.gameBoardWindow, text = 'Chips:', font = arial)
            self.player2_chips_label.grid(row = 2, column = 1)
            self.player2_chips = Label(self.gameBoardWindow, text = self.players[1].chips, font = arial)
            self.player2_chips.grid(row = 3, column = 1)
            # add button to roll dice
            self.player2_rolldice = tk.Button(self.gameBoardWindow, text = 'P2 Roll Dice', font = arial_bold)
            self.player2_rolldice.grid(row = 4, column = 1, pady = 10)
            # dice roll result
            self.player2_dice_result = Label(self.gameBoardWindow, text = '0', font = arial)
            self.player2_dice_result.grid(row = 5, column = 1)

            # add label for player one name
            self.player3_name = Label(self.gameBoardWindow, text = 'Player: ' + self.players[2].id, font = arial)
            self.player3_name.grid(row = 1, column = 2)
            # add label for player one chips
            self.player3_chips_label = Label(self.gameBoardWindow, text = 'Chips:', font = arial)
            self.player3_chips_label.grid(row = 2, column = 2)
            self.player3_chips = Label(self.gameBoardWindow, text = self.players[2].chips, font = arial)
            self.player3_chips.grid(row = 3, column = 2)
            # add button to roll dice
            self.player3_rolldice = tk.Button(self.gameBoardWindow, text = 'P3 Roll Dice', font = arial_bold)
            self.player3_rolldice.grid(row = 4, column = 2, pady = 10)
            # dice roll result
            self.player3_dice_result = Label(self.gameBoardWindow, text = '0', font = arial)
            self.player3_dice_result.grid(row = 5, column = 2)

        elif len(self.players) == 4:
            
            # add image for main screen
            self.tp_img = Image.open('./res/tp_temp_gameboard_4.png')
            self.tp_photo = ImageTk.PhotoImage(self.tp_img)
            self.tp_holder_img = Label(self.gameBoardWindow, image = self.tp_photo)
            self.tp_holder_img.grid(row = 0, columnspan = 4)
            
            self.column_num = 1
            # add label for player one name
            self.player1_name = Label(self.gameBoardWindow, text = 'Player: ' + self.players[0].id, font = arial)
            self.player1_name.grid(row = 1, column = 0)
            # add label for player one chips
            self.player1_chips_label = Label(self.gameBoardWindow, text = 'Chips:', font = arial)
            self.player1_chips_label.grid(row = 2, column = 0)
            self.player1_chips = Label(self.gameBoardWindow, text = self.players[0].chips, font = arial)
            self.player1_chips.grid(row = 3, column = 0)
            # add button to roll dice
            self.player1_rolldice = tk.Button(self.gameBoardWindow, text = 'P1 Roll Dice', font = arial_bold)
            self.player1_rolldice.grid(row = 4, column = 0, pady = 10)
            # dice roll result
            self.player1_dice_result = Label(self.gameBoardWindow, text = '0', font = arial)
            self.player1_dice_result.grid(row = 5, column = 0)

            # add label for player one name
            self.player2_name = Label(self.gameBoardWindow, text = 'Player: ' + self.players[1].id, font = arial)
            self.player2_name.grid(row = 1, column = 1)
            # add label for player one chips
            self.player2_chips_label = Label(self.gameBoardWindow, text = 'Chips:', font = arial)
            self.player2_chips_label.grid(row = 2, column = 1)
            self.player2_chips = Label(self.gameBoardWindow, text = self.players[1].chips, font = arial)
            self.player2_chips.grid(row = 3, column = 1)
            # add button to roll dice
            self.player2_rolldice = tk.Button(self.gameBoardWindow, text = 'P2 Roll Dice', font = arial_bold)
            self.player2_rolldice.grid(row = 4, column = 1, pady = 10)
            # dice roll result
            self.player2_dice_result = Label(self.gameBoardWindow, text = '0', font = arial)
            self.player2_dice_result.grid(row = 5, column = 1)

            # add label for player three name
            self.player3_name = Label(self.gameBoardWindow, text = 'Player: ' + self.players[2].id, font = arial)
            self.player3_name.grid(row = 1, column = 2)
            # add label for player three chips
            self.player3_chips_label = Label(self.gameBoardWindow, text = 'Chips:', font = arial)
            self.player3_chips_label.grid(row = 2, column = 2)
            self.player3_chips = Label(self.gameBoardWindow, text = self.players[2].chips, font = arial)
            self.player3_chips.grid(row = 3, column = 2)
            # add button to roll dice
            self.player3_rolldice = tk.Button(self.gameBoardWindow, text = 'P3 Roll Dice', font = arial_bold)
            self.player3_rolldice.grid(row = 4, column = 2, pady = 10)
            # dice roll result
            self.player3_dice_result = Label(self.gameBoardWindow, text = '0', font = arial)
            self.player3_dice_result.grid(row = 5, column = 2)

            # add label for player one name
            self.player4_name = Label(self.gameBoardWindow, text = 'Player: ' + self.players[3].id, font = arial)
            self.player4_name.grid(row = 1, column = 3)
            # add label for player one chips
            self.player4_chips_label = Label(self.gameBoardWindow, text = 'Chips:', font = arial)
            self.player4_chips_label.grid(row = 2, column = 3)
            self.player4_chips = Label(self.gameBoardWindow, text = self.players[3].chips, font = arial)
            self.player4_chips.grid(row = 3, column = 3)
            # add button to roll dice
            self.player4_rolldice = tk.Button(self.gameBoardWindow, text = 'P4 Roll Dice', font = arial_bold)
            self.player4_rolldice.grid(row = 4, column = 3, pady = 10)
            # dice roll result
            self.player4_dice_result = Label(self.gameBoardWindow, text = '0', font = arial)
            self.player4_dice_result.grid(row = 5, column = 3)

        # player question/answer area
        self.player_in_turn = tk.Label(self.gameBoardWindow, text = 'Current Player:', font = arial_bold)
        self.player_in_turn.grid(row = 6, column = 0)

        # player question
        self.playerLabel = tk.Label(self.gameBoardWindow, text = 'Question:', font = arial_bold)
        self.playerLabel.grid(row = 7, column = 0)
        self.question = 'What protest took place to oppose the taxes imposed on American colonists?'
        self.questionText = Label(self.gameBoardWindow, text = self.question, font = arial)
        self.questionText.grid(row = 8, column = 0, columnspan = 4)
        # player answer
        self.answerLabel = tk.Label(self.gameBoardWindow, text = 'Answer:', font = arial_bold)
        self.answerLabel.grid(row = 9, column = 0)
        self.answerEntry = Entry(self.gameBoardWindow, bd = 5)
        self.answerEntry.grid(row = 9, column = 0, columnspan = 4, pady = 10)

        # submit answer
        self.submitAnswer = tk.Button(self.gameBoardWindow, command = self.checkAnswer, text = 'Submit Answer', font = arial_bold)
        self.submitAnswer.grid(row = 10)

        # game simulation
        self.gameSimulation = tk.Button(self.gameBoardWindow, command = self.beginGameSimulation, text = 'Game Simulation', font = arial_bold)
        self.gameSimulation.grid(row = 11)

        # add button to access dice roll
        self.rulesButton = tk.Button(self.gameBoardWindow, command = self.viewRules, text = 'View Game Rules', font = arial_bold)
        self.rulesButton.grid(column = 0)

        # add button to access dice roll
        self.gameExitButton = tk.Button(self.gameBoardWindow, command = self.close, text = 'Exit Game Board', font = arial_bold)
        self.gameExitButton.grid(column = 0)

    def rolldice(self):
        print('Roll Dice')

    def beginGameSimulation(self):
        print('Begin Game Simulation...')
        game = tp_game.Game()
        game.run()
        
    def checkAnswer(self):
        print('Check answer')

    def viewRules(self):
        rules_window = tp_rules_UI.RulesUI()

    def close(self):
        print('Close Game Board')
        self.gameBoardWindow.destroy()
