def is_safe(row, col, board, n):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_n_queens(row, board, n):
    if row == n:
        print_solution(board)
        return True

    for col in range(n):
        if is_safe(row, col, board, n):
            board[row] = col
            if solve_n_queens(row + 1, board, n):
                return True
            board[row] = -1
    return False

def print_solution(board):
    for i in range(len(board)):
        row = ["Q" if board[i] == j else "." for j in range(len(board))]
        print(" ".join(row))
    print()

n = int(input("Enter the number of queens: "))
board = [-1] * n
if not solve_n_queens(0, board, n):
    print("No solution found.")
