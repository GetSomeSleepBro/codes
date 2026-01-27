// Uninformed Search: BFS
#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>

static std::vector<int> bfs_path(const std::vector<std::vector<int>>& graph, int start, int goal) {
    int n = (int)graph.size();
    std::vector<int> prev(n, -1);
    std::vector<bool> visited(n, false);
    std::queue<int> q;

    visited[start] = true;
    q.push(start);

    while (!q.empty()) {
        int u = q.front();
        q.pop();
        if (u == goal) break;
        for (int v : graph[u]) {
            if (!visited[v]) {
                visited[v] = true;
                prev[v] = u;
                q.push(v);
            }
        }
    }

    if (!visited[goal]) return {};
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
    auto path = bfs_path(graph, start, goal);

    if (path.empty()) {
        std::cout << "No path\n";
        return 0;
    }

    std::cout << "BFS Path: ";
    for (size_t i = 0; i < path.size(); i++) {
        if (i) std::cout << " -> ";
        std::cout << path[i];
    }
    std::cout << "\n";
    return 0;
}
