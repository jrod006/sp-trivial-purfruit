from PIL import ImageTk, Image
from tkinter import Label, Entry, StringVar, font
import tkinter as tk
import tp_game
import tp_startScreen
import os

class TrivialPurfruitGameBoard:

	def __init__(self):

		# set font type and size in root window
		arial10 = font.Font(family = 'Arial', size = 14)
		arial10_bold = font.Font(family = 'Arial', size = 14, weight = 'bold')

		self.gameBoardWindow = tk.Toplevel()
		self.frame = tk.Frame(self.gameBoardWindow)

		# temp title
		self.game_title = Label(self.gameBoardWindow, text = 'TRIVIAL PURFRUIT', font = arial10_bold)
		self.game_title.grid(column = 0)

		# add image for main screen
		self.tp_img = Image.open('./res/trivial_pursuit_holder.jpg')
		self.tp_photo = ImageTk.PhotoImage(self.tp_img)
		self.tp_holder_img = Label(self.gameBoardWindow, image = self.tp_photo)
		self.tp_holder_img.grid()

		# button to begin game simulation
		self.gameSimulation = tk.Button(self.gameBoardWindow, command = self.game_simulation, text = 'Begin Game Simulation', font = arial10_bold)
		self.gameSimulation.grid(sticky = 'EW')

		# add button to access dice roll
		self.gameExitButton = tk.Button(self.gameBoardWindow, command = self.closeGameBoard, text = 'Exit Game Board', font = arial10_bold)
		self.gameExitButton.grid(sticky = 'EW')

	def closeGameBoard(self):

		print('Closing game board')
		self.gameBoardWindow.destroy()

	def game_simulation(self):

		game = tp_game.Game()
		game.run()
                
