from PIL import ImageTk, Image
from tkinter import Label, Entry, StringVar, font
from tp_diceroll import DiceRoll
import json
import os
import time
import tkinter as tk
import tp_gameUI_new
import tp_rules_UI
import tp_settings
import random

class GameSettings:

    players = {
                'player1': 'player1'
    }
    names = []
    settings = tp_settings.Settings()
    num_of_players = int(settings.settings['players'])

    def __init__(self):

        print('Open window to initialize settings for new game...')
        # set font type and size in root window
        arial = font.Font(family = 'Arial', size = 14)
        arial_bold = font.Font(family = 'Arial', size = 14, weight = 'bold')

        self.gameSettingsWindow = tk.Toplevel()
        self.gameSettingsWindow.title('TP Game Settings')
        self.frame = tk.Frame(self.gameSettingsWindow)

        self.instructions = 'Enter Settings for New Game:\n1) Enter names of players \nNote: Only enter names \nof players to play\n2) Select time for question answering\n3) Click Set Player Order button \nto determine player order \n4) Click Begin New Game\nto start new game'
        # trivial pursuit welcome label
        self.settingsLabel = Label(self.gameSettingsWindow, text = self.instructions, font = arial_bold)
        self.settingsLabel.grid(sticky = 'EW', row = 0, column = 0)

        # enter player names
        self.playerNamesLabel = Label(self.gameSettingsWindow, text = 'Enter Player Names:', font = arial_bold)
        self.playerNamesLabel.grid(row = 1, columnspan = 3)
        # entry for player one
        self.playeroneLabel = Label(self.gameSettingsWindow, text = 'Player 1:', font = arial_bold)
        self.playeroneLabel.grid(row = 2, column = 0)
        self.p1_entry = Entry(self.gameSettingsWindow)
        self.p1_entry.grid(row = 2, column = 1, columnspan = 3)
        # entry for player two
        self.playertwoLabel = Label(self.gameSettingsWindow, text = 'Player 2:', font = arial_bold)
        self.playertwoLabel.grid(row = 3, column = 0)
        self.p2_entry = Entry(self.gameSettingsWindow)
        self.p2_entry.grid(row = 3, column = 1, columnspan = 3)
        # entry for player three
        self.playerthreeLabel = Label(self.gameSettingsWindow, text = 'Player 3:', font = arial_bold)
        self.playerthreeLabel.grid(row = 4, column = 0)
        self.p3_entry = Entry(self.gameSettingsWindow)
        self.p3_entry.grid(row = 4, column = 1, columnspan = 3)
        # entry for player four
        self.playerfourLabel = Label(self.gameSettingsWindow, text = 'Player 4:', font = arial_bold)
        self.playerfourLabel.grid(row = 5, column = 0)
        self.p4_entry = Entry(self.gameSettingsWindow)
        self.p4_entry.grid(row = 5, column = 1, columnspan = 3)

        # select answer time limit
        self.timeLimit = Label(self.gameSettingsWindow, text = 'Select Timer for \nAnswers (in seconds):', font = arial_bold)
        self.timeLimit.grid(row = 6, column = 0)
        # 5 second time limit
        self.fiveSec = tk.Button(self.gameSettingsWindow, text = '5', command = lambda: self.time_limit(5), font = arial, height = 2, width = 6)
        self.fiveSec.grid(row = 6, column = 1)
        # 10 second time limit
        self.tenSec = tk.Button(self.gameSettingsWindow, text = '10', command = lambda: self.time_limit(10), font = arial, height = 2, width = 6)
        self.tenSec.grid(row = 6, column = 2)
        # 15 second time limit
        self.fifteenSec = tk.Button(self.gameSettingsWindow, text = '15', command = lambda: self.time_limit(15), font = arial, height = 2, width = 6)
        self.fifteenSec.grid(row = 6, column = 3)

        # dice rolls for player order
        self.dicerollLabel = Label(self.gameSettingsWindow, text = 'Player Order Results:', font = arial_bold)
        self.dicerollLabel.grid(row = 1, column = 4)
        # die results for player order
        self.p1rollLabel = Label(self.gameSettingsWindow, text = '', font = arial)
        self.p1rollLabel.grid(row = 2, column = 4)
        # die results for player order
        self.p2rollLabel = Label(self.gameSettingsWindow, text = '', font = arial)
        self.p2rollLabel.grid(row = 3, column = 4)
        # die results for player order
        self.p3rollLabel = Label(self.gameSettingsWindow, text = '', font = arial)
        self.p3rollLabel.grid(row = 4, column = 4)
        # die results for player order
        self.p4rollLabel = Label(self.gameSettingsWindow, text = '', font = arial)
        self.p4rollLabel.grid(row = 5, column = 4)

        # add button to exit program
        self.exitGameSettings = tk.Button(self.gameSettingsWindow, text = 'Set Player Order', command = self.rollDie, font = arial_bold)
        self.exitGameSettings.grid(row = 6, column = 4)

        # add button to exit program
        self.exitGameSettings = tk.Button(self.gameSettingsWindow, text = 'Begin New Game', command = self.beginNewGame, font = arial_bold)
        self.exitGameSettings.grid(sticky = 'EW')

        # add button to view game rules
        self.exitGameSettings = tk.Button(self.gameSettingsWindow, text = 'View Game Rules', command = self.viewRulesUI, font = arial_bold)
        self.exitGameSettings.grid(sticky = 'EW')

        # add button to exit program
        self.exitGameSettings = tk.Button(self.gameSettingsWindow, text = 'Return to Main Menu', command = self.mainMenu, font = arial_bold)
        self.exitGameSettings.grid(sticky = 'EW')

    def time_limit(self, ques_time):
        print('Setting question time limit to: {}'.format(ques_time))
        self.time_limit = ques_time

    def viewRulesUI(self):
        rules_window = tp_rules_UI.RulesUI()

    def mainMenu(self):
        print('Close new game settings and return to Main Menu')
        self.gameSettingsWindow.destroy()

    def rollDie(self):

        get_names = []
        if len(self.p1_entry.get()) != 0:
            get_names.append(self.p1_entry.get())
        if len(self.p2_entry.get()) != 0:
            get_names.append(self.p2_entry.get())
        if len(self.p3_entry.get()) != 0:
            get_names.append(self.p3_entry.get())
        if len(self.p4_entry.get()) != 0:
            get_names.append(self.p4_entry.get())
        print(get_names)

        if len(get_names) == 2:
            self.rollResults = random.sample(range(1, 3), 2)
            print('Order Results: ', self.rollResults)
            self.p1rollLabel.configure(text = self.rollResults[0])
            self.p2rollLabel.configure(text = self.rollResults[1])
        elif len(get_names) == 3:
            self.rollResults = random.sample(range(1, 4), 3)
            print('Order Results: ', self.rollResults)
            self.p1rollLabel.configure(text = self.rollResults[0])
            self.p2rollLabel.configure(text = self.rollResults[1])
            self.p3rollLabel.configure(text = self.rollResults[2])
        elif len(get_names) == 4:
            self.rollResults = random.sample(range(1, 5), 4)
            print('Order Results: ', self.rollResults)
            self.p1rollLabel.configure(text = self.rollResults[0])
            self.p2rollLabel.configure(text = self.rollResults[1])
            self.p3rollLabel.configure(text = self.rollResults[2])
            self.p4rollLabel.configure(text = self.rollResults[3])

    def beginNewGame(self):

        self.player_order = []

        print('Begin New Game Now')
        if len(self.p1_entry.get()) != 0:
            self.names.append(self.p1_entry.get())
        if len(self.p2_entry.get()) != 0:
            self.names.append(self.p2_entry.get())
        if len(self.p3_entry.get()) != 0:
            self.names.append(self.p3_entry.get())
        if len(self.p4_entry.get()) != 0:
            self.names.append(self.p4_entry.get())

        # order players based on roll results
        for name, num in zip(self.names, self.rollResults):
            self.player_order.append((name, num))
        print('Player Order: ', self.player_order)

        # reorder names based on roll die results in game settings
        self.player_order.sort(key=lambda x:x[1])
        # self.player_order = self.player_order[::-1]
        self.names = [x[0] for x in self.player_order]
        print('Names: ', self.names)

        if len(self.names) == 0:
            print('No players entered')
        if len(self.names) == 1:
            players = {
                        'player1': self.names[0]
            }
        elif len(self.names) == 2:
            players = {
                        'player1': self.names[0],
                        'player2': self.names[1]
            }
        elif len(self.names) == 3:
            players = {
                        'player1': self.names[0],
                        'player2': self.names[1],
                        'player3': self.names[2]
            }
        elif len(self.names) == 4:
            players = {
                        'player1': self.names[0],
                        'player2': self.names[1],
                        'player3': self.names[2],
                        'player4': self.names[3]
            }

        self.settings = {
                        'time_limit': self.time_limit,
                        'players': players
                        }

        print('Close new game settings and proceed to new game')
        self.gameSettingsWindow.destroy()
        game_window = tp_gameUI_new.GameUI(self.settings)
