// DAA Assignment 1
// Write a non-recursive and recursive program to calculate Fibonacci numbers
// and analyze their time and space complexity.
// Compile: g++ fibonacci.cpp -o fib     Run: ./fib   (Windows: fib.exe)
#include <iostream>
using namespace std;

long long recSteps = 0;   // number of function calls in recursive version
long long iterSteps = 0;  // number of loop iterations in iterative version

// Recursive: T(n) = T(n-1) + T(n-2) + O(1)  =>  O(2^n) time, O(n) stack space
long long fibRecursive(int n) {
    recSteps++;
    if (n <= 1) return n;
    return fibRecursive(n - 1) + fibRecursive(n - 2);
}

// Iterative (non-recursive): O(n) time, O(1) space
long long fibIterative(int n) {
    if (n <= 1) return n;
    long long a = 0, b = 1, c;
    for (int i = 2; i <= n; i++) {
        iterSteps++;
        c = a + b;
        a = b;
        b = c;
    }
    return b;
}

int main() {
    int n;
    cout << "Enter n: ";
    cin >> n;

    if (n < 0 || n > 40) { cerr << "Use n between 0 and 40\n"; return 1; }
    cout << "\nFibonacci series (iterative): ";
    long long a = 0, b = 1;
    for (int i = 0; i < n; i++) {
        cout << a << " ";
        long long c = a + b; a = b; b = c;
    }

    cout << "\n\nF(" << n << ") using recursion     = " << fibRecursive(n);
    cout << "\nF(" << n << ") using non-recursion = " << fibIterative(n);
    cout << "\n\nSteps (recursive calls)     : " << recSteps;
    cout << "\nSteps (iterative loop runs) : " << iterSteps << "\n";

    cout << "\nComplexity Analysis:";
    cout << "\n  Recursive     -> Time O(2^n), Space O(n) (recursion stack)";
    cout << "\n  Non-recursive -> Time O(n),   Space O(1)\n";
    return 0;
}
