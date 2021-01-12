# ---- Global Variables ----

# Initilize game board
board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_"]

# If game is still going
game_status_active= True

# Initize winner
winner = None

# Initialize current player
current_player = "X"

# Play tic-tac-toe
def play_game():

    # Display initial board
    display_board()

    # While the game is still going
    while game_status_active:

        # Handle a single input of an arbitrary player
        handle_input(current_player)
    
        # check if the game has ended
        check_if_game_over()

        # Flop to the other player
        flip_player()

    # The game ended. Print result.
    if winner:
        print(winner + " won.")
    elif winner == None:
        print("It's a tie.")

# Display board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

# Handle a single turn of an arbitrary player
def handle_input(player):
    # Let the players know whose turn it is
    print(player + "'s turn.")

    # Contiuosly get user's input
    while(True):
        position = input("Choose a position from 1-9: ")
        # If input is valid, fill the board move on. 
        try:
            position = int(position) -1
            if board[position] == "_":
                board[position] = player
                break
            else:
                print("This position is taken. Please choose another number. ")
        except: 
            print("Not a valid input.")
            continue

    # Update board
    display_board()

# Flip player
def flip_player():
    # Set up global variable
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

# Check if the game is over.
def check_if_game_over():
    # Check if the game has a winner.
    check_for_winner()
    # Check if the game is a tie.
    check_if_tie()

# Check for a winner
def check_for_winner():

    # Set up global variables
    global winner

    # Check rows
    row_winner = check_rows()
    # Check columns
    column_winner = check_columns()
    # Check diagonal
    diagonal_winner = check_diagonals()
    
    # Get the winner 
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return

# Check if the game is tie.
def check_if_tie():
    global game_status_active
    if "_" not in board:
        # Stop game
        game_status_active = False
    return

# Check each row for winning pattern.
def check_rows():
    # Set up global variables
    global game_status_active
    # Check if any of the rows have all the value (and is not empty)
    row_1 = board[0] == board[1] == board[2] != "_"
    row_2 = board[3] == board[4] == board[5] != "_"
    row_3 = board[6] == board[7] == board[8] != "_"
    if row_1 | row_2 | row_3:
        # Stop game
        game_status_active = False
    # Return the winner
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3: 
        return board[6]
    return
    
# Check each column for winning pattern.
def check_columns():
    # Set up global variables
    global game_status_active
    # Check if any of the columns have all the value (and is not empty)
    column_1 = board[0] == board[3] == board[6] != "_"
    column_2 = board[1] == board[4] == board[7] != "_"
    column_3 = board[2] == board[5] == board[8] != "_"
    if column_1 | column_2 | column_3:
        game_status_active = False
    # Return the winner
    if column_1:
        return board[0]
    if column_2:
        return board[1]
    if column_3: 
        return board[2]
    return

# Check diagonal winning pattern.
def check_diagonals():
    # Set up global variables
    global game_status_active
    # Check if any of the diagonals have all the value (and is not empty)
    diagonal_1 = board[0] == board[4] == board[8] != "_"
    diagonal_2 = board[6] == board[4] == board[2] != "_"
    if diagonal_1 | diagonal_2:
        game_status_active = False
    # Return the winner
    if diagonal_1:
        return board[0]
    if diagonal_2:
        return board[6]
    return

play_game()
