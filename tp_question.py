import pandas as pd
import os

class QuestionGenerator:

	def __init__(self):

		print('INIT QUESTION GENERATOR')
		self.df = pd.read_csv('./res/trivial_purfruit_questions.csv')
		self.colors = list(set(self.df['color'].tolist()))
		self.categories = {
						'White': 'Events',
						'Blue': 'Places',
						'Green': 'Independence Day',
						'Red': 'People'
					}

		self.color = input('Enter color to determine question category: ')

		if self.color in self.colors:
					print('================================')
					print('Category:', self.categories[self.color])
					self.question_df = self.df[self.df['color'] == self.color].copy()
					self.loadQA(self.question_df)
		else:
			print('Invalid entry, try again')

	def loadQA(self, df):

		self.random_row = df.sample(n = 1)
		self.question = self.random_row.iloc[0]['question']
		self.answer = self.random_row.iloc[0]['answer']
		print('Question:', self.question)
		print('Answer:', self.answer)

if __name__ == "__main__":
       
        QuestionGenerator()
		