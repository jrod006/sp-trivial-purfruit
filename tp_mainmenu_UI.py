from PIL import ImageTk, Image
from tkinter import Label, Entry, StringVar, font
import tkinter as tk
import tp_gamesettings_UI
import tp_admin_UI

class MainMenu:

    def __init__(self):

        # initialize main menu window
        self.root = tk.Tk()
        self.root.title('Trivial Purfruit Main Menu')
        self.default_bg = self.root.cget('bg')
        self.panel = None

        print('Open Main Menu window...')
        # set font for GUIs
        self.arial = font.Font(family = 'Arial', size = 14)
        self.arial_bold = font.Font(family = 'Arial', size = 14, weight = 'bold')

        # trivial purfruit welcome text
        self.mainlabel = Label(text = 'Welcome to Trivial Purfruit!', font = self.arial_bold)
        self.mainlabel.grid()
        self.infolabel = Label(text = 'The game of trivia to test your Declaration of Independence knowledge', font = self.arial)
        self.infolabel.grid()

        # add image for main screen
        self.img = Image.open('./res/continental_congress.jpeg')
        self.photo = ImageTk.PhotoImage(self.img)
        self.congress_img = Label(image = self.photo)
        self.congress_img.grid()

        # add button to initiate new game
        self.newgame = tk.Button(self.root, text = 'Start New Game', command = self.startgame, font = self.arial)
        self.newgame.grid(sticky = 'EW')

        # add button to access game settings
        self.settings = tk.Button(self.root, text = 'Access Database', command = self.accessAdminSettings, font = self.arial)
        self.settings.grid(sticky = 'EW')

        # add button to exit program
        self.exit = tk.Button(self.root, text = 'Exit Trivial Purfruit', command = self.exit, font = self.arial)
        self.exit.grid(stick = 'EW')

    def startgame(self):
        print('Open game settings window...')
        pregameplay_window = tp_gamesettings_UI.GameSettings()

    def accessAdminSettings(self):
        print('Access admin settings')
        admin_window = tp_admin_UI.AdminAuthUI()

    def exit(self):

        print('Shutdown Trivial Purfruit game...')
        self.root.quit()
