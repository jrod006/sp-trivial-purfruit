import pandas as pd
import os

def select_q_a(df):

	random_row = df.sample(n = 1)
	question = random_row.iloc[0]['question']
	answer = random_row.iloc[0]['answer']
	print('Question:', question)
	print('Answer:', answer)
	
	return question, answer

if __name__ == "__main__":

	file = '/Users/jacobrodriguez/Documents/johns_hopkins/coursework/eng.605.601.83/project/trivial_purfruit_questions.csv'
	df = pd.read_csv(file)
	colors = list(set(df['color'].to_list()))
	categories = {
					'White': 'Events',
					'Blue': 'Places',
					'Green': 'Independence Day',
					'Red': 'People'
				}

	questions = []

	while True:
		print('================================')
		if len(questions) == df.shape[0]:
			print('No more questions to ask...')
			break
		color = input('Enter color to determine question category ("Exit" to exit program): ')
		if color == 'Exit':
			print('Closing program...')
			break
		elif color in colors:
			print('================================')
			print('Category:', categories[color])
			question_df = df[df['color'] == color].copy()
			ques, anw = select_q_a(question_df)
			questions.append(ques)
		else:
			print('Invalid entry, try again')

		
