from PIL import ImageTk, Image
from tkinter import Label, Entry, StringVar, font
import tkinter as tk
import tp_gameboard
import os

class createNewGameSettings:

	def __init__(self):

		# set font type and size in root window
		arial10 = font.Font(family = 'Arial', size = 14)
		arial10_bold = font.Font(family = 'Arial', size = 14, weight = 'bold')

		self.gameSettingsWindow = tk.Toplevel()
		self.gameSettingsWindow.geometry('500x700')
		self.frame = tk.Frame(self.gameSettingsWindow)

		# self.quitButton = tk.Button(self.frame, text = 'Quit')
		# self.quitButton.pack()

		# trivial pursuit welcome label
		self.settingsLabel = Label(self.gameSettingsWindow, text = 'Enter Settings for New Game', font = arial10_bold)
		self.settingsLabel.grid(sticky = 'EW', row = 0)

		# select number of players
		self.noPlayersLabel = Label(self.gameSettingsWindow, text = 'Select Number of Players:', font = arial10_bold)
		self.noPlayersLabel.grid(row = 1, column = 0)
		# single player for game
		self.one_player = tk.Button(self.gameSettingsWindow, text = '1', command = lambda: self.no_of_players(1), font = arial10)
		self.one_player.grid(row = 1, column = 1)
		# two players for game
		self.two_players = tk.Button(self.gameSettingsWindow, text = '2', command = lambda: self.no_of_players(2), font = arial10)
		self.two_players.grid(row = 1, column = 2)
		# three players for game
		self.three_players = tk.Button(self.gameSettingsWindow, text = '3', command = lambda: self.no_of_players(3), font = arial10)
		self.three_players.grid(row = 1, column = 3)
		# four players for game
		self.three_players = tk.Button(self.gameSettingsWindow, text = '4', command = lambda: self.no_of_players(4), font = arial10)
		self.three_players.grid(row = 1, column = 4)

		# enter player names
		self.playerNamesLabel = Label(self.gameSettingsWindow, text = 'Enter Player Names:', font = arial10_bold)
		self.playerNamesLabel.grid(row = 2)
		# entry for player one
		self.playeroneLabel = Label(self.gameSettingsWindow, text = 'Player 1:', font = arial10_bold)
		self.playeroneLabel.grid(row = 3, column = 0)
		self.p1_entry = Entry(self.gameSettingsWindow, bd = 5)
		self.p1_entry.grid(row = 4, column = 0)
		# entry for player two
		self.playertwoLabel = Label(self.gameSettingsWindow, text = 'Player 2:', font = arial10_bold)
		self.playertwoLabel.grid(row = 5, column = 0)
		self.p2_entry = Entry(self.gameSettingsWindow, bd = 5)
		self.p2_entry.grid(row = 6, column = 0)
		# entry for player three
		self.playerthreeLabel = Label(self.gameSettingsWindow, text = 'Player 3:', font = arial10_bold)
		self.playerthreeLabel.grid(row = 7, column = 0)
		self.p3_entry = Entry(self.gameSettingsWindow, bd = 5)
		self.p3_entry.grid(row = 8, column = 0)
		# entry for player four
		self.playerfourLabel = Label(self.gameSettingsWindow, text = 'Player 4:', font = arial10_bold)
		self.playerfourLabel.grid(row = 9, column = 0)
		self.p4_entry = Entry(self.gameSettingsWindow, bd = 5)
		self.p4_entry.grid(row = 10, column = 0)

		# add button to access dice roll
		self.diceButton = tk.Button(self.gameSettingsWindow, text = 'Roll Dice', font = arial10_bold)
		self.diceButton.grid(row = 11, sticky = 'EW')

		# select number of players
		self.noTurns = Label(self.gameSettingsWindow, text = 'Select Number of Turns:', font = arial10_bold)
		self.noTurns.grid(row = 12, column = 0)
		# button for 10 turns
		self.tenTurns = tk.Button(self.gameSettingsWindow, text = '10', command = lambda: self.turns(10), font = arial10)
		self.tenTurns.grid(row = 12, column = 1)
		# button for 15 turns
		self.fifteenTurns = tk.Button(self.gameSettingsWindow, text = '15', command = lambda: self.turns(15), font = arial10)
		self.fifteenTurns.grid(row = 12, column = 2)
		# button for 20 turns
		self.twentyTurns = tk.Button(self.gameSettingsWindow, text = '20', command = lambda: self.turns(20), font = arial10)
		self.twentyTurns.grid(row = 12, column = 3)

		# select answer time limit
		self.timeLimit = Label(self.gameSettingsWindow, text = 'Select Timer for Answers (in seconds):', font = arial10_bold)
		self.timeLimit.grid(row = 13, column = 0)
		# 5 second time limit
		self.fiveSec = tk.Button(self.gameSettingsWindow, text = '5', command = lambda: self.time_limit(5), font = arial10)
		self.fiveSec.grid(row = 13, column = 1)
		# 10 second time limit
		self.tenSec = tk.Button(self.gameSettingsWindow, text = '10', command = lambda: self.time_limit(10), font = arial10)
		self.tenSec.grid(row = 13, column = 2)
		# 15 second time limit
		self.fifteenSec = tk.Button(self.gameSettingsWindow, text = '15', command = lambda: self.time_limit(15), font = arial10)
		self.fifteenSec.grid(row = 13, column = 3)

		# select game difficulty
		self.gameDifficulty = Label(self.gameSettingsWindow, text = 'Select Game Difficulty:', font = arial10_bold)
		self.gameDifficulty.grid(row = 14, column = 0)
		# 5 second time limit
		self.easyDifficulty = tk.Button(self.gameSettingsWindow, text = 'Easy', command = lambda: self.difficulty_level('easy'), font = arial10)
		self.easyDifficulty.grid(row = 14, column = 1)
		# 10 second time limit
		self.normDifficulty = tk.Button(self.gameSettingsWindow, text = 'Normal', command = lambda: self.difficulty_level('normal'), font = arial10)
		self.normDifficulty.grid(row = 14, column = 2)
		# 15 second time limit
		self.hardDifficulty = tk.Button(self.gameSettingsWindow, text = 'Hard', command = lambda: self.difficulty_level('hard'), font = arial10)
		self.hardDifficulty.grid(row = 14, column = 3)

		# add button to exit program
		self.exitGameSettings = tk.Button(self.gameSettingsWindow, text = 'Enter New Game', command = self.exitGamePlaySettings, font = arial10_bold)
		self.exitGameSettings.grid(stick = 'EW')

	def exitGamePlaySettings(self):

		print('Close new game settings and proceed to new game')
		self.gameSettingsWindow.destroy()
		game_window = tp_gameboard.TrivialPurfruitGameBoard()

	def no_of_players(self, num):

		if num == 1:
			print('Disable name entries for player 2-4 for game')
			# disable entry for player 2
			self.p2_entry = Entry(self.gameSettingsWindow, state = 'disabled', bd = 5)
			self.p2_entry.grid(row = 6, column = 0)
			# disable entry for player 3
			self.p3_entry = Entry(self.gameSettingsWindow, state = 'disabled', bd = 5)
			self.p3_entry.grid(row = 8, column = 0)
			# disable entry for player 4
			self.p4_entry = Entry(self.gameSettingsWindow, state = 'disabled', bd = 5)
			self.p4_entry.grid(row = 10, column = 0)
		elif num == 2:
			print('Disable name entries for player 3-4 for game')
			# enable entry for player 2
			self.p2_entry = Entry(self.gameSettingsWindow, state = 'normal', bd = 5)
			self.p2_entry.grid(row = 6, column = 0)
			# disable entry for player 3
			self.p3_entry = Entry(self.gameSettingsWindow, state = 'disabled', bd = 5)
			self.p3_entry.grid(row = 8, column = 0)
			# disable entry for player 4
			self.p4_entry = Entry(self.gameSettingsWindow, state = 'disabled', bd = 5)
			self.p4_entry.grid(row = 10, column = 0)
		elif num == 3:
			# enable entry for player 2
			self.p2_entry = Entry(self.gameSettingsWindow, state = 'normal', bd = 5)
			self.p2_entry.grid(row = 6, column = 0)
			# enable entry for player 3
			self.p3_entry = Entry(self.gameSettingsWindow, state = 'normal', bd = 5)
			self.p3_entry.grid(row = 8, column = 0)
			print('Disable name entries for player 4 for game')
			# disable entry for player 4
			self.p4_entry = Entry(self.gameSettingsWindow, state = 'disabled', bd = 5)
			self.p4_entry.grid(row = 10, column = 0)
		elif num == 4:
			print('Disable no entries, max number of players in game')
			# enable entry for player 1
			self.p2_entry = Entry(self.gameSettingsWindow, state = 'normal', bd = 5)
			self.p2_entry.grid(row = 4, column = 0)
			# enable entry for player 2
			self.p3_entry = Entry(self.gameSettingsWindow, state = 'normal', bd = 5)
			self.p3_entry.grid(row = 6, column = 0)
			# enable entry for player 3
			self.p2_entry = Entry(self.gameSettingsWindow, state = 'normal', bd = 5)
			self.p2_entry.grid(row = 8, column = 0)
			# enable entry for player 4
			self.p3_entry = Entry(self.gameSettingsWindow, state = 'normal', bd = 5)
			self.p3_entry.grid(row = 10, column = 0)

	def turns(self, num):

		print('Selected {} number of turns for gameplay'.format(num))

	def time_limit(self, time):

		print('Selected {} seconds to answer questions'.format(time))

	def difficulty_level(self, level):

		print('Selected {} difficulty level for gameplay'.format(level))