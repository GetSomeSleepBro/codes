// DAA Assignment 4
// Write a program to solve a 0-1 Knapsack problem using dynamic programming
// or branch and bound strategy.   (Dynamic Programming used here)
// Compile: g++ knapsack_01.cpp -o k01     Run: ./k01
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, W;
    cout << "Enter number of items: ";
    cin >> n;
    vector<int> val(n + 1), wt(n + 1);
    for (int i = 1; i <= n; i++) {
        cout << "Enter value and weight of item " << i << ": ";
        cin >> val[i] >> wt[i];
    }
    cout << "Enter knapsack capacity: ";
    cin >> W;

    if (n < 0 || W < 0 || W > 100000) { cerr << "Invalid item count or capacity\n"; return 1; }
    for (int i = 1; i <= n; ++i) if (wt[i] <= 0 || val[i] < 0) { cerr << "Invalid weight or value\n"; return 1; }
    // dp[i][w] = best value using first i items with capacity w
    vector<vector<int>> dp(n + 1, vector<int>(W + 1, 0));
    for (int i = 1; i <= n; i++) {
        for (int w = 0; w <= W; w++) {
            dp[i][w] = dp[i - 1][w];                                   // don't take item i
            if (wt[i] <= w)
                dp[i][w] = max(dp[i][w], val[i] + dp[i - 1][w - wt[i]]); // take item i
        }
    }

    cout << "\nDP Table:\n";
    for (int i = 0; i <= n; i++) {
        for (int w = 0; w <= W; w++) cout << dp[i][w] << "\t";
        cout << "\n";
    }

    // Backtrack to find which items were selected
    cout << "\nItems selected: ";
    int w = W;
    for (int i = n; i > 0; i--) {
        if (dp[i][w] != dp[i - 1][w]) {
            cout << i << " ";
            w -= wt[i];
        }
    }

    cout << "\nMaximum profit = " << dp[n][W] << "\n";
    cout << "\nTime Complexity : O(n * W)";
    cout << "\nSpace Complexity: O(n * W)\n";
    return 0;
}
