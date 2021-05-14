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
 
# Play game   
def play_game():
    
    # Display initial board
    display_board()
    
    # While the game is still ongoing
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
        

#handle turn 
def handle_turn(player):  
    position = input("Choose a position from 1-9: ")
    position = int(position) - 1
    
    board[position] = "X"
    
    display_board()
  
  
def check_if_game_over():
    check_if_win()
    check_if_tie()
    
def check_if_win():
    #check rows
    #check colums
    #check diagonals 
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
