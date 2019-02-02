
def welcome():
    print("Welcome to Battleship!")

def ask_boardsize():
    board_size = int(input("\nSelect board width and length.  Traditional Battleship is a 10x10 grid.\n"))
    return board_size

def show_board(board):
    print(board.view())

def get_attack_coords(board):
    while True:
        value_x = input("x coordinate to attack: ")
        value_y = input("y coordinate to attack: ")
        try:
            x = int(value_x) - 1
            y = int(value_y) - 1
        except ValueError:
            print(" invalid input!")
            continue
        if x < 0 or x >= board.width or y < 0 or y >= board.height:
            print(" coordinates out of range!")
            continue
        break
    return x, y

def miss():
    print("\nYou missed!!\n")

def hit():
    print("\nYou hit a ship!!\n")

def goodbye():
    print("You hit all the ships! Thanks for playing!\n")
