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

class Victory:

    def __init__(self, winners):

        print('Winners: ', winners)

        print('Open window to display game results (victory)...')
        # set font type and size in root window
        arial = font.Font(family = 'Arial', size = 14)
        arial_bold = font.Font(family = 'Arial', size = 20, weight = 'bold')

        self.victoryWindow = tk.Toplevel()
        self.victoryWindow.title('TP Game Victory')
        self.frame = tk.Frame(self.victoryWindow)

        # self.firstPlace = winners[0]
        # self.secondPlace = winners[1]
        # self.thirdPlace = winners[2]
        # self.fourthPlace = winners[3]

        # trivial pursuit game results label
        self.victoryHeadLabel = Label(self.victoryWindow, text = 'Game Results', font = arial_bold)
        self.victoryHeadLabel.grid(sticky = 'EW', row = 0, column = 0)

        self.firstPlaceText = "First Place: " + winners[0].id
        self.firstPlaceLabel = Label(self.victoryWindow, text = self.firstPlaceText, font = arial)
        self.firstPlaceLabel.grid(sticky='EW', row=200, column=0)

        self.secondPlaceText = "Second Place: " + winners[1].id
        self.secondPlaceLabel = Label(self.victoryWindow, text=self.secondPlaceText, font=arial)
        self.secondPlaceLabel.grid(sticky='EW', row=300, column=0)

        if (len(winners) > 2):
            self.thirdPlaceText = "Third Place: " + winners[2].id
            self.thirdPlaceLabel = Label(self.victoryWindow, text=self.thirdPlaceText, font=arial)
            self.thirdPlaceLabel.grid(sticky='EW', row=400, column=0)

        if (len(winners) > 3):
            self.fourthPlaceText = "Fourth Place: " + winners[3].id
            self.fourthPlaceLabel = Label(self.victoryWindow, text=self.fourthPlaceText, font=arial)
            self.fourthPlaceLabel.grid(sticky='EW', row=500, column=0)

        self.congratsLabel = Label(self.victoryWindow, text="Congratulations, Players!", font=arial)
        self.congratsLabel.grid(sticky='EW', row=600, column=0)

        self.close = tk.Button(self.victoryWindow, text='Back to Main Menu', command=lambda: self.mainMenu(), font=arial)
        self.close.grid(sticky='EW', row=700, column=0)

    def mainMenu(self):
        print('Close new game settings and return to Main Menu')
        self.victoryWindow.destroy()

if __name__ == "__main__":

    v = Victory()


 