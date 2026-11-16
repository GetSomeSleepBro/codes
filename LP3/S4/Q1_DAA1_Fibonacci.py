# ============================================================
# A(1) Write a recursive and non-recursive program to calculate
# Fibonacci numbers and analyze their time and space complexity.
# ============================================================

import time


# Recursive Fibonacci
def recursive_fib(n):
    if n <= 1:
        return n
    return recursive_fib(n - 1) + recursive_fib(n - 2)


# Non-Recursive Fibonacci
def iterative_fib(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b


# Main Program
n = int(input("Enter number of terms: "))

if n <= 0:
    print("Please enter a positive number.")
else:
    print("\nRecursive Fibonacci:")
    start = time.perf_counter()

    for i in range(n):
        print(recursive_fib(i), end=" ")

    recursive_time = time.perf_counter() - start
    print(f"\nExecution Time: {recursive_time:.6f} seconds")

    print("\nNon-Recursive Fibonacci:")
    start = time.perf_counter()

    iterative_fib(n)

    iterative_time = time.perf_counter() - start
    print(f"\nExecution Time: {iterative_time:.6f} seconds")

    print("\nComplexity Analysis:")
    print("Recursive     : Time O(2^n), Space O(n)")
    print("Non-Recursive : Time O(n),   Space O(1)")


# ============================================================
# SAMPLE OUTPUT
# ============================================================
#
# Enter number of terms: 7
#
# Recursive Fibonacci:
# 0 1 1 2 3 5 8
# Execution Time: 0.000020 seconds
#
# Non-Recursive Fibonacci:
# 0 1 1 2 3 5 8
# Execution Time: 0.000010 seconds
#
# Complexity Analysis:
# Recursive     : Time O(2^n), Space O(n)
# Non-Recursive : Time O(n),   Space O(1)
#
# Note: Actual execution times vary between runs.


# ============================================================
# ------------------------------------------------------------
# THEORY AND VIVA QUESTIONS & ANSWERS
# ------------------------------------------------------------
# ============================================================

# THEORY:
#
# Fibonacci series is a sequence in which each number
# is the sum of the previous two numbers.
#
# Series : 0, 1, 1, 2, 3, 5, 8, 13, ...
# Formula: F(n) = F(n-1) + F(n-2)
# Base   : F(0) = 0, F(1) = 1
#
# Recursive Method:
# - A function calls itself to calculate Fibonacci numbers.
# - Time Complexity  : O(2^n) - Exponential upper bound
# - Space Complexity : O(n)   - Recursive call stack
#
# Non-Recursive Method:
# - Uses a loop and two variables to generate the series.
# - Time Complexity  : O(n) - Linear
# - Space Complexity : O(1) - Constant auxiliary space


# Q1. What is recursion?
# Ans: Recursion is a technique where a function calls
# itself until a base condition is reached.


# Q2. What is the difference between recursive and iterative?
# Ans: Recursive uses repeated function calls, while
# iterative uses loops to solve the same problem.


# Q3. Which method is more efficient and why?
# Ans: Iterative is more efficient because it calculates
# each value once and avoids repeated function calls.


# Q4. What is time complexity?
# Ans: Time complexity describes how an algorithm's
# running time grows as the input size increases.
# It is commonly represented using Big O notation.


# Q5. Why is recursive Fibonacci O(2^n)?
# Ans: Each non-base call creates two more recursive
# calls, causing many repeated calculations.
# The number of calls grows exponentially.
# O(2^n) is an upper bound.


# Q6. Why is iterative Fibonacci O(n)?
# Ans: It uses a single loop that executes n times.
# Therefore, its running time grows linearly.


# Q7. What is space complexity?
# Ans: Space complexity describes how memory usage
# grows with the input size, including variables,
# temporary storage and function call stacks.


# Q8. Why does recursive Fibonacci use O(n) space?
# Ans: Recursive calls are stored on the call stack.
# The maximum recursion depth is proportional to n.


# Q9. Why does iterative Fibonacci use O(1) space?
# Ans: It uses only two variables (a and b), regardless
# of input size. Therefore, auxiliary memory is constant.


# Q10. What is the purpose of the base condition?
# Ans: It stops recursion at n = 0 or n = 1.
# Without it, recursive calls would not terminate.


# Q11. What is Big O notation?
# Ans: Big O represents an upper bound on how an
# algorithm's time or space requirements grow.
# Example: O(1), O(n), O(n^2), O(2^n).


# Q12. Why do we use time.perf_counter()?
# Ans: It provides a high-resolution timer to measure
# elapsed execution time in seconds.
# Elapsed time = End time - Start time.


# Q13. Why can execution times vary?
# Ans: Execution time depends on CPU speed, system load,
# input size and other running processes.
# Our measurement also includes printing the series.


# Q14. What happens when the input size increases?
# Ans: Recursive execution becomes much slower because
# repeated calculations increase exponentially.
# Iterative execution grows approximately linearly.


# Q15. What is a recursion stack?
# Ans: It is memory used to store active function calls,
# their local variables and return information.


# Q16. Which approach should be preferred for large n?
# Ans: Iterative, because it is faster, uses less memory
# and avoids Python's recursion-depth limit.


# Q17. What are the types of complexity analysis?
# Ans: Best Case    - Minimum resources required.
#      Average Case - Expected resources required.
#      Worst Case   - Maximum resources required.
# Both Fibonacci implementations have predictable
# work for a given n, regardless of the input values.


# ============================================================
# CONCLUSION
# ============================================================
#
# Both methods generate the same Fibonacci series.
# Recursive Fibonacci is simple but performs repeated
# calculations and uses additional stack memory.
#
# The iterative method is more efficient because it
# takes O(n) time and O(1) auxiliary space.
# ============================================================
