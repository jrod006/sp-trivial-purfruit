from tp_database import Database
import pandas as pd
import os

class QuestionGenerator:

        def __init__(self):
                print('INIT QUESTION GENERATOR')
                self.df = pd.read_csv('./res/trivial_purfruit_questions.csv')
                self.colors = list(set(self.df['color'].tolist()))
                self.categories = {'White': 'Events','Blue': 'Places','Green': 'Independence Day','Red': 'People'}

        def retrieveQA(self):

                self.color = input('Enter color to determine question category: ')
                self.ques, self.ans = Database.retrieveQuesAns(self, self.color)
                print('Question: ', self.ques)
                print('Answer: ', self.ans)

if __name__ == "__main__":
       
        QG = QuestionGenerator()
        QG.retrieveQA()
                
