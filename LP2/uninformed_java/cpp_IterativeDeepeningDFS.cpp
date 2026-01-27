#include <algorithm>
#include <iostream>
#include <vector>

static bool dls(int u, int goal, int depth, int limit, const std::vector<std::vector<int>>& graph,
                std::vector<bool>& onPath, std::vector<int>& prev) {
    onPath[u] = true;
    if (u == goal) return true;
    if (depth == limit) {
        onPath[u] = false;
        return false;
    }
    for (int v : graph[u]) {
        if (!onPath[v]) {
            prev[v] = u;
            if (dls(v, goal, depth + 1, limit, graph, onPath, prev)) return true;
        }
    }
    onPath[u] = false;
    return false;
}

static std::vector<int> iddfs_path(const std::vector<std::vector<int>>& graph, int start, int goal, int maxDepth) {
    int n = (int)graph.size();
    for (int limit = 0; limit <= maxDepth; limit++) {
        std::vector<bool> onPath(n, false);
        std::vector<int> prev(n, -1);
        if (dls(start, goal, 0, limit, graph, onPath, prev)) {
            std::vector<int> path;
            for (int at = goal; at != -1; at = prev[at]) path.push_back(at);
            std::reverse(path.begin(), path.end());
            return path;
        }
    }
    return {};
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
    int maxDepth = 5;
    auto path = iddfs_path(graph, start, goal, maxDepth);

    if (path.empty()) {
        std::cout << "No path within max depth " << maxDepth << "\n";
        return 0;
    }

    std::cout << "IDDFS Path: ";
    for (size_t i = 0; i < path.size(); i++) {
        if (i) std::cout << " -> ";
        std::cout << path[i];
    }
    std::cout << "\n";
    return 0;
}

