
from logic import Initialize_board, display_board, checkforwin, checkfortie, get_available_moves
from minimax_algorithm import find_best_move


def run_game():
 #main function to run the game
 
    #human plays first
    board = Initialize_board()
    current_player = 'x'

    print("Welcome to    Minimax AI!")
    print("You are 'x', the AI is 'o'")
    print("The board positions are   numbered 0 to 8 .")
    
    # empty boards with positions as a reference
    ref_board = [str(i) for i in range(9)]
    display_board(ref_board)
    print("Game starting...\n")
    
    game_over = False
    
    while not game_over:
        display_board(board)

        if current_player == 'x':
            while True:
                try:

                    move = int(input(f"Player {current_player}, enter your move (0-8): "))
                    if move in get_available_moves(board):
                        board[move] = 'x'
                        break


                    else:
                        print("Invalid move.")
                except ValueError:
                    print("Invalid input. Please enter a number between 0 and 8.")
            
            if checkforwin(board, 'x'):
                print("\n\n** GAME OVER ")
                display_board(board)
                print(" You won")
                game_over = True
            elif checkfortie(board):
                print("\n\n*** GAME OVER *")
                display_board(board)
                print("Its a Tie")
                game_over = True
            else:
                current_player = 'o'

        elif current_player == 'o':
            #ai plays now
            print("ai is calculating its move (o)")
            ai_move     = find_best_move(board)
            if ai_move    != -1:
                board[ai_move] = 'o'
            
            if checkforwin(board, 'o'):
                print("\n\n* GAME OVER ")
                display_board(board)
                print("AI   wins! Better luck next time.")
                game_over = True
            
            current_player = 'x'


if __name__ ==    "__main   __":
    pass
run_game()
