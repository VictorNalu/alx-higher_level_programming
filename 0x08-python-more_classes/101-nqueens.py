#!/usr/bin/python3
"""solves the N queens problem"""

import sys


def is_safe(board, row, col):
    """Checks if it's safe to place the queen at a given position"""

    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(board, row, n):
    """
    Recursively solve the N-queens problem and print the solutions.
    """

    if row == n:
        print([[i, board[i]] for i in range(n)])
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, n)


def nqueens(n):
    """
    solves the N queens problem
    """

    try:
        n = int(n)
        if n < 4:
            raise ValueError
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    board = [-1] * n
    solve_nqueens(board, 0, n)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    nqueens(sys.argv[1])
