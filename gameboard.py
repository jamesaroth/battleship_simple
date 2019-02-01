from arepldump import dump
import os

# SPACES:
# ' ' : empty square
# 'S' : square with an unhit ship square
# 'X' : square with a hit ship square
# 'O' : square where a miss has happened

class Gameboard:   
    
    def __init__(self, cols=10, rows=10):
        self.cols = cols
        self.rows = rows
        self.data = [] # list with a number of elements equal to #rows, each
                        # row is a list with a number of string elements equal
                        # to #cols
        self.width = cols
        self.height = rows
        # TODO: rewrite other methods to use width, height instead of len(data)
        
        for r in range(rows):
            newrow = []
            for c in range(cols):
                newrow.append(" ")
            self.data.append(newrow)
    
    # def __iter__(self):
    #    yield from self.data
    
    def __getitem__(self, index_tuple):
        col, row = index_tuple
        return self.data[row][col]
    
    def __setitem__(self, index_tuple, value):
        col, row = index_tuple
        self.data[row][col] = value

    def place_ship(self, x, y):
        self[x, y] = "S"

    def print_first_row(self):
        print(",".join(self.data[0]))
  
    def attack(self, x, y):
        """ if x,y is a ship, mark X if blank mark O, leave X or O unchanged"""
        if self[x, y] == 'S':
            self[x, y] = 'X'
        elif self[x, y] == ' ':
            self[x, y] = 'O'

    def view(self, hide_symbols= ('S',)):
        result = ""
        for row in self.data:
            for col in row:
                if col not in hide_symbols:
                    sym = col
                else:
                    sym = " "
                result = result + "[{}] ".format(sym)
            result = result + os.linesep
        return result

    def count_symbol(self, symbol):
        _sum = 0
        for row in self.data:
            for col in row:
                if col == symbol:
                    _sum = _sum + 1
        return _sum

    def no_ships(self):
        if self.count_symbol('S') == 0:
            return True
        else:
            return False

    def __str__(self):
        return self.view(tuple())

def run():
    x = Gameboard(3,3)
    print(x)

if __name__ == "__main__":
    run()
