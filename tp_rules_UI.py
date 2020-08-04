from PIL import ImageTk, Image
from tkinter import Label, Entry, StringVar, font
import tkinter as tk

class RulesUI:

    def __init__(self):

        print('Open window to view game rules')
        # set font type and size in root window
        arial = font.Font(family = 'Arial', size = 14)
        arial_bold = font.Font(family = 'Arial', size = 14, weight = 'bold')

        self.rulesText = 'Overview:\nAnswer questions related to the Declaration of Independence \nand Continential Congress ' \
                            'against other players\n\nGame Components:\n40 questions related to 4 different categories:\nRed: People\n' \
                            'White: Events\nBlue: Places\nGreen: Independence Day\n\nWhen an answer is correctly answered, the player will\n' \
                            'receive a chip in the color associated with that question category.\n\nPregame Setup:\n\nPlaying the Game:\n\nWinning the Game:\n'

        self.gameRulesWindow = tk.Toplevel()
        self.frame = tk.Frame(self.gameRulesWindow)

        # trivial pursuit welcome label
        self.rulesTitleLabel = Label(self.gameRulesWindow, text = 'Trivial Purfruit Rules', font = arial_bold)
        self.rulesTitleLabel.grid()

        # trivial pursuit rules
        self.rulesLabel = Label(self.gameRulesWindow, text = self.rulesText, font = arial)
        self.rulesLabel.grid()

        # add button to exit rules
        self.exitGameSettings = tk.Button(self.gameRulesWindow, text = 'Exit Rules', command = self.close, font = arial_bold, height = 2, width = 6)
        self.exitGameSettings.grid(stick = 'EW')

    def close(self):
        print('Close Rules Window')
        self.gameRulesWindow.destroy()

