// Informed Search: Best-First (Greedy)
#include <algorithm>
#include <iostream>
#include <queue>
#include <utility>
#include <vector>

static std::vector<int> greedy_best_first_path(const std::vector<std::vector<int>>& graph,
                                               const std::vector<int>& h, int start, int goal) {
    int n = (int)graph.size();
    std::vector<int> prev(n, -1);
    std::vector<bool> visited(n, false);

    using State = std::pair<int, int>; // (heuristic, node)
    std::priority_queue<State, std::vector<State>, std::greater<State>> pq;
    pq.push({h[start], start});

    while (!pq.empty()) {
        auto [_, u] = pq.top();
        pq.pop();
        if (visited[u]) continue;
        visited[u] = true;
        if (u == goal) break;

        for (int v : graph[u]) {
            if (!visited[v]) {
                if (prev[v] == -1) prev[v] = u;
                pq.push({h[v], v});
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

    // heuristic (estimated distance to goal)
    std::vector<int> h = {7, 6, 5, 1, 4, 2, 0};

    int start = 0, goal = 6;
    auto path = greedy_best_first_path(graph, h, start, goal);

    if (path.empty()) {
        std::cout << "No path\n";
        return 0;
    }

    std::cout << "Best-First (Greedy) Path: ";
    for (size_t i = 0; i < path.size(); i++) {
        if (i) std::cout << " -> ";
        std::cout << path[i];
    }
    std::cout << "\n";
    return 0;
}
