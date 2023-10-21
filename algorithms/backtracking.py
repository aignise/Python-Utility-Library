def solve_sudoku(board):
    """
    Try to fill the board following the rules of Sudoku.
    """
    empty = find_empty_location(board)
    
    # If there's no empty location, the board is solved
    if not empty:
        return True
    
    row, col = empty

    for num in range(1, 10):
        if is_safe(board, row, col, num):
            
            # Place the number
            board[row][col] = num
            
            # Continue with this placement and see if it leads to a solution
            if solve_sudoku(board):
                return True
            
            # If placing num didn't lead to a solution, reset the cell and try the next number
            board[row][col] = 0

    # If no number can be placed in the current cell, backtrack to the previous cell
    return False

def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def is_safe(board, row, col, num):
    # Check if 'num' is not in the current row and column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check 3x3 square
    startRow, startCol = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + startRow][j + startCol] == num:
                return False

    return True
