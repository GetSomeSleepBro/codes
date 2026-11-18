# A(5) N-Queens with first queen fixed using backtracking

def safe(board, row, col, n):
    for i in range(row):
        for j in range(n):
            if board[i][j] == 1:
                if j == col or abs(i-row) == abs(j-col):
                    return False
    return True


def solve(board, row, n):
    if row == n:
        return True
    for col in range(n):
        if safe(board, row, col, n):
            board[row][col] = 1
            if solve(board, row+1, n):
                return True
            board[row][col] = 0  # Backtrack
    return False


n = int(input("Enter N: "))
if n <= 0:
    print("Enter a positive number.")
else:
    board = [[0]*n for i in range(n)]
    board[0][0] = 1  # First Queen fixed
    if solve(board, 1, n):
        print("\nFinal N-Queens Matrix:")
        for row in board:
            print(row)
    else:
        print("No solution")
