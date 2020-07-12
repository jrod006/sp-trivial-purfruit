import json
import os

class Settings:


    def __init__(self):
        # Load Settings from file on startup of settings module
        with open('./res/settings.json') as f:
            self.settings = json.load(f)
            self.auth = False

    def save(self):
        with open('./res/settings.json', "w") as f:
            f.write(json.dumps(settings))

    def getSettings(self):
        return self.settings
        

    def authenticate(self):
        #In the future this is the result of a text field check
        entered_pass = input("Enter the Admin Password: ")
        if (entered_pass == self.settings['adminPassword']):
            print("AUTH")
            self.auth=True
            return True
        else:
            print("NO AUTH")
            self.auth=False
            return False

    def getQuestions(self):
        # DB module get all questions
        print('ALL QUESTIONS')








def testSettings():
    settings = Settings()
    print(settings.getSettings())
    while (not settings.auth):
        if settings.authenticate():
            print(settings.getQuestions())


# Basically Unit Testing
if __name__ == "__main__":
    testSettings()
