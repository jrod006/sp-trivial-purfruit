import tp_settings

class StartScreen:

    def __init__(self, parent):
        print("INIT START SCREEN UI")
        settings = tp_settings.Settings()
        self.currentSettings = settings.getSettings()
        self.parent=parent

    def show(self):
        print("SHOWING STARTUP SCREEN EDIT/CONFIRM SETTINGS HERE")
        print(self.currentSettings)
        input("PRESS ENTER TO CONFIRM SETTINGS")
        self.parent.currentSettings=self.currentSettings
    
