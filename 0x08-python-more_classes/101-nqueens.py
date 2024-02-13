import sys

def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at the given position.

    Parameters:
        board (list): A list representing the current state of the board.
        row (int): The row index to check.
        col (int): The column index to check.
        n (int): The size of the board (number of rows/columns).

    Returns:
        bool: True if it's safe to place a queen at the given position, False otherwise.
    """
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_nqueens_util(board, row, n, solutions):
    """
    Recursively solve the N-queens problem and store the solutions.

    Parameters:
        board (list): A list representing the current state of the board.
        row (int): The current row being considered.
        n (int): The size of the board (number of rows/columns).
        solutions (list): A list to store the solutions.

    Returns:
        None
    """
    if row == n:
        queens_positions = []
        for r in range(n):
            for c in range(n):
                if board[r][c] == 1:
                    queens_positions.append([r, c])
        solutions.append(queens_positions)
        return
    
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_nqueens_util(board, row + 1, n, solutions)
            board[row][col] = 0

def solve_nqueens(n):
    """
    Solve the N-queens problem and print the solutions.

    Parameters:
        n (int): The size of the board (number of rows/columns).

    Returns:
        None
    """
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens_util(board, 0, n, solutions)
    for sol in solutions:
        print(sol)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(N)
