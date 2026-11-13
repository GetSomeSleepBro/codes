// DAA Assignment 2
// Write a program to implement Huffman Encoding using a greedy strategy.
// Compile: g++ huffman.cpp -o huff     Run: ./huff
#include <iostream>
#include <queue>
#include <vector>
#include <string>
#include <map>
using namespace std;

struct Node {
    char ch;
    int freq;
    Node *left, *right;
    Node(char c, int f, Node *l = nullptr, Node *r = nullptr) : ch(c), freq(f), left(l), right(r) {}
};

// Min-heap ordering: smaller frequency = higher priority
struct Compare {
    bool operator()(Node *a, Node *b) { return a->freq > b->freq; }
};

void buildCodes(Node *root, string code, map<char, string> &codes) {
    if (!root) return;
    if (!root->left && !root->right) {          // leaf node
        codes[root->ch] = code.empty() ? "0" : code;
        return;
    }
    buildCodes(root->left, code + "0", codes);
    buildCodes(root->right, code + "1", codes);
}

int main() {
    string text;
    cout << "Enter text to encode: ";
    getline(cin, text);

    // 1. Count frequency of each character
    map<char, int> freq;
    for (char c : text) freq[c]++;

    // 2. Push all characters into a min-heap
    priority_queue<Node *, vector<Node *>, Compare> pq;
    for (auto &p : freq) pq.push(new Node(p.first, p.second));

    // 3. Greedy step: repeatedly merge the two least frequent nodes
    while (pq.size() > 1) {
        Node *l = pq.top(); pq.pop();
        Node *r = pq.top(); pq.pop();
        pq.push(new Node('$', l->freq + r->freq, l, r));
    }

    map<char, string> codes;
    if (!pq.empty()) buildCodes(pq.top(), "", codes);

    cout << "\nChar\tFreq\tCode\n";
    for (auto &p : codes) cout << "'" << p.first << "'\t" << freq[p.first] << "\t" << p.second << "\n";

    string encoded;
    for (char c : text) encoded += codes[c];
    cout << "\nEncoded string : " << encoded;
    cout << "\nOriginal size  : " << text.size() * 8 << " bits";
    cout << "\nEncoded size   : " << encoded.size() << " bits\n";

    cout << "\nTime Complexity : O(n log n), n = number of unique characters";
    cout << "\nSpace Complexity: O(n)\n";
    return 0;
}
