import warnings
warnings.simplefilter(action = 'ignore', category = FutureWarning)
import pandas as pd
from PIL import ImageTk, Image
from tkinter import Label, Entry, StringVar, font, Listbox
import tkinter as tk
from csv import reader

class AdminSettings:

    categories = {
                            'Events': 'White',
                            'Places': 'Blue',
                            'Independence Day': 'Green',
                            'People': 'Red'
                        }
    df = pd.read_csv('./res/trivial_purfruit_questions.csv')
    category_list = list(set(df['category'].tolist()))

    def __init__(self):

        print('Open window to initialize settings for new game...')

        # set font type and size in root window
        self.arial = font.Font(family = 'Arial', size = 14)
        self.arial_bold = font.Font(family = 'Arial', size = 14, weight = 'bold')

        self.databaseWindow = tk.Toplevel()
        self.databaseWindow.title('Trivial Purfruit Question Database')
        self.frame = tk.Frame(self.databaseWindow)

        ######################################### ADD QUESTION TO DATABASE #############################################
        # new category label
        self.newCategoryLabel = Label(self.databaseWindow, text = 'Category of New Question:', font =self.arial_bold)
        self.newCategoryLabel.grid(row = 0, column = 0)
        # new category entry
        self.newCategoryEntry = Entry(self.databaseWindow, bd = 5)
        self.newCategoryEntry.grid(row = 0, column = 1)
        # new question label
        self.newQuestionLabel = Label(self.databaseWindow, text = 'New Question:', font = self.arial_bold)
        self.newQuestionLabel.grid(row = 1, column = 0)
        # new question entry
        self.newQuestionEntry = Entry(self.databaseWindow, bd = 5)
        self.newQuestionEntry.grid(row = 1, column = 1)
        # new answer label
        self.newAnswerLabel = Label(self.databaseWindow, text = 'New Question Answer:', font = self.arial_bold)
        self.newAnswerLabel.grid(row = 2, column = 0)
        # new answer entry
        self.newAnswerEntry = Entry(self.databaseWindow, bd = 5)
        self.newAnswerEntry.grid(row = 2, column = 1)
        # add question button
        self.add_question = tk.Button(self.databaseWindow, text = 'Add Question', command = self.addQuestion, font = self.arial)
        self.add_question.grid(row = 3, column = 1)

        ######################################### UPDATE QUESTION IN DATABASE #############################################

        self.update_question = tk.Button(self.databaseWindow, text = 'Retrieve Question to Modify', command = self.getQuestion, font = self.arial)
        self.update_question.grid(row = 4, column = 1)
        # label for question to modify
        self.retrieveQuestionLabel = Label(self.databaseWindow, text = 'Question to be Updated:', font = self.arial_bold)
        self.retrieveQuestionLabel.grid(row = 5, column = 0)
        # entry to retrieve question to modify
        self.retrieveQuestionEntry = Entry(self.databaseWindow, bd = 5)
        self.retrieveQuestionEntry.grid(row = 5, column = 1)
        # label for answer to modify
        self.retrieveAnswerLabel = Label(self.databaseWindow, text = 'Answer to be Updated:', font = self.arial_bold)
        self.retrieveAnswerLabel.grid(row = 6, column = 0)
        # entry to retrieve answer to modify
        self.retrieveAnswerEntry = Entry(self.databaseWindow, bd = 5)
        self.retrieveAnswerEntry.grid(row = 6, column = 1)
        # label for category to modify
        self.retrieveCategoryLabel = Label(self.databaseWindow, text = 'Category to be Updated:', font = self.arial_bold)
        self.retrieveCategoryLabel.grid(row = 7, column = 0)
        # entry to retrieve category to modify
        self.retrieveCategoryEntry = Entry(self.databaseWindow, bd = 5)
        self.retrieveCategoryEntry.grid(row = 7, column = 1)
        # button to update modified question in database
        self.confirmModification = tk.Button(self.databaseWindow, command = self.updateQuestion, text = 'Update Changes')
        self.confirmModification.grid(row = 9, column = 1)

        ######################################### REMOVE QUESTION IN DATABASE #############################################

        # remove question button
        self.delete_question = tk.Button(self.databaseWindow, text = 'Remove Question', command = self.deleteQuestion, font = self.arial)
        self.delete_question.grid(row = 10, column = 1)

        ######################################### SWAP COLOR CATEGORY IN DATABASE #############################################

        # color to be replaced label
        self.oldColorLabel = Label(self.databaseWindow, text = 'Category of Color to be Replaced:', font = self.arial_bold)
        self.oldColorLabel.grid(row = 11, column = 0)
        # color to be replaced entry
        self.oldColorEntry = Entry(self.databaseWindow, bd = 5)
        self.oldColorEntry.grid(row = 11, column = 1)
        # new color of category label
        self.newColorLabel = Label(self.databaseWindow, text = 'New Color for Category:', font = self.arial_bold)
        self.newColorLabel.grid(row = 12, column = 0)
        # new color of category entry
        self.newColorEntry = Entry(self.databaseWindow, bd = 5)
        self.newColorEntry.grid(row = 12, column = 1)
        # swap colors of category button
        self.swap_colors = tk.Button(self.databaseWindow, text = 'Swap Color Category', command = self.swapColors, font = self.arial)
        self.swap_colors.grid(row = 13, column = 1)

        ######################################### SAVE/CLOSE BUTTON #############################################

        # save database button
        self.save_question = tk.Button(self.databaseWindow, text = 'Save and Close Database', command = self.saveDatabase, font = self.arial)
        self.save_question.grid(row = 14, column = 1, pady = 5)

        # insert listbox of questions
        self.question_list = tk.Listbox(self.databaseWindow, font = self.arial, height = 40, width = 90)
        self.question_list.grid(row = 0, column = 2, rowspan = 16, sticky = 'EW', padx = 10)
        self.question_list.insert(tk.END, 'Index\tColor\tCategory\tQuestion\tAnswer')
        with open('./res/trivial_purfruit_questions.csv', 'r') as file:
            csv_reader = reader(file)
            header = next(csv_reader)
            if header != None:
                for row in enumerate(csv_reader):
                    self.question_list.insert(tk.END, str(row[0]) + '\t' + str(row[1]))
        self.scrollbar = tk.Scrollbar(self.question_list, orient = 'vertical')

    def addQuestion(self):

        print('Add question to database...')
        if self.newCategoryEntry.get() in self.category_list:
            print('Color of new question: {}'.format(self.categories[self.newCategoryEntry.get()]))
        self.new_question = self.newQuestionEntry.get()
        self.new_answer = self.newAnswerEntry.get()
        self.new_data = [
                            self.categories[self.newCategoryEntry.get()],
                            self.newCategoryEntry.get(),
                            self.new_question,
                            self.new_answer
                        ]
        self.new_df = pd.DataFrame([self.new_data], columns = self.df.keys())
        self.df = self.df.append(self.new_df, ignore_index = True)
        self.df.to_csv('./res/trivial_purfruit_questions.csv', index = False)
        self.newCategoryEntry.delete(0, 'end')
        self.newQuestionEntry.delete(0, 'end')
        self.newAnswerEntry.delete(0, 'end')
        self.question_list.delete(0, tk.END)
        with open('./res/trivial_purfruit_questions.csv', 'r') as file:
            csv_reader = reader(file)
            header = next(csv_reader)
            if header != None:
                for row in enumerate(csv_reader):
                    self.question_list.insert(tk.END, str(row[0]) + '\t' + str(row[1]))
        self.scrollbar = tk.Scrollbar(self.question_list, orient = 'vertical')

    def deleteQuestion(self):

        print('Remove question from database...')
        self.value = self.question_list.get(self.question_list.curselection())
        self.value = self.value.split()
        self.index_no = int(self.value[0])
        print(self.index_no)
        self.df = self.df.drop(self.index_no)
        self.df = self.df.reset_index(drop = True)
        self.df.to_csv('./res/trivial_purfruit_questions.csv', index = False)
        self.question_list.delete(0, tk.END)
        with open('./res/trivial_purfruit_questions.csv', 'r') as file:
            csv_reader = reader(file)
            header = next(csv_reader)
            if header != None:
                for row in enumerate(csv_reader):
                    self.question_list.insert(tk.END, str(row[0]) + '\t' + str(row[1]))
        self.scrollbar = tk.Scrollbar(self.question_list, orient = 'vertical')

    def getQuestion(self):

        print('Retrieve question in database...')
        self.value = self.question_list.get(self.question_list.curselection())
        self.value = self.value.split()
        self.index_no = int(self.value[0])
        rowData = self.df.loc[self.index_no, : ]
        self.retrieveQuestionEntry.insert(0, rowData['question'])
        self.retrieveAnswerEntry.insert(0, rowData['answer'])
        self.retrieveCategoryEntry.insert(0, rowData['category'])
        self.retrieveColorEntry.insert(0, rowData['color'])

    def updateQuestion(self):

        print('Update question in database')
        print('Index:', self.index_no)
        self.df = self.df.drop(self.index_no)
        self.new_data = [
                                    self.categories[self.retrieveCategoryEntry.get()],
                                    self.retrieveCategoryEntry.get(),
                                    self.retrieveQuestionEntry.get(),
                                    self.retrieveAnswerEntry.get()
                                ]
        self.new_df = pd.DataFrame([self.new_data], columns = self.df.keys())
        self.df = self.df.append(self.new_df, ignore_index = True)
        self.df.to_csv('./res/trivial_purfruit_questions.csv', index = False)
        self.retrieveCategoryEntry.delete(0, 'end')
        self.retrieveQuestionEntry.delete(0, 'end')
        self.retrieveAnswerEntry.delete(0, 'end')
        self.question_list.delete(0, tk.END)
        with open('./res/trivial_purfruit_questions.csv', 'r') as file:
            csv_reader = reader(file)
            header = next(csv_reader)
            if header != None:
                for row in enumerate(csv_reader):
                    self.question_list.insert(tk.END, str(row[0]) + '\t' + str(row[1]))
        self.scrollbar = tk.Scrollbar(self.question_list, orient = 'vertical')

    def readQuestionAnswer(self, category):

        print('Retrieve question and answer for gameplay')      
        if category in self.category_list:
                print('================================')
                print('Color:', self.categories[category])
                self.question_df = self.df[self.df['category'] == category].copy()
        else:
                print('Invalid entry, try again')
        random_row = self.question_df.sample(n = 1)
        question = random_row.iloc[0]['question']
        answer = random_row.iloc[0]['answer']

        return {'question':question, 'answer':answer}

    def swapColors(self):
        
        print('Change category colors...')
        self.replacement_color = self.oldColorEntry.get()
        self.color = self.newColorEntry.get()
        self.df = self.df.replace(to_replace = self.replacement_color, value = self.color)
        self.df.to_csv('./res/trivial_purfruit_questions.csv', index = False)
        self.oldColorEntry.delete(0, 'end')
        self.newColorEntry.delete(0, 'end')
        self.question_list.delete(0, tk.END)
        with open('./res/trivial_purfruit_questions.csv', 'r') as file:
            csv_reader = reader(file)
            header = next(csv_reader)
            if header != None:
                for row in enumerate(csv_reader):
                    self.question_list.insert(tk.END, str(row[0]) + '\t' + str(row[1]))
        self.scrollbar = tk.Scrollbar(self.question_list, orient = 'vertical')

    def saveDatabase(self):

        print('Saving database and closing database window...')
        self.databaseWindow.destroy()
