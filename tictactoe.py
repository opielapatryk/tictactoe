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
        return O
    else:
        return X


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

    X win = 1 max player max(x) aims to max score
    None = 0
    O win = -1 min player min(o) aims to min score

    state = board 

    initial state = empty board

    player(board) = return which player will move in state board

    actions(board) = possible moves on board

    results(board,actions) = result after move a on state board

    terminal(board) = check if board is terminal (goal test)

    utility(board) = gives num value for terminal state / 1 if x win / 0 if none / -1 if O

    1. player(board) = X (board is empty so X starts)
    2. actions(board) = set((i,j),(i,j)....) # gives set of all possible moves
    3. results(board,actions) = newboard # return deepcopy of new updated board
    4. terminal(board) = True/ False # returns True if game is over or false if not 
    5. utility(board) = 1 # because X won the game... or -1 if O won the game or 0 if tie

    """

    if player(board) == X: # aim for 1 
        bestScore = float('-inf')
        for action in actions(board):
            newBestScore = minValue(result(board,action))
            if newBestScore > bestScore:
                bestScore = newBestScore
                bestMove = action
    elif player(board) == O: # aim for -1
        bestScore = float('inf')
        for action in actions(board):
            newBestScore = maxValue(result(board,action))
            if newBestScore < bestScore:
                bestScore = newBestScore
                bestMove = action

    return bestMove

def maxValue(board): 
    v = float('-inf')
    if terminal(board):
        return utility(board) 
    for action in actions(board):
        v = max(v,minValue(result(board,action)))
    return v

def minValue(board):
    v = float('inf')
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v,maxValue(result(board,action)))
    return v