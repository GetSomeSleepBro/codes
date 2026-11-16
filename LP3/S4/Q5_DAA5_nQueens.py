# ============================================================
# A(5) Design n-Queens matrix having first Queen placed.
# Use backtracking to place remaining Queens to generate
# the final n-Queens matrix.
# ============================================================

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


# Main Program
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


# ============================================================
# SAMPLE OUTPUT
# ============================================================
#
# Enter N: 5
#
# Final N-Queens Matrix:
# [1, 0, 0, 0, 0]
# [0, 0, 1, 0, 0]
# [0, 0, 0, 0, 1]
# [0, 1, 0, 0, 0]
# [0, 0, 0, 1, 0]
#
# Note: For N=4, no solution exists with the first
# queen fixed at (0, 0). Try N=5.


# ============================================================
# ------------------------------------------------------------
# THEORY AND VIVA QUESTIONS & ANSWERS
# ------------------------------------------------------------
# ============================================================

# THEORY:
#
# N-Queens is a backtracking problem where N queens
# must be placed on an N x N chessboard so that
# no two queens attack each other.
#
# A queen can attack horizontally, vertically
# and diagonally.
#
# Here, the first queen is fixed at (0, 0).
# Remaining queens are placed using backtracking.
#
# BACKTRACKING:
# Backtracking tries possible solutions one by one.
# If a placement leads to failure, it removes the
# queen and tries another position.
#
# ALGORITHM:
# 1. Create an N x N matrix filled with zeros.
# 2. Place the first queen at (0, 0).
# 3. Start placing queens from the second row.
# 4. Check column and diagonal safety.
# 5. If safe, place the queen.
# 6. Recursively try the next row.
# 7. If unsuccessful, remove queen (backtrack).
# 8. Repeat until all queens are placed.
#
# COMPLEXITY:
# Time Complexity  : O(N! * N^2) worst-case upper bound
# Space Complexity : O(N^2)
#
# The backtracking search is commonly described as
# O(N!), with extra safety-check work in this code.
# The board uses N x N memory, and recursion uses O(N).


# Q1. What is the N-Queens problem?
# Ans: Placing N queens on an N x N chessboard
# so that no two queens attack each other.


# Q2. What is Backtracking?
# Ans: A technique that tries possible solutions
# and reverses decisions when they lead to failure.


# Q3. Why do we use Backtracking?
# Ans: To avoid exploring further positions when
# the current queen placement is invalid.


# Q4. What is the condition for placing a queen?
# Ans: No other queen must be present in the
# same row, column or diagonal.


# Q5. Why do we check only previous rows?
# Ans: Queens are placed row by row, so future
# rows are still empty.


# Q6. Why don't we check the same row?
# Ans: We place only one queen in each row.


# Q7. How do we check diagonal attacks?
# Ans: Two positions are on the same diagonal if:
# abs(row1-row2) == abs(col1-col2)


# Q8. What does safe() do?
# Ans: Checks whether a queen can be placed
# without attacking any previously placed queen.


# Q9. What does solve() do?
# Ans: Recursively places queens and uses
# backtracking when no safe position is found.


# Q10. Why is board[row][col] = 0 used?
# Ans: To remove a queen when its placement
# cannot lead to a complete solution.


# Q11. What is the base condition?
# Ans: When row == n, all N queens have been
# successfully placed.


# Q12. What is the time complexity?
# Ans: Backtracking may explore factorially many
# placements. This implementation also scans the
# board for safety, giving O(N! * N^2) upper bound.


# Q13. What is the space complexity?
# Ans: O(N^2) for the chessboard matrix.
# Recursion additionally uses O(N) stack space.


# Q14. What do 0 and 1 represent?
# Ans: 0 represents an empty position.
# 1 represents a queen.


# Q15. Why is the first queen fixed?
# Ans: Because the question specifies that the
# first queen must already be placed.


# Q16. Why can N=4 give "No solution"?
# Ans: N=4 has solutions, but none when the
# first queen is fixed at position (0, 0).


# Q17. Does N-Queens have multiple solutions?
# Ans: Yes, depending on N and the fixed queen.
# This program stops after finding one solution.


# Q18. Difference between Greedy and Backtracking?
# Ans: Greedy chooses the locally best option.
# Backtracking tries options and reverses choices
# when they fail.


# Q19. Is Backtracking recursive?
# Ans: It is commonly implemented recursively.
# Each recursive call handles the next row.


# Q20. What is a state space tree?
# Ans: A tree representing possible decisions.
# Each branch represents a queen placement.


# ============================================================
# CONCLUSION
# ============================================================
#
# The N-Queens problem is solved using Backtracking.
# The first queen remains fixed, while remaining
# queens are placed without attacking each other.
# ============================================================
