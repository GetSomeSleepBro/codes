// DAA Assignment 6 (not a mini-project under SPPU LP-III)
// Write a program for analysis of quick sort by using deterministic and
// randomized variant.
// Compile: g++ -O2 quicksort_analysis.cpp -o qs     Run: ./qs
#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <chrono>
#include <algorithm>
using namespace std;

long long comparisons = 0;

// Lomuto partition with last element as pivot
int partition(vector<int> &a, int low, int high) {
    int pivot = a[high];
    int i = low - 1;
    for (int j = low; j < high; j++) {
        comparisons++;
        if (a[j] <= pivot) swap(a[++i], a[j]);
    }
    swap(a[i + 1], a[high]);
    return i + 1;
}

// Deterministic: always uses last element as pivot
void quickSort(vector<int> &a, int low, int high) {
    if (low < high) {
        int p = partition(a, low, high);
        quickSort(a, low, p - 1);
        quickSort(a, p + 1, high);
    }
}

// Randomized: swap a random element into the pivot position first
int randomPartition(vector<int> &a, int low, int high) {
    int r = low + rand() % (high - low + 1);
    swap(a[r], a[high]);
    return partition(a, low, high);
}

void randomizedQuickSort(vector<int> &a, int low, int high) {
    if (low < high) {
        int p = randomPartition(a, low, high);
        randomizedQuickSort(a, low, p - 1);
        randomizedQuickSort(a, p + 1, high);
    }
}

void runTest(const string &label, vector<int> data) {
    vector<int> d1 = data, d2 = data;

    comparisons = 0;
    auto t1 = chrono::high_resolution_clock::now();
    quickSort(d1, 0, d1.size() - 1);
    auto t2 = chrono::high_resolution_clock::now();
    long long detComp = comparisons;
    double detTime = chrono::duration<double, milli>(t2 - t1).count();

    comparisons = 0;
    t1 = chrono::high_resolution_clock::now();
    randomizedQuickSort(d2, 0, d2.size() - 1);
    t2 = chrono::high_resolution_clock::now();
    long long randComp = comparisons;
    double randTime = chrono::duration<double, milli>(t2 - t1).count();

    cout << label << "\n";
    cout << "  Deterministic : comparisons = " << detComp << ", time = " << detTime << " ms\n";
    cout << "  Randomized    : comparisons = " << randComp << ", time = " << randTime << " ms\n";
}

int main() {
    srand(time(0));

    // Small demo with user input
    int n;
    cout << "Enter number of elements: ";
    cin >> n;
    vector<int> a(n);
    cout << "Enter elements: ";
    for (int &x : a) cin >> x;
    vector<int> b = a;
    quickSort(a, 0, n - 1);
    randomizedQuickSort(b, 0, n - 1);
    cout << "Sorted (deterministic): ";
    for (int x : a) cout << x << " ";
    cout << "\nSorted (randomized)   : ";
    for (int x : b) cout << x << " ";
    cout << "\n\n===== Performance Analysis (N = 5000) =====\n";

    int N = 5000;
    vector<int> randomArr(N), sortedArr(N), reverseArr(N);
    for (int i = 0; i < N; i++) {
        randomArr[i] = rand() % 100000;
        sortedArr[i] = i;
        reverseArr[i] = N - i;
    }
    runTest("Random input:", randomArr);
    runTest("Already sorted input (worst case for deterministic):", sortedArr);
    runTest("Reverse sorted input:", reverseArr);

    cout << "\nConclusion:\n";
    cout << "  Deterministic: Best/Avg O(n log n), Worst O(n^2) on sorted/reverse input.\n";
    cout << "  Randomized   : Expected O(n log n) for every input; worst case O(n^2) is very unlikely.\n";
    cout << "  Space        : O(log n) average recursion stack.\n";
    return 0;
}
