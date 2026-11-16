# ============================================================
# DAA MINI PROJECT
# Write a program to implement matrix multiplication.
# Also implement multithreaded matrix multiplication using
# one thread per row or one thread per cell.
# Analyze and compare their performance.
# ============================================================

import threading
import time


# Normal Matrix Multiplication
def normal_multiply(A, B):
    n = len(A)
    C = [[0]*n for i in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    return C


# Function to multiply one row
def multiply_row(A, B, C, row):
    n = len(A)

    for j in range(n):
        for k in range(n):
            C[row][j] += A[row][k] * B[k][j]


# Multithreaded Matrix Multiplication
def threaded_multiply(A, B):
    n = len(A)
    C = [[0]*n for i in range(n)]
    threads = []

    for i in range(n):
        t = threading.Thread(target=multiply_row,
                             args=(A, B, C, i))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return C


# Main Program
n = int(input("Enter matrix size: "))

if n <= 0:
    print("Enter a positive matrix size.")
else:
    print("Enter first matrix:")
    A = [list(map(int, input().split())) for i in range(n)]

    print("Enter second matrix:")
    B = [list(map(int, input().split())) for i in range(n)]

    if any(len(row) != n for row in A + B):
        print("Invalid matrix! Enter exactly", n, "values per row.")
    else:
        # Normal Execution
        start = time.time()
        C1 = normal_multiply(A, B)
        normal_time = time.time() - start

        # Multithreaded Execution
        start = time.time()
        C2 = threaded_multiply(A, B)
        thread_time = time.time() - start

        print("\nNormal Matrix Multiplication:")
        for row in C1:
            print(row)

        print("\nMultithreaded Matrix Multiplication:")
        for row in C2:
            print(row)

        print(f"\nNormal Time: {normal_time:.6f} seconds")
        print(f"Threaded Time: {thread_time:.6f} seconds")

        print("\nResults Match:", C1 == C2)

        if normal_time < thread_time:
            print("Normal multiplication is faster.")
        else:
            print("Multithreaded multiplication is faster.")


# ============================================================
# SAMPLE OUTPUT
# ============================================================
#
# Enter matrix size: 2
# Enter first matrix:
# 1 2
# 3 4
# Enter second matrix:
# 5 6
# 7 8
#
# Normal Matrix Multiplication:
# [19, 22]
# [43, 50]
#
# Multithreaded Matrix Multiplication:
# [19, 22]
# [43, 50]
#
# Normal Time: 0.000010 seconds
# Threaded Time: 0.000530 seconds
#
# Results Match: True
# Normal multiplication is faster.
#
# Note: Execution times are illustrative and vary.


# ============================================================
# ------------------------------------------------------------
# THEORY AND VIVA QUESTIONS & ANSWERS
# ------------------------------------------------------------
# ============================================================

# THEORY:
#
# Matrix Multiplication:
# The process of multiplying rows of one matrix
# with columns of another matrix.
#
# Condition:
# Columns of A = Rows of B
#
# Formula:
# C[i][j] = Sum(A[i][k] * B[k][j])
#
# NORMAL MULTIPLICATION:
# Uses nested loops to calculate matrix elements
# sequentially.
#
# MULTITHREADED MULTIPLICATION:
# Uses multiple threads to divide the work.
# This program creates one thread per row.
#
# ALGORITHM:
# 1. Accept matrix size and elements.
# 2. Perform normal multiplication using loops.
# 3. Create one thread for each result row.
# 4. Start all threads using start().
# 5. Wait for completion using join().
# 6. Display results and compare execution times.
#
# COMPLEXITY:
# For two N x N matrices:
#
# Normal Time       : O(N^3)
# Multithreaded Work: O(N^3)
# Space Complexity  : O(N^2) for result matrix
# Additional Space  : O(N) threads and their stacks
#
# Both methods perform O(N^3) arithmetic work.
# Multithreading adds thread creation and scheduling.
#
# Python's standard CPython implementation generally
# has a Global Interpreter Lock (GIL), so CPU-bound
# Python threads may not execute in parallel.


# Q1. What is Matrix Multiplication?
# Ans: Multiplying rows of the first matrix with
# columns of the second matrix.


# Q2. What is the condition for multiplication?
# Ans: Number of columns in A must equal the
# number of rows in B.


# Q3. What is Multithreading?
# Ans: Executing multiple threads concurrently
# within the same process.


# Q4. What is a Thread?
# Ans: A lightweight unit of execution that
# shares memory with other threads.


# Q5. Difference between normal and multithreaded?
# Ans: Normal performs tasks sequentially.
# Multithreaded divides tasks among threads.


# Q6. Why do we use Multithreading?
# Ans: To execute independent tasks concurrently
# and potentially improve performance.


# Q7. What is one thread per row?
# Ans: Each thread calculates one complete row
# of the result matrix.


# Q8. What is one thread per cell?
# Ans: Each thread calculates one element
# of the result matrix.


# Q9. What is the time complexity?
# Ans: O(N^3) total arithmetic work because
# three nested loops perform multiplication.


# Q10. What is the space complexity?
# Ans: O(N^2) for the result matrix.
# Threads also require additional memory.


# Q11. Which method is faster?
# Ans: It depends on matrix size and environment.
# Normal multiplication is often faster in
# standard Python due to thread overhead and GIL.


# Q12. What is GIL?
# Ans: Global Interpreter Lock, which normally
# prevents simultaneous execution of Python
# bytecode by multiple threads in standard CPython.


# Q13. What is threading.Thread()?
# Ans: It creates a new thread to execute
# a specified function.


# Q14. What does start() do?
# Ans: Starts the execution of a thread.


# Q15. What does join() do?
# Ans: Waits for a thread to finish execution.


# Q16. Why do we use time.time()?
# Ans: To measure elapsed execution time.
# Execution Time = End Time - Start Time.


# Q17. Why might Multithreading be slower?
# Ans: Because thread creation and scheduling
# add overhead, and the GIL limits CPU parallelism.


# Q18. What is the difference between
# Concurrency and Parallelism?
# Ans: Concurrency means overlapping task progress.
# Parallelism means simultaneous task execution.


# Q19. Why do both methods produce identical results?
# Ans: Both apply the same multiplication formula.
# Each thread writes to a separate result row.


# Q20. Where is Multithreading used?
# Ans: Web servers, file processing, background
# tasks and concurrent applications.


# ============================================================
# CONCLUSION
# ============================================================
#
# Normal and multithreaded matrix multiplication
# produce identical results.
#
# Multithreading divides work among threads, but
# its performance depends on the execution environment.
# ============================================================
