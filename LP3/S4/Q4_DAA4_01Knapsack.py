# ============================================================
# A(4) Write a program to solve a 0-1 Knapsack problem
# using Dynamic Programming or Branch and Bound strategy.
# ============================================================

def knapsack(W, wt, val, n):

    # Create DP table
    dp = [[0 for i in range(W + 1)] for j in range(n + 1)]

    # Fill DP table
    for i in range(1, n + 1):
        for w in range(W + 1):

            if wt[i-1] <= w:
                dp[i][w] = max(
                    val[i-1] + dp[i-1][w-wt[i-1]],
                    dp[i-1][w]
                )
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][W]


# Main Program
n = int(input("Enter number of items: "))

val = list(map(int, input("Enter values (separated by space): ").split()))
wt = list(map(int, input("Enter weights (separated by space): ").split()))

W = int(input("Enter knapsack capacity: "))

if (n <= 0 or len(val) != n or len(wt) != n
        or any(w <= 0 for w in wt)
        or any(v < 0 for v in val) or W < 0):
    print("Invalid input!")
else:
    print("Maximum value =", knapsack(W, wt, val, n))


# ============================================================
# SAMPLE OUTPUT
# ============================================================
#
# Enter number of items: 3
# Enter values: 60 100 120
# Enter weights: 10 20 30
# Enter knapsack capacity: 50
# Maximum value = 220
#
# Explanation:
# Item 2: Value 100, Weight 20
# Item 3: Value 120, Weight 30
# Total : Value 220, Weight 50


# ============================================================
# ------------------------------------------------------------
# THEORY AND VIVA QUESTIONS & ANSWERS
# ------------------------------------------------------------
# ============================================================

# THEORY:
#
# 0-1 Knapsack is an optimization problem in which
# items are selected to maximize total profit without
# exceeding the knapsack capacity.
#
# Each item can either be selected (1) or rejected (0).
# Items cannot be divided into fractions.
#
# DYNAMIC PROGRAMMING (DP):
# DP divides a problem into smaller overlapping
# subproblems and stores their results in a table.
#
# ALGORITHM:
# 1. Accept item values, weights and capacity.
# 2. Create a DP table of size (n+1) x (W+1).
# 3. Initialize the table with zeros.
# 4. For each item, check whether it fits.
# 5. If it fits, choose maximum of:
#    - Including the item
#    - Excluding the item
# 6. Otherwise, exclude the item.
# 7. Return dp[n][W] as the maximum value.
#
# FORMULA:
# If wt[i-1] <= w:
# dp[i][w] = max(
#     val[i-1] + dp[i-1][w-wt[i-1]],
#     dp[i-1][w]
# )
#
# Otherwise:
# dp[i][w] = dp[i-1][w]
#
# COMPLEXITY:
# n = Number of items
# W = Knapsack capacity
#
# Time Complexity  : O(n * W)
# Space Complexity : O(n * W)
#
# Both depend on the number of items and capacity.


# Q1. What is the 0-1 Knapsack problem?
# Ans: An optimization problem where items are either
# completely selected or rejected to maximize profit.


# Q2. What is Dynamic Programming?
# Ans: A technique that stores solutions of smaller
# subproblems to avoid repeated calculations.


# Q3. Why do we use Dynamic Programming?
# Ans: To solve overlapping subproblems efficiently
# and obtain the optimal solution.


# Q4. What is the difference between 0-1 and
# Fractional Knapsack?
# Ans: 0-1 Knapsack allows only complete items.
# Fractional Knapsack allows dividing items.


# Q5. Why doesn't Greedy always work for 0-1 Knapsack?
# Ans: Choosing the highest value/weight ratio first
# may not give the maximum total profit.


# Q6. What is the time complexity?
# Ans: O(n * W), because the algorithm fills a
# table having approximately n * W cells.


# Q7. What is the space complexity?
# Ans: O(n * W), because a 2D DP table is stored
# in memory.


# Q8. What is a DP table?
# Ans: A table that stores solutions of smaller
# subproblems to avoid recalculating them.


# Q9. What does dp[i][w] represent?
# Ans: Maximum profit using the first i items
# with knapsack capacity w.


# Q10. Why do we use max()?
# Ans: To select the better option between
# including and excluding an item.


# Q11. Why do we initialize the table with zeros?
# Ans: With zero items or zero capacity,
# the maximum possible profit is zero.


# Q12. What happens if an item exceeds capacity?
# Ans: The item is excluded, and the previous
# maximum profit is carried forward.


# Q13. What are overlapping subproblems?
# Ans: Smaller problems that occur repeatedly.
# DP stores their results to avoid recalculation.


# Q14. What is optimal substructure?
# Ans: A property where the optimal solution
# can be formed using optimal subproblem solutions.


# Q15. What is Branch and Bound?
# Ans: An optimization technique that explores
# possible solutions and eliminates branches
# that cannot improve the best solution.


# Q16. Difference between DP and Branch and Bound?
# Ans: DP stores subproblem results in a table.
# Branch and Bound uses bounds to prune unnecessary
# branches while searching for the best solution.


# Q17. What is the disadvantage of DP?
# Ans: Large capacity values require more time
# and memory. O(n * W) is pseudo-polynomial.


# Q18. Why is the answer 220 in our example?
# Ans: We select items 2 and 3:
# Value = 100 + 120 = 220
# Weight = 20 + 30 = 50
# This gives the maximum profit within capacity.


# Q19. Where is 0-1 Knapsack used?
# Ans: Budget allocation, cargo loading,
# project selection and resource optimization.


# Q20. Which approach is used in our program?
# Ans: Dynamic Programming using tabulation.
# It stores results in a 2D table using loops.


# ============================================================
# CONCLUSION
# ============================================================
#
# The 0-1 Knapsack problem is solved using Dynamic
# Programming to maximize profit within capacity.
#
# Time Complexity : O(n * W)
# Space Complexity: O(n * W)
# ============================================================
