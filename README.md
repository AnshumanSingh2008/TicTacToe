Tic tac toe (based on Minimax algorithm)

Summary: This is a simple, command-line Tic-Tac-Toe game built in Python where the opponent is an Artificial Intelligence that will never lose. This project is a perfect introduction to how AI "thinks" using an algorithm called Minimax.

Installation & setup The project runs entirely in Python so it is very quick and easy .

1.1 Prerequisites
You only need python installed on your device 

1.2 Running the game 
1. Download the Files: Get all the code files from the project repository.
2. Open Your Terminal/Command Prompt: Navigate into the project folder using the cd .. command.
3. Run the Game !: Once inside the project folder, execute the main game file using this command:

 python main.py

The game will start, and you will be prompted to make your first move.

How to Play:

The game board is displayed in your terminal. It's a standard 3 x 3 grid.
You will be prompted to "enter your move (0-8)".
The board cells are numbered from 0 (top-left) to 8 (bottom-right)
Enter the number corresponding to the empty cell where you want to place your 'X'.
The AI will then make its move as 'O'.
The goal is simple: try to win, or at least force a draw! (The AI will make it very tough!)
How the AI Works This project isn't just a game; it's a demonstration of a powerful AI concept called the Minimax Algorithm.

The Problem: The AI's job is to figure out the absolute best move to make.
The Solution (Minimax): The AI looks ahead at every single possible move you and it could make until the game ends (a win, loss, or draw).
It Maximizes its own score (aiming for a win, which it scores as high).
It Minimizes your score (assuming you will always make the move that is worst for it).
The Result: Because it can see the end of every possible path, the AI will always choose the move that guarantees it will either win or at worst achieve a draw. It is unbeatable.
Project Structure The code is organized into three clean and easy-to-understand Python modules:

main.py ---------------->Game interface 
logic.py---------------->Game Logic 
minimax_algorithm.py---->Recursive Minimax Algorithm

Project Details:

Project Name: Unbeatable Tic-Tac-Toe AI
Algorithm: Minimax
Language: Python
Author: Anshuman Singh
Institution: VIT Bhopal
