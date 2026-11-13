// DAA Assignment 5
// Design n-Queens matrix having first Queen placed. Use backtracking to place
// remaining Queens to generate the final n-queen's matrix.
// Compile: g++ n_queens.cpp -o nq     Run: ./nq
#include <iostream>
#include <vector>
using namespace std;

int n;
vector<vector<int>> board;

bool isSafe(int row, int col) {
    for (int i = 0; i < row; i++)                                   // same column above
        if (board[i][col]) return false;
    for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--)  // upper-left diagonal
        if (board[i][j]) return false;
    for (int i = row - 1, j = col + 1; i >= 0 && j < n; i--, j++)   // upper-right diagonal
        if (board[i][j]) return false;
    return true;
}

// Row 0 already has the first queen; place queens from row 1 onwards
bool solve(int row) {
    if (row == n) return true;
    for (int col = 0; col < n; col++) {
        if (isSafe(row, col)) {
            board[row][col] = 1;          // place
            if (solve(row + 1)) return true;
            board[row][col] = 0;          // backtrack
        }
    }
    return false;
}

void printBoard() {
    for (auto &r : board) {
        for (int c : r) cout << (c ? " Q " : " . ");
        cout << "\n";
    }
}

int main() {
    int firstCol;
    cout << "Enter n (board size): ";
    cin >> n;
    cout << "Enter column (0 to " << n - 1 << ") of first queen in row 0: ";
    cin >> firstCol;

    if (n < 1 || n > 14 || firstCol < 0 || firstCol >= n) { cerr << "Invalid board or first queen column\n"; return 1; }
    board.assign(n, vector<int>(n, 0));
    board[0][firstCol] = 1;               // first queen already placed

    cout << "\nInitial board (first queen placed):\n";
    printBoard();

    if (solve(1)) {
        cout << "\nFinal " << n << "-Queens matrix:\n";
        printBoard();
        cout << "\nMatrix form:\n";
        for (auto &r : board) {
            for (int c : r) cout << c << " ";
            cout << "\n";
        }
    } else {
        cout << "\nNo solution exists with first queen at column " << firstCol << "\n";
    }

    cout << "\nTime Complexity : O(n!)";
    cout << "\nSpace Complexity: O(n^2) board + O(n) recursion stack\n";
    return 0;
}
