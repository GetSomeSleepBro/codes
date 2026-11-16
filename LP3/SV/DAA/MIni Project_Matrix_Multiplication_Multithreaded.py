import threading
import time
import math


def read_matrix(name, rows, cols):
    print(f"\nEnter Matrix {name}:")
    matrix = []

    for i in range(rows):
        while True:
            try:
                values = list(map(float, input(f"Row {i + 1}: ").split()))
                if len(values) != cols:
                    print(f"Please enter exactly {cols} values.")
                else:
                    matrix.append(values)
                    break
            except ValueError:
                print("Please enter valid numbers.")

    return matrix


def normal_multiply(A, B):
    rows = len(A)
    common = len(B)
    cols = len(B[0])
    C = [[0.0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            for k in range(common):
                C[i][j] += A[i][k] * B[k][j]

    return C


def threaded_multiply(A, B):
    rows = len(A)
    common = len(B)
    cols = len(B[0])
    C = [[0.0 for _ in range(cols)] for _ in range(rows)]

    def multiply_row(i):
        for j in range(cols):
            for k in range(common):
                C[i][j] += A[i][k] * B[k][j]

    threads = []

    for i in range(rows):
        t = threading.Thread(target=multiply_row, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return C


def display(C):
    for row in C:
        print(" ".join(f"{value:g}" for value in row))


def matrices_equal(A, B):
    for i in range(len(A)):
        for j in range(len(A[0])):
            if not math.isclose(A[i][j], B[i][j], rel_tol=1e-9, abs_tol=1e-9):
                return False
    return True


def main():
    r1, c1 = map(int, input("Enter rows and columns of A: ").split())
    r2, c2 = map(int, input("Enter rows and columns of B: ").split())

    if min(r1, c1, r2, c2) <= 0:
        print("Invalid matrix dimensions!")
        return

    if c1 != r2:
        print("Matrix multiplication is not possible!")
        return

    A = read_matrix("A", r1, c1)
    B = read_matrix("B", r2, c2)

    start = time.perf_counter()
    C1 = normal_multiply(A, B)
    t1 = time.perf_counter() - start

    start = time.perf_counter()
    C2 = threaded_multiply(A, B)
    t2 = time.perf_counter() - start

    print("\nNormal Matrix Multiplication:")
    display(C1)

    print("\nMultithreaded Matrix Multiplication:")
    display(C2)

    print("\nPerformance Comparison:")
    print(f"Normal Time: {t1:.6f} seconds")
    print(f"Multithreaded Time: {t2:.6f} seconds")

    if matrices_equal(C1, C2):
        print("Both results are equal.")
    else:
        print("The results are different.")

    if t1 < t2:
        print("Normal multiplication is faster.")
    elif t2 < t1:
        print("Multithreaded multiplication is faster.")
    else:
        print("Both methods took the same time.")


if __name__ == "__main__":
    main()


# SAMPLE OUTPUT (execution times vary depending on the computer):
# Enter rows and columns of A: 2 3
# Enter rows and columns of B: 3 2
#
# Enter Matrix A:
# Row 1: 1 2 3
# Row 2: 4 5 6
#
# Enter Matrix B:
# Row 1: 7 8
# Row 2: 9 10
# Row 3: 11 12
#
# Normal Matrix Multiplication:
# 58 64
# 139 154
#
# Multithreaded Matrix Multiplication:
# 58 64
# 139 154
#
# Performance Comparison:
# Normal Time: 0.000020 seconds
# Multithreaded Time: 0.000650 seconds
# Both results are equal.
# Normal multiplication is faster.
