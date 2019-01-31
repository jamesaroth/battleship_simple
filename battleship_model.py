from arepldump import dump

# import os
# os.system("clear")

# class Gameboard:

#     def __init__(self, rows, columns):
#         self.__data = tuple([None] * columns for row in range(rows))
#         self.__rows, self.__columns = rows, columns

#     def __repr__(self):
#         table = Gameboard(self.__rows, self.__columns)
#         rows, columns = [0] * self.__rows, [0] * self.__columns
#         for (row, column), value in self:
#             lines = tuple(repr(value).replace('\r\n', '\n')
#                           .replace('\r', '\n').split('\n'))
#             table[row, column] = self.__yield(lines)
#             rows[row] = max(rows[row], len(lines))
#             columns[column] = max(columns[column], max(map(len, lines)))
#         return ('\n' + '+'.join('-' * column for column in columns) + '\n') \
#                .join('\n'.join('|'.join(next(table[row, column])
#                .ljust(columns[column]) for column in range(table.columns))
#                for line in range(rows[row])) for row in range(table.rows))
    
#     def __len__(self):
#         return self.rows * self.columns

#     def __getitem__(self, key):
#         row, column = key
#         return self.__data[row][column]

#     def __setitem__(self, key, value):
#         row, column = key
#         self.__data[row][column] = value

#     def __delitem__(self, key):
#         self[key] = None

#     def __iter__(self):
#         for row in range(self.rows):
#             for column in range(self.columns):
    
    
class Gameboard:   
    
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.data = []
        for _ in range(rows):
            self.data.append("\r")
            for _ in range(cols):
                self.data.append("  ")
    
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







