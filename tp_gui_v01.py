from PIL import ImageTk, Image
from tkinter import Label, Entry, StringVar, font
import tkinter as tk
import os
import tp_settings as tpset
import tp_game as tpgame

class TrivialPurfruit:

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
		self.newgame = tk.Button(self.root, text = 'Begin New Game', command = self.newGameSettings, font = arial10)
		self.newgame.grid(sticky = 'EW')

		# add button to access game settings
		self.settings = tk.Button(self.root, text = 'Settings', command = self.programSettings, font = arial10)
		self.settings.grid(sticky = 'EW')

	def newGameSettings(self):
		print('Open window for new game settings')
		tpgame.testGame()


	def programSettings(self):

		print('Open window for program settings')
                #For Skeletal demo just run the settings demo to show the connectivity/Auth
		tpset.testSettings()
                

	def gameBoard(self):

		print('Open window of game board for play')

if __name__ == "__main__":

	window = TrivialPurfruit()
	window.root.mainloop()
