import time

# Recursive method
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Non-recursive method
def fibonacci_iterative(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

n = int(input("Enter n: "))

if n < 0 or n > 35:
    print("Enter n between 0 and 35")
else:
    start = time.perf_counter()
    print("Recursive Result:", fibonacci_recursive(n))
    print("Recursive Time:", time.perf_counter() - start)

    start = time.perf_counter()
    print("Non-Recursive Result:", fibonacci_iterative(n))
    print("Non-Recursive Time:", time.perf_counter() - start)

    print("\nTime Complexity:")
    print("Recursive: O(2^n)")
    print("Non-Recursive: O(n)")

    print("\nSpace Complexity:")
    print("Recursive: O(n)")
    print("Non-Recursive: O(1)")
