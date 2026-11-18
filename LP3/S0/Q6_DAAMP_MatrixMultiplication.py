# DAA Mini Project: normal vs multithreaded square matrix multiplication
import threading
import time


def normal_multiply(A, B):
    n = len(A)
    C = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C


def multiply_row(A, B, C, row):
    n = len(A)
    for j in range(n):
        for k in range(n):
            C[row][j] += A[row][k] * B[k][j]


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
        start = time.time()
        C1 = normal_multiply(A, B)
        normal_time = time.time() - start
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
