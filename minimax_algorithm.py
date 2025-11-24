
from logic import checkforwin, checkfortie, get_available_moves


scores = {'o': 10, 'x': -10, 'tie': 0}


def minimax(board, depth, already_maximizing):
    if checkforwin(board, "o"):
        return scores["o"] - depth

    if checkforwin(board, 'x'):
        return scores['x'] + depth

    if checkfortie(board):
        return scores["tie"]

    if already_maximizing:
        best_score = -float('inf')
        for move in get_available_moves(board):
            board[move] = 'o'
            current_score = minimax(board, depth + 1, False)
            board[move] = ' '
            best_score = max(best_score, current_score)
        return best_score
    else:
        best_score = float('inf')
        for move in get_available_moves(board):
            board[move] = 'x'
            current_score = minimax(board, depth + 1, True)
            board[move] = ' '
            best_score = min(best_score, current_score)
        return best_score


def find_best_move(board):
    best_score = -float('inf')
    best_move = -1

    for move in get_available_moves(board):
        board[move] = 'o'
        current_score = minimax(board, 0, False)
        board[move] = ' '

        if current_score > best_score:
            best_score = current_score
            best_move = move

    return best_move


