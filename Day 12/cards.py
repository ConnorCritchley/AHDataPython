# Connor Critchley
# Unit Testing lab // day 12

# Card value tuple
cards = ('S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SJ', 'SQ', 'SK', 'SA')
# num = num, j=11, q=12, k=13, A=14


# helper function to pull int value from cards, takes in single tuple index (card), returns int value
def numerical(card):
    if card == 'S10':
        return 10
    elif card[-1] not in ['J', 'Q', 'K', 'A']:
        return int(card[-1])
    else:
        match card[-1]:
            case 'J':
                return 11
            case 'Q':
                return 12
            case 'K':
                return 13
            case 'A':
                return 14


# Checks for adjacent values for a straight, returns highest value, otherwise returns 0
def check_straight(card1, card2, card3):
    if numerical(card2) == (numerical(card1) + 1) and numerical(card3) == (numerical(card2) + 1):
        return numerical(card3)
    else:
        return 0


# checks for 3 of a kind, matching values, returns value, otherwise returns 0
def check_3ofa_kind(card1, card2, card3):
    if numerical(card1) == numerical(card2) and numerical(card2) == numerical(card3):
        return numerical(card1)
    else:
        return 0


# Checks for royal flush, 12, 13, 14; uses straight function
def check_royal_flush(card1, card2, card3):
    if check_straight(card1, card2, card3) == 14:
        return 14
    else:
        return 0


# Plays cards, left win = -1, right win = 1, draw = 0 // I dunno if I'm overcomplicating, but this is a doozy
def play_cards(left1, left2, left3, right1, right2, right3):
    lhas = False  # left has currently checked hand
    rhas = False  # right has currently checked hand
    # check for highest hand first, flush
    lval = check_royal_flush(left1, left2, left3)
    rval = check_royal_flush(right1, right2, right3)
    if lval == 14:  # if left has a flush
        lhas = True
    if rval == 14:  # else if right has a flush
        rhas = True
    # Compare flush statuses
    if lhas and rhas:  # if both, draw
        return 0
    elif lhas:  # else if only left, left wins
        return -1
    elif rhas:  # else if only right, right wins
        return 1
    # Check for next highest hand, straight
    lval = check_straight(left1, left2, left3)
    rval = check_straight(right1, right2, right3)
    if lval > 0:
        lhas = True  # if either have non-zero val, they have straight
    if rval > 0:
        rhas = True
    # Compare straight statuses
    if lhas and rhas:  # if both straights
        if lval > rval:  # if left is of higher value, left wins
            return -1
        elif lval == rval:  # else if matching, draw
            return 0
        else:  # else right is bigger, right wins
            return 1
    elif lhas:  # else if only left has straight, left wins
        return -1
    elif rhas:  # else if only right has straight, right wins
        return 1
    # Check for next hand, three of a kind
    lval = check_3ofa_kind(left1, left2, left3)
    rval = check_3ofa_kind(right1, right2, right3)
    if lval > 0:
        lhas = True
    if rval > 0:
        rhas = True
    # Compare three of a kind statuses
    if lhas and rhas:  # if both have three of a kind
        if lval == rval: # if both have same value, draw
            return 0
        elif lval > rval:  # if left has higher value, left wins
            return -1
        else:  # else right has higher value, right wins
            return 1
    elif lhas:  # else if only left has three, left wins
        return -1
    elif rhas:  # else if only right has three, right wins
        return 1
    else:  # else all other cases are draw
        return 0

print(play_cards('S2', 'S3', 'S4','S5', 'S6', 'S7'))
