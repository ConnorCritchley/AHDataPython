# Checkers game lab
# Connor Critchley

# initial imports
from numpy import random as rand

# build board takes a board square size (nxn), returns numpy array as board
def build_board(size):
    return rand.choice(['Empty', 'Red', 'Black'], (size,size))


# Finds the count of target instances within the board parameter
def get_count(board, target):
    search = board == target
    return search.sum()

# Checks if running in own file
if __name__ == '__main__':
    print("Not meant to be run directly")