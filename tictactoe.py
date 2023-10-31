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

    actions = {}
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
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
