// Uninformed Search: DFS
#include <algorithm>
#include <iostream>
#include <vector>

static bool dfs(int u, int goal, const std::vector<std::vector<int>>& graph, std::vector<bool>& visited,
                std::vector<int>& prev) {
    visited[u] = true;
    if (u == goal) return true;
    for (int v : graph[u]) {
        if (!visited[v]) {
            prev[v] = u;
            if (dfs(v, goal, graph, visited, prev)) return true;
        }
    }
    return false;
}

static std::vector<int> dfs_path(const std::vector<std::vector<int>>& graph, int start, int goal) {
    int n = (int)graph.size();
    std::vector<int> prev(n, -1);
    std::vector<bool> visited(n, false);

    if (!dfs(start, goal, graph, visited, prev)) return {};

    std::vector<int> path;
    for (int at = goal; at != -1; at = prev[at]) path.push_back(at);
    std::reverse(path.begin(), path.end());
    return path;
}

int main() {
    std::vector<std::vector<int>> graph = {
        {1, 2},    // 0
        {3, 4},    // 1
        {5},       // 2
        {6},       // 3
        {6},       // 4
        {6},       // 5
        {}         // 6
    };

    int start = 0, goal = 6;
    auto path = dfs_path(graph, start, goal);

    if (path.empty()) {
        std::cout << "No path\n";
        return 0;
    }

    std::cout << "DFS Path: ";
    for (size_t i = 0; i < path.size(); i++) {
        if (i) std::cout << " -> ";
        std::cout << path[i];
    }
    std::cout << "\n";
    return 0;
}



// #include <bits/stdc++.h>
// using namespace std;

// void dfs(int node, vector<vector<int>>& graph, vector<bool>& visited) {
//     visited[node] = true;
//     cout << node << " ";

//     for (int neighbor : graph[node]) {
//         if (!visited[neighbor]) {
//             dfs(neighbor, graph, visited);
//         }
//     }
// }

// int main() {
//     int n = 5; // number of nodes (0 to 4)
//     vector<vector<int>> graph(n);

//     // example edges
//     graph[0] = {1, 2};
//     graph[1] = {3};
//     graph[2] = {};
//     graph[3] = {4};
//     graph[4] = {};

//     vector<bool> visited(n, false);

//     dfs(0, graph, visited);

//     return 0;
// }

