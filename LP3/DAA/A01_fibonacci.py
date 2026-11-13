"""SPPU Group A #1: iterative and recursive Fibonacci; 0-indexed F(0)=0."""
import argparse
import time

def fibonacci_iterative(n: int) -> int:
    if n < 0: raise ValueError("n must be >= 0")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def fibonacci_recursive(n: int) -> int:
    if n < 0: raise ValueError("n must be >= 0")
    if n < 2: return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def main():
    ap = argparse.ArgumentParser();ap.add_argument('--n',type=int,default=12);args=ap.parse_args()
    if not 0 <= args.n <= 30: ap.error('Use 0 <= n <= 30; naive recursion grows exponentially')
    t=time.perf_counter();a=fibonacci_iterative(args.n);ti=time.perf_counter()-t
    t=time.perf_counter();b=fibonacci_recursive(args.n);tr=time.perf_counter()-t
    assert a==b
    print(f'F({args.n}) = {a}; iterative={ti:.6f}s, recursive={tr:.6f}s')
    print('Iterative: O(n) time / O(1) auxiliary space; recursive: O(2^n) time / O(n) stack')
if __name__=='__main__':main()
