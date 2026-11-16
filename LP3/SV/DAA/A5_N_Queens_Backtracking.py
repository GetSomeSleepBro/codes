def is_safe(board, row, col, n):
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1 and (i != row or j != col):
                if i == row or j == col or abs(i - row) == abs(j - col):
                    return False
    return True


def solve_queens(board, col, fixed_col, n):
    if col == n:
        return True

    if col == fixed_col:
        return solve_queens(board, col + 1, fixed_col, n)

    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1

            if solve_queens(board, col + 1, fixed_col, n):
                return True

            board[row][col] = 0

    return False


def main():
    n = int(input("Enter the value of n: "))

    if n <= 0:
        print("Board size must be greater than zero.")
        return

    if n == 2 or n == 3:
        print("No solution exists for n =", n)
        return

    row = int(input("Enter row of first queen (1 to n): ")) - 1
    col = int(input("Enter column of first queen (1 to n): ")) - 1

    if row < 0 or row >= n or col < 0 or col >= n:
        print("Enter a row and column between 1 and", n)
        return

    board = [[0 for j in range(n)] for i in range(n)]
    board[row][col] = 1

    if solve_queens(board, 0, col, n):
        print("\nSolution:")
        for i in range(n):
            print(" ".join("Q" if board[i][j] == 1 else "." for j in range(n)))
    else:
        print("No solution is possible for this first queen position.")


if __name__ == "__main__":
    main()


# SAMPLE OUTPUT:
# Enter the value of n: 8
# Enter row of first queen (1 to n): 1
# Enter column of first queen (1 to n): 1
#
# Solution:
# Q . . . . . . .
# . . . . . . Q .
# . . . . Q . . .
# . . . . . . . Q
# . Q . . . . . .
# . . . Q . . . .
# . . . . . Q . .
# . . Q . . . . .
