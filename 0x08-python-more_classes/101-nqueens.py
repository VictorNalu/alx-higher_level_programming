#!/usr/bin/python3

"""Solves the N-queens puzzle."""

import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at the given position.

    Parameters:
        board (list): A list representing the current state of the board.
        row (int): The row index to check.
        col (int): The column index to check.

    Returns:
        bool: True if it's safe to place a queen at the given position,
        False otherwise.
    """
    # Check if there is a queen in the same column or diagonals
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True


def solve_nqueens(board, row, n):
    """
    Recursively solve the N-queens problem and print the solutions.

    Parameters:
        board (list): A list representing the current state of the board.
        row (int): The current row being considered.
        n (int): The size of the board (number of rows/columns).

    Returns:
        None
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
    Solve the N-queens problem and print the solutions.

    Parameters:
        n (str): The size of the board (number of rows/columns).

    Returns:
        None
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
