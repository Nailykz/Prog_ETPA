import sys

def game ():
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    while True:
        turn (board)
        
def turn (board):
    play ("X", board)
    play ("O", board)


def play (player, board):
    print_board (board)
    check_for_tie (board)
    print ("C'est au tour du joueur " + player + ".")
    print ("Ligne? (0, 1 ou 2)")
    line = int (input ())
    print ("Colonne? (0, 1 ou 2)")
    column = int (input ())
    if board[line][column] == " ":
        board[line][column] = player
        check_if_game_is_won (player, board)
    else:
        invalid_choice ()
        
def print_board (board):
    print ("-------")
    for i in range (0, 3):
        for j in range (0, 3):
            print ("|" + board[i][j], end="")
        print ("|")
        print ("-------")

def check_if_game_is_won (player, board):
    check_alignments (player, lines (board) + columns (board) + diagonals (board))

def check_alignment_for (player, line):
    if line == player * 3:
        game_is_over (player)

def check_alignments (player, candidates):
    for i in range (0, len (candidates)):
        check_alignment_for (player, candidates[i])

def columns (board):
    tboard = [[]] * 3
    for i in range (0, 3):
        tboard[i] = [" "] * 3
    for i in range (0, 3):
        for j in range (0, 3):
            tboard[j][i] = board[i][j]
    return tboard

def lines (board):
    return (board)
    
def diagonals (board):
    return [
        [ board[0][0], board[1][1], board[2][2] ],
        [ board[2][0], board[1][1], board[0][2] ]
    ]

def count_empty_cells (board):
    c = 0
    for i in range (0, 3):
        for j in range (0, 3):
            if board[i][j] == " ":
                c = c + 1
    return c

def check_for_tie (board):
    if count_empty_cells (board) == 0:
        print ("Egalite!")
        sys.exit (0)

def invalid_choice ():
    print ("Coup invalide!")
    sys.exit (0)

def game_is_over (player, board):
    print (player + " a gagne!")
    print_board (board)
    sys.exit (0)

game ()
print_board (board)