#-------Global Variables -------------


board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

#If game is still going
game_still_going = True

#who won? or tie?
winner = None

#whos turn is it
current_player = "X"

# Display board
def display_board():
    print(board[0] +  " | " + board[1] + " | " + board[2])
    print(board[3] +  " | " + board[4] + " | " + board[5])
    print(board[6] +  " | " + board[7] + " | " + board[8])
 
# Play game of tic-tac-toe  
def play_game():
    
    # Display initial board
    display_board()
    
    # While the game is still going
    while game_still_going:
        
        #handle a signle turn of an arbituary player 
        handle_turn(current_player)
        
        #Check if the game has ended
        check_if_game_over()
        
        # Flip to the other player 
        flip_player()
        
    # The game has ended 
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")
        

#handle turn of a arbituary player
def handle_turn(player):  
    position = input("Choose a position from 1-9: ")
    position = int(position) - 1
    
    board[position] = "X"
    
    display_board()
  
  
def check_if_game_over():
    check_for_winner()
    check_if_tie()
    
def check_for_winner():
    
    #set up global variables
    global winner
    
    #check rows
    row_winner = check_rows()
    #check columns
    coloumn_winner = check_coloumns()
    #check diagonals 
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner()
    elif column_winner:
        winner = coloumn_winner()
    elif diagonal_winner:
        winner = diagonal_winner()
    else:
        winner = None
    return
    
def check_rows():
    #setup global variables
    global game_still_going
    #check if any of the rows have the ame value
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    #If any row does have amtch, flash as win
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
       return board[0]
    elif row_2:
       return board[3]
    elif row_3:
        return board[6]
    return

def check_coloumns():
    return

def check_diagonals():
    return

def check_if_tie():
    #check rows
    #check columns
    #check diagonals 
    return
    
def flip_player():  
    return
    
    
play_game()


#0.26S









#board
#display
#play game
#handle turn
#check win
    #check rows
    #check columns
    #check diagonals
#check tie
#flip player
