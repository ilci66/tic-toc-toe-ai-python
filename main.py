import random


# TODO: draw the board in the console
def draw_board(board):
    for i in range(0, 9, 3):
        print("|", board[i], "--", board[i+1], "--", board[i+2], "|")


# TODO: player chooses their letter, use input
def choose_letter():
    letter = ""
    while not (letter == "X" or letter == "O"):
        print("Pick your letter, X or O ?")
        letter = input().upper()

    if letter == "X":
        return ["X", "O"]
    elif letter == "O":
        return ["O", "X"]
    else:
        return False


# TODO: randomly decide who goes first
def who_goes_first():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


# TODO: ask if they wanna go again, use input
def play_again():
    print('Wanna play again ? y / n')
    return input().lower().startswith('y')


# TODO: place the letter on the board
def place_letter(board, letter, move):
    board[move] = letter


# TODO: check if the space on the board is empty
def is_free(board, space):
    return board[space] == ' '


# TODO: check if there is a winner
def is_win(board, letter):
    result = False

    # Check diagonal
    if board[0] == board[4] == board[8] == letter \
            or board[2] == board[4] == board[6] == letter:
        result = True

    # Check horizontal
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == letter:
            result = True

    # Check vertical
    for i in range(0, 3):
        if board[i] == board[i+3] == board[i+6] == letter:
            result = True

    return result


# TODO: copy the board and return the copy
def copy_board(board):
    copy = []
    for i in board:
        copy.append(i)
    return copy


# TODO: get the player move and register its legitimacy
def get_player_move(board):
    nums = '1 2 3 4 5 6 7 8 9'.split()
    move = ' '
    while move not in nums or not is_free(board, int(move)):
        print('What is your next move* (1-9)')
        move = input()
    return int(move)


# TODO: do a random move in a possible slot
def get_random_move_from_list(board, moves_list):
    moves = []
    for i in moves_list:
        if is_free(board, i):
            moves.append(i)
    if len(moves) != 0:
        return random.choice(moves)
    else:
        return None


# TODO: determine where to place the letter and return the letter
def get_computer_move(board, com_letter):
    player_letter = " "
    if com_letter == 'X':
        player_letter = 'O'
    else:
        player_letter = 'X'

    # TODO: check if there's a winner, return winner
    for i in range(9):
        copy = copy_board(board)
        if is_free(copy, i):
            place_letter(copy, com_letter, i)
            if is_win(copy, com_letter):
                return i

    # TODO: check if there is a corner free, return corner
    for i in range(9):
        copy = copy_board(board)
        if is_free(copy, i):
            place_letter(copy, player_letter, i)
            if is_win(copy, player_letter):
                return i

    # TODO: check if there is side free, return get_random_move_from_list
    move = get_random_move_from_list(board, [1, 3, 7, 9])
    if move is not None:
        return move

    if is_free(board, 5):
        return 5

    return get_random_move_from_list(board, [2, 4, 6, 8])


# TODO: check if the board is full
def is_board_full(board):
    for i in range(9):
        if is_free(board, i):
            return False
    return True


# TODO: start the game
def start_game():
    pass


if __name__ == '__main__':
    # print('Works !!!')
    draw_board('a b c d e f g h j'.split())
