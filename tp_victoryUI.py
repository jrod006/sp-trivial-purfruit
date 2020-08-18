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
        arial_bold = font.Font(family = 'Arial', size = 14, weight = 'bold')

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

        self.firstPlaceText = "First Place: " + winners[0]
        self.firstPlaceLabel = Label(self.victoryWindow, text = firstPlaceText, font = arial_bold)
        self.firstPlaceLabel.grid(sticky='EW', row=0, column=200)

        self.secondPlaceText = "Second Place: " + winners[1]
        self.secondPlaceLabel = Label(self.victoryWindow, text=secondPlaceText, font=arial_bold)
        self.secondPlaceLabel.grid(sticky='EW', row=0, column=300)

        # if ('''number of players > 2'''):
        self.thirdPlaceText = "Third Place: " + winners[2]
        self.thirdPlaceLabel = Label(self.victoryWindow, text=thirdPlaceText, font=arial_bold)
        self.thirdPlaceLabel.grid(sticky='EW', row=0, column=400)

        # if ('''number of players > 3'''):
        self.fourthPlaceText = "Fourth Place: " + winners[3]
        self.fourthPlaceLabel = Label(self.victoryWindow, text=fourthPlaceText, font=arial_bold)
        self.fourthPlaceLabel.grid(sticky='EW', row=0, column=500)

    def mainMenu(self):
        print('Close new game settings and return to Main Menu')
        self.gameSettingsWindow.destroy()

if __name__ == "__main__":

    v = Victory()


 