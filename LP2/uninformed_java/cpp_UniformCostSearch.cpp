#include <algorithm>
#include <iostream>
#include <limits>
#include <queue>
#include <utility>
#include <vector>

struct Edge {
    int to;
    int w;
};

static std::vector<int> ucs_path(const std::vector<std::vector<Edge>>& graph, int start, int goal) {
    int n = (int)graph.size();
    const int INF = std::numeric_limits<int>::max() / 4;

    std::vector<int> dist(n, INF);
    std::vector<int> prev(n, -1);

    using State = std::pair<int, int>; // (cost, node)
    std::priority_queue<State, std::vector<State>, std::greater<State>> pq;

    dist[start] = 0;
    pq.push({0, start});

    while (!pq.empty()) {
        auto [cost, u] = pq.top();
        pq.pop();
        if (cost != dist[u]) continue;
        if (u == goal) break;

        for (const auto& e : graph[u]) {
            int nc = cost + e.w;
            if (nc < dist[e.to]) {
                dist[e.to] = nc;
                prev[e.to] = u;
                pq.push({nc, e.to});
            }
        }
    }

    if (dist[goal] == INF) return {};
    std::vector<int> path;
    for (int at = goal; at != -1; at = prev[at]) path.push_back(at);
    std::reverse(path.begin(), path.end());
    return path;
}

int main() {
    std::vector<std::vector<Edge>> graph = {
        {{1, 2}, {2, 4}},   // 0
        {{3, 7}, {4, 3}},   // 1
        {{5, 1}},           // 2
        {{6, 1}},           // 3
        {{6, 5}},           // 4
        {{6, 3}},           // 5
        {}                  // 6
    };

    int start = 0, goal = 6;
    auto path = ucs_path(graph, start, goal);

    if (path.empty()) {
        std::cout << "No path\n";
        return 0;
    }

    std::cout << "UCS Path: ";
    for (size_t i = 0; i < path.size(); i++) {
        if (i) std::cout << " -> ";
        std::cout << path[i];
    }
    std::cout << "\n";
    return 0;
}

