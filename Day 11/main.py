# Checkers lab
# Connor Critchley

# initial imports
import checkers


def game():
    board = checkers.build_board(int(input("How big is the board?\n")))
    print(board)
    print(f"Empty spaces: {checkers.get_count(board, 'Empty')}")
    print(f"Red spaces: {checkers.get_count(board, 'Red')}")
    print(f"Black spaces: {checkers.get_count(board, 'Black')}")


if __name__ == '__main__':
    game()