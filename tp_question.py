from tp_database import Database
import pandas as pd
import os

class QuestionGenerator:

        def __init__(self):
                print('INIT QUESTION GENERATOR')
                #self.categories = {'White': 'Events','Blue': 'Places','Green': 'Independence Day','Red': 'People'}
                self.categories = {'Events':'White','Places': 'Blue','Independence Day': 'Green','People': 'Red'}
                self.colors = ['White', 'Blue', 'Green', 'Red']
                currentQuestion = {}

        def getRandomQuestion(self, category):
                
                self.currentQuestion = Database().retrieveQuesAns(category)
                return self.currentQuestion

                # self.currentQuestion = Database.retrieveQuesAns(self.colors[category])
                # return self.currentQuestion['question']

        def checkAnswer(answer):
                if answer == self.currentQuestion['answer']:
                        return True
                else:
                        return False

if __name__ == "__main__":

        #This is demo is broken for now
        QG = QuestionGenerator()
        #QG.retrieveQA()
                
