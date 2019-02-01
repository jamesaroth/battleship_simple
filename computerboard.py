from gameboard import Gameboard
from random import randint

class ComputerBoard(Gameboard):

    def random_ship(self):
        width = len(self.data[0])
        height = len(self.data)
        x = randint(0, width-1)
        y = randint(0, height-1)
        self[x, y] = 'S'
