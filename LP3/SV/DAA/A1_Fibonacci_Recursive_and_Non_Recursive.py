import time


def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n):
    first, second = 0, 1
    for i in range(n):
        first, second = second, first + second
    return first


def main():
    n = int(input("Enter the value of n (0 to 35): "))

    if n < 0 or n > 35:
        print("Enter a value between 0 and 35 for the recursive comparison.")
        return

    start = time.perf_counter()
    recursive_result = fibonacci_recursive(n)
    recursive_time = time.perf_counter() - start

    start = time.perf_counter()
    iterative_result = fibonacci_iterative(n)
    iterative_time = time.perf_counter() - start

    print("\nRecursive Fibonacci:")
    print("Fibonacci number:", recursive_result)
    print(f"Execution time: {recursive_time:.6f} seconds")

    print("\nNon-Recursive Fibonacci:")
    print("Fibonacci number:", iterative_result)
    print(f"Execution time: {iterative_time:.6f} seconds")

    print("\nExecution-Time Comparison:")
    print(f"{'n':<6}{'Recursive Time (s)':<22}{'Iterative Time (s)'}")

    for value in [10, 20, 30, 35]:
        start = time.perf_counter()
        fibonacci_recursive(value)
        recursive_time = time.perf_counter() - start

        start = time.perf_counter()
        fibonacci_iterative(value)
        iterative_time = time.perf_counter() - start

        print(f"{value:<6}{recursive_time:<22.6f}{iterative_time:.6f}")

    print("\nTime and Space Complexity:")
    print("Recursive    : Time O(2^n), Space O(n)")
    print("Non-Recursive: Time O(n), Space O(1)")


if __name__ == "__main__":
    main()


# SAMPLE OUTPUT (times will vary on every computer):
# Enter the value of n (0 to 35): 7
#
# Recursive Fibonacci:
# Fibonacci number: 13
# Execution time: 0.000004 seconds
#
# Non-Recursive Fibonacci:
# Fibonacci number: 13
# Execution time: 0.000002 seconds
#
# Execution-Time Comparison:
# n     Recursive Time (s)    Iterative Time (s)
# 10    0.000006              0.000002
# 20    0.000540              0.000001
# 30    0.070833              0.000008
# 35    0.819534              0.000008
#
# Time and Space Complexity:
# Recursive    : Time O(2^n), Space O(n)
# Non-Recursive: Time O(n), Space O(1)
