// Uninformed Search: Bidirectional Search
#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>

static std::vector<int> build_path(int meet, const std::vector<int>& parentA, const std::vector<int>& parentB) {
    std::vector<int> left;
    for (int at = meet; at != -1; at = parentA[at]) left.push_back(at);
    std::reverse(left.begin(), left.end()); // start -> meet

    std::vector<int> right;
    for (int at = parentB[meet]; at != -1; at = parentB[at]) right.push_back(at); // meet -> goal (excluding meet)

    left.insert(left.end(), right.begin(), right.end());
    return left;
}

static std::vector<int> bidir_path(const std::vector<std::vector<int>>& graph, int start, int goal) {
    int n = (int)graph.size();
    std::vector<bool> visA(n, false), visB(n, false);
    std::vector<int> parentA(n, -1), parentB(n, -1);
    std::queue<int> qa, qb;

    visA[start] = true;
    visB[goal] = true;
    qa.push(start);
    qb.push(goal);

    while (!qa.empty() && !qb.empty()) {
        int szA = (int)qa.size();
        while (szA--) {
            int u = qa.front();
            qa.pop();
            if (visB[u]) return build_path(u, parentA, parentB);
            for (int v : graph[u]) {
                if (!visA[v]) {
                    visA[v] = true;
                    parentA[v] = u;
                    qa.push(v);
                }
            }
        }

        int szB = (int)qb.size();
        while (szB--) {
            int u = qb.front();
            qb.pop();
            if (visA[u]) return build_path(u, parentA, parentB);
            for (int v : graph[u]) {
                if (!visB[v]) {
                    visB[v] = true;
                    parentB[v] = u;
                    qb.push(v);
                }
            }
        }
    }

    return {};
}

int main() {
    // Undirected graph (so bidirectional search is simple)
    std::vector<std::vector<int>> graph = {
        {1, 2},       // 0
        {0, 3, 4},    // 1
        {0, 5},       // 2
        {1, 6},       // 3
        {1, 6},       // 4
        {2, 6},       // 5
        {3, 4, 5}     // 6
    };

    int start = 0, goal = 6;
    auto path = bidir_path(graph, start, goal);

    if (path.empty()) {
        std::cout << "No path\n";
        return 0;
    }

    std::cout << "Bidirectional Path: ";
    for (size_t i = 0; i < path.size(); i++) {
        if (i) std::cout << " -> ";
        std::cout << path[i];
    }
    std::cout << "\n";
    return 0;
}
