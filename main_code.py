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
   
    print(player + "'S turn.") 
    position = input("Choose a position from 1-9: ")
    
    valid = False
    while not valid:
    
        while position not in ["1", "2", "3","4","5","6","7","8","9"]:
            position = input("Choose a position from 1-9: ")
    
        position = int(position) - 1
    
        if board[position] == "-":
            valid = True
        else:
         print("You cant go there. Go again.")
    

    board[position] = player
    
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
        winner = row_winner
    elif coloumn_winner:
        winner = coloumn_winner
    elif diagonal_winner:
        winner = diagonal_winner
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
        # Return the WInner (X or ) )
    if row_1:
       return board[0]
    elif row_2:
       return board[3]
    elif row_3:
        return board[6]
    return

def check_coloumns():
        #setup global variables
    global game_still_going
    #check if any of the coloumns have the ame value
    coloumn_1 = board[0] == board[3] == board[6] != "-"
    coloumn_2 = board[1] == board[4] == board[7] != "-"
    coloumn_3 = board[2] == board[5] == board[8] != "-"
    #If any coloumns does have amtch, flash as win
    if coloumn_1 or coloumn_2 or coloumn_3:
        game_still_going = False
        # Return the WInner (X or ) )
    if coloumn_1:
       return board[0]
    elif coloumn_2:
       return board[1]
    elif coloumn_3:
        return board[2]
    return


def check_diagonals():
        #check if any of the diagonals have the ame value
    diagonals_1 = board[0] == board[4] == board[8] != "-"
    diagonals_2 = board[6] == board[4] == board[2] != "-"
    #If any diagonals does have a match, flash as win
    if diagonals_1 or diagonals_2 :
        game_still_going = False
        # Return the WInner (X or ) 
    if diagonals_1:
       return board[0]
    elif diagonals_2:
       return board[6]
   
    return

def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return
    
def flip_player():  
    #global variables needed
    global current_player
    #if the current player was x, then change it to 0
    if current_player =="X":
     current_player = "0"
    #If the current player was ), then change it to X
    elif current_player == "0":
     current_player = "X"
    return
    
    
play_game()


#0.40









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
# testing my strength  