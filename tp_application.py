from tp_mainmenu_UI import MainMenu

class Application:

	def __init__(self):
		print('Start Application...')

	def run(self):
		self.main = MainMenu()
		self.main.root.mainloop()

if __name__ == "__main__":

	app = Application()
	app.run()