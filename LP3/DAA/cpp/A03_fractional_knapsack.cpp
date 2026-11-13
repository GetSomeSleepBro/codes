// DAA Assignment 3
// Write a program to solve a fractional Knapsack problem using a greedy method.
// Compile: g++ fractional_knapsack.cpp -o fk     Run: ./fk
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Item {
    int id;
    double value, weight;
};

int main() {
    int n;
    double capacity;
    cout << "Enter number of items: ";
    cin >> n;
    vector<Item> items(n);
    for (int i = 0; i < n; i++) {
        cout << "Enter value and weight of item " << i + 1 << ": ";
        cin >> items[i].value >> items[i].weight;
        items[i].id = i + 1;
    }
    cout << "Enter knapsack capacity: ";
    cin >> capacity;

    if (n < 0 || capacity < 0) { cerr << "Invalid capacity or item count\n"; return 1; }
    for (const auto &it : items) if (it.weight <= 0 || it.value < 0) { cerr << "Weights must be positive and values nonnegative\n"; return 1; }
    // Greedy choice: highest value/weight ratio first
    sort(items.begin(), items.end(), [](const Item &a, const Item &b) {
        return a.value / a.weight > b.value / b.weight;
    });

    double totalValue = 0, remaining = capacity;
    cout << "\nItem\tValue\tWeight\tRatio\tFraction taken\n";
    for (auto &it : items) {
        double fraction = 0;
        if (remaining <= 0) fraction = 0;
        else if (it.weight <= remaining) fraction = 1;
        else fraction = remaining / it.weight;

        totalValue += it.value * fraction;
        remaining -= it.weight * fraction;
        cout << it.id << "\t" << it.value << "\t" << it.weight << "\t"
             << it.value / it.weight << "\t" << fraction << "\n";
    }

    cout << "\nMaximum value in knapsack = " << totalValue << "\n";
    cout << "\nTime Complexity : O(n log n) (sorting)";
    cout << "\nSpace Complexity: O(1) extra (O(n) for items)\n";
    return 0;
}
