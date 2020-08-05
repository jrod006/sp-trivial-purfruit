from PIL import ImageTk, Image
from tkinter import Label, Entry, StringVar, font, Listbox
import tkinter as tk
import tp_admin_database_UI
import json
import time
import pandas as pd

class AdminAuthUI:

    with open('./res/Settings.json') as json_file:
        credentials = json.load(json_file)

    def __init__(self):

        print('Open window to authenticate user and access database')
        # set font type and size in root window
        self.arial = font.Font(family = 'Arial', size = 14)
        self.arial_bold = font.Font(family = 'Arial', size = 14, weight = 'bold')

        self.adminAuthWindow = tk.Toplevel()
        # self.adminAuthWindow.geometry("500x400")
        self.adminAuthWindow.title('Database Authentication')
        self.frame = tk.Frame(self.adminAuthWindow)

        # enter player names
        self.adminLabel = Label(self.adminAuthWindow, text = 'ENTER ADMIN CREDENTIALS', font = self.arial_bold)
        self.adminLabel.grid(column = 0)
        # admin username entry
        self.usernameLabel = Label(self.adminAuthWindow, text = 'Username:', font = self.arial_bold)
        self.usernameLabel.grid(row = 1, column = 0)
        self.usernameEntry = Entry(self.adminAuthWindow, bd = 5)
        self.usernameEntry.grid(row = 1, column = 1)
        # admin password entry
        self.passwordLabel = Label(self.adminAuthWindow, text = 'Password:', font = self.arial_bold)
        self.passwordLabel.grid(row = 2, column = 0)
        self.passwordEntry = Entry(self.adminAuthWindow, bd = 5)
        self.passwordEntry.grid(row = 2, column = 1)

        # button to enter username/password
        self.submitCredentials = tk.Button(self.adminAuthWindow, text = 'Authenticate', command = self.authenticate, font = self.arial)
        self.submitCredentials.grid(column = 0)

       # add button to exit program
        self.exitGameSettings = tk.Button(self.adminAuthWindow, text = 'Exit Admin Settings', command = self.close, font = self.arial)
        self.exitGameSettings.grid(column = 0)

    def showUI(self):
        print('Show admin UI window...')

    def authenticate(self):
        
        if self.usernameEntry.get() == self.credentials['username'] and self.passwordEntry.get() == self.credentials['adminPassword']:
            database_window = tp_admin_database_UI.AdminSettings()
            print('Database Access Granted...')
        else:
            self.usernameEntry.delete(0, 'end')
            self.passwordEntry.delete(0, 'end')
            print('Incorrect Credentials, Try Again...')

    def addQuestion(self, category, question, answer):
        print('Add question to database...')
        print('Category: {}'.format(category))
        print('New Question: {}'.format(question))
        print('Question Answer: {}'.format(answer))

    def removeQuestion(self, category, question, answer):
        print('View all questions in database')
        print('Remove question from database based on index of question/answer')

    def updateQuestion(self):
        print('Update question')

    def close(self):
        print('Close Admin Settings UI')
        self.adminAuthWindow.destroy()
        
