from PIL import ImageTk, Image
from tkinter import Label, Entry, StringVar, font
import json
import os
import tkinter as tk
import tp_gameUI
import tp_rules_UI
import tp_settings

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

        # trivial pursuit welcome label
        self.settingsLabel = Label(self.gameSettingsWindow, text = 'Enter Settings for New Game', font = arial_bold)
        self.settingsLabel.grid(sticky = 'EW', row = 0)

        # enter player names
        self.playerNamesLabel = Label(self.gameSettingsWindow, text = 'Enter Player Names:', font = arial_bold)
        self.playerNamesLabel.grid(row = 2)
        # entry for player one
        self.playeroneLabel = Label(self.gameSettingsWindow, text = 'Player 1:', font = arial_bold)
        self.playeroneLabel.grid(row = 3, column = 0)
        self.p1_entry = Entry(self.gameSettingsWindow, bd = 5)
        self.p1_entry.grid(row = 3, column = 1, columnspan = 5)
        # entry for player two
        self.playertwoLabel = Label(self.gameSettingsWindow, text = 'Player 2:', font = arial_bold)
        self.playertwoLabel.grid(row = 5, column = 0)
        self.p2_entry = Entry(self.gameSettingsWindow, bd = 5)
        self.p2_entry.grid(row = 5, column = 1, columnspan = 5)
        # entry for player three
        self.playerthreeLabel = Label(self.gameSettingsWindow, text = 'Player 3:', font = arial_bold)
        self.playerthreeLabel.grid(row = 7, column = 0)
        self.p3_entry = Entry(self.gameSettingsWindow, bd = 5)
        self.p3_entry.grid(row = 7, column = 1, columnspan = 5)
        # entry for player four
        self.playerfourLabel = Label(self.gameSettingsWindow, text = 'Player 4:', font = arial_bold)
        self.playerfourLabel.grid(row = 9, column = 0)
        self.p4_entry = Entry(self.gameSettingsWindow, bd = 5)
        self.p4_entry.grid(row = 9, column = 1, columnspan = 5)

        # select answer time limit
        self.timeLimit = Label(self.gameSettingsWindow, text = 'Select Timer for Answers (in seconds):', font = arial_bold)
        self.timeLimit.grid(row = 13, column = 0)
        # 5 second time limit
        self.fiveSec = tk.Button(self.gameSettingsWindow, text = '5', command = lambda: self.time_limit(5), font = arial, height = 2, width = 6)
        self.fiveSec.grid(row = 13, column = 1)
        # 10 second time limit
        self.tenSec = tk.Button(self.gameSettingsWindow, text = '10', command = lambda: self.time_limit(10), font = arial, height = 2, width = 6)
        self.tenSec.grid(row = 13, column = 2)
        # 15 second time limit
        self.fifteenSec = tk.Button(self.gameSettingsWindow, text = '15', command = lambda: self.time_limit(15), font = arial, height = 2, width = 6)
        self.fifteenSec.grid(row = 13, column = 3)

        # select game difficulty
        self.gameDifficulty = Label(self.gameSettingsWindow, text = 'Select Game Difficulty:', font = arial_bold)
        self.gameDifficulty.grid(row = 14, column = 0)
        # 5 second time limit
        self.easyDifficulty = tk.Button(self.gameSettingsWindow, text = 'Easy', command = lambda: self.difficulty_level('easy'), font = arial, height = 2, width = 6)
        self.easyDifficulty.grid(row = 14, column = 1)
        # 10 second time limit
        self.normDifficulty = tk.Button(self.gameSettingsWindow, text = 'Normal', command = lambda: self.difficulty_level('normal'), font = arial, height = 2, width = 6)
        self.normDifficulty.grid(row = 14, column = 2)
        # 15 second time limit
        self.hardDifficulty = tk.Button(self.gameSettingsWindow, text = 'Hard', command = lambda: self.difficulty_level('hard'), font = arial, height = 2, width = 6)
        self.hardDifficulty.grid(row = 14, column = 3)

        # add button to view game rules
        self.exitGameSettings = tk.Button(self.gameSettingsWindow, text = 'View Game Rules', command = self.viewRulesUI, font = arial_bold, height = 2, width = 6)
        self.exitGameSettings.grid(stick = 'EW')

        # add button to exit program
        self.exitGameSettings = tk.Button(self.gameSettingsWindow, text = 'Begin New Game', command = self.beginNewGame, font = arial_bold, height = 2, width = 6)
        self.exitGameSettings.grid(stick = 'EW')

    def difficulty_level(self, diff):
        print('Setting difficulty level to: {}'.format(diff))
        self.difficulty = diff

    def time_limit(self, ques_time):
        print('Setting question time limit to: {}'.format(ques_time))
        self.time_limit = ques_time

    def viewRulesUI(self):
        rules_window = tp_rules_UI.RulesUI()

    def beginNewGame(self):

        if len(self.p1_entry.get()) != 0:
            self.names.append(self.p1_entry.get())
        if len(self.p2_entry.get()) != 0:
            self.names.append(self.p2_entry.get())
        if len(self.p3_entry.get()) != 0:
            self.names.append(self.p3_entry.get())
        if len(self.p4_entry.get()) != 0:
            self.names.append(self.p4_entry.get())

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
                        'difficulty': self.difficulty,
                        'players': players
                        }

#         for key, value in self.settings['players'].items():
#             print('{}: {}'.format(key, value))

        print('Close new game settings and proceed to new game')
        self.gameSettingsWindow.destroy()
        game_window = tp_gameUI.GameUI(self.settings)
