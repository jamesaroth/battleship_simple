import view
from computerboard import ComputerBoard
import sys

NUMSHIPS = 3

def run():
    if len(sys.argv) > 1 and sys.argv[1] == "--cheat":
        cheat = True
    else:
        cheat = False
    # print welcome message
    view.welcome()
    # generate computer's board
    board = ComputerBoard()
    while board.count_symbol('S') < NUMSHIPS:
        board.random_ship()

    while not board.no_ships():
        if cheat:
            print(board)
        else:
            view.show_board(board)
        x, y = view.get_attack_coords(board)
        board.attack(x, y)

    view.goodbye()

    # start main loop
    # display current player view of board
    # player makes attacks
    # if no ships left, exit loop

    # print goodbye message

if __name__ == "__main__":
    run()
