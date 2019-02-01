from arepldump import dump

    
    
class Gameboard:   
    
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.data = [] # list with a number of elements equal to #rows, each
                        # row is a list with a number of string elements equal
                        # to #cols
        for r in range(rows):
            newrow = []
            for c in range(cols):
                newrow.append(" ")
            self.data.append(newrow)
    
    def __iter__(self):
        yield from self.data
    
    def __getitem__(self, row):
        return self.data[row]
    
    def __setitem__(self, key, value):
        col, row = key
        self.data[col][row] = value
    
    def __str__(self):
        display = []
        for row in self.data:
            display.append(" ".join(row))
        return "| |".join(display)

x = Gameboard(3,3)
print(x)

# print(Gameboard(5,5))







