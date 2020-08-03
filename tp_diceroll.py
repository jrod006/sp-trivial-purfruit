from random import randint

class DiceRoll:

    def __init__(self):

        print('DICE ROLL INIT')

    @staticmethod
    def rollDice():

        return randint(1, 6)
