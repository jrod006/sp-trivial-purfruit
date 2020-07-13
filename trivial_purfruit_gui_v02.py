from PIL import ImageTk, Image
from tkinter import Label, Entry, StringVar, font
import tkinter as tk
import tp_gameboard
import tp_gamesettings
import os

class TrivialPurfruitMain:

	def __init__(self):

		# initialize the root window
		self.root = tk.Tk()
		self.default_bg = self.root.cget('bg')
		self.panel = None

		# set font type and size in root window
		arial10 = font.Font(family = 'Arial', size = 14)
		arial10_bold = font.Font(family = 'Arial', size = 14, weight = 'bold')

		# trivial pursuit welcome label
		self.mainlabel = Label(text = 'Welcome to Trivial Purfruit!', font = arial10_bold)
		self.mainlabel.grid()
		self.infolabel = Label(text = 'The game of trivia to test your Declaration of Independence knowledge')
		self.infolabel.grid()

		# add image for main screen
		self.img = Image.open('/Users/jacobrodriguez/Documents/johns_hopkins/coursework/eng.605.601.83/project/continental_congress.jpeg')
		self.photo = ImageTk.PhotoImage(self.img)
		self.congress_img = Label(image = self.photo)
		self.congress_img.grid()

		# add button to initiate new game
		self.newgame = tk.Button(self.root, text = 'Begin New Game', command = self.createNewGameSettings, font = arial10)
		self.newgame.grid(sticky = 'EW')

		# add button to access game settings
		self.settings = tk.Button(self.root, text = 'Settings', command = self.programSettings, font = arial10)
		self.settings.grid(sticky = 'EW')

		# add button to exit program
		self.exit = tk.Button(self.root, text = 'Exit Trivial Purfruit', command = self.exitGame, font = arial10)
		self.exit.grid(stick = 'EW')

	def createNewGameSettings(self):

		print('Open window for new game settings')
		game_window = tp_gamesettings.createNewGameSettings()

	def programSettings(self):

		print('Open window for program settings')

	def gameBoard(self):

		print('Open window of game board for play')
		game_window.root.mainloop()

	def exitGame(self):

		print('Close program')
		self.root.quit()

if __name__ == "__main__":

	window = TrivialPurfruitMain()
	window.root.mainloop()