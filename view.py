
def welcome():
    print("Welcome to Battleship!")
    print()

def show_board(board):
    print(board.view())

def get_attack_coords(board):
    while True:
        value_x = input("x coordinate to attack: ")
        value_y = input("y coordinate to attack: ")
        try:
            x = int(value_x)
            y = int(value_y)
        except ValueError:
            print(" invalid input!")
            continue
        if x < 0 or x >= board.width or y < 0 or y >= board.height:
            print(" coordinates out of range!")
            continue
        break
    return x, y

def goodbye():
    print("You hit all the ships! Thanks for playing!")
