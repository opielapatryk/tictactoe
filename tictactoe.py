"""
Tic Tac Toe Player
"""

import math, copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countNone = 0

    for row in board:
        countNone += row.count(EMPTY)

    if countNone % 2 == 0:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i, j))
    return actions



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i = action[0]
    j = action[1]
    if board[i][j] == EMPTY:
        newBoardState = copy.deepcopy(board)
        newBoardState[i][j] = player(board)
        return newBoardState
    else:
        raise ValueError("Action not available")
    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winner = None
    for row in board:
        if all(cell == X for cell in row):
            winner = X
        elif all(cell == O for cell in row):
            winner = O
        
    for col in range(3):
        if all(board[row][col] == X for row in range(3)):
            winner = X
        elif all(board[row][col] == O for row in range(3)):
            winner = O
        
    if all(board[i][i] == X for i in range(3)) or all(board[i][2 - i] == X for i in range(3)):
        winner = X
    elif all(board[i][i] == O for i in range(3)) or all(board[i][2 - i] == O for i in range(3)):
        winner = O

    return winner
    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None or EMPTY not in [cell for row in board for cell in row]:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1 
        else:
            return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.

    The minimax function should take a board as input, and return the optimal move for the player to move on that board.

    - The move returned should be the optimal action (i, j) that is one of the allowable actions on the board. If multiple moves are equally optimal, any of those moves is acceptable.
    - If the board is a terminal board, the minimax function should return None.

    For all functions that accept a board as input, you may assume that it is a valid board (namely, that it is a list that contains three rows, each with three values of either X, O, or EMPTY). You should not modify the function declarations (the order or number of arguments to each function) provided.

    Once all functions are implemented correctly, you should be able to run python runner.py and play against your AI. And, since Tic-Tac-Toe is a tie given optimal play by both sides, you should never be able to beat the AI (though if you don’t play optimally as well, it may beat you!)

    Alpha-beta pruning is optional, but may make your AI run more efficiently!

    """
    # returned move should be the optimal action (i, j)
    # if the board is a terminal board the minimax function should return None
    if terminal(board):
        return None
    
    availableActions = actions(board)
    return availableActions[0]