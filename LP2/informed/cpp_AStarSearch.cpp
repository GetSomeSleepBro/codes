#include <algorithm>
#include <iostream>
#include <limits>
#include <queue>
#include <tuple>
#include <utility>
#include <vector>

struct Edge {
    int to;
    int w;
};

static std::vector<int> astar_path(const std::vector<std::vector<Edge>>& graph, const std::vector<int>& h,
                                   int start, int goal) {
    int n = (int)graph.size();
    const int INF = std::numeric_limits<int>::max() / 4;

    std::vector<int> gCost(n, INF);
    std::vector<int> prev(n, -1);

    using State = std::tuple<int, int, int>; // (f = g + h, g, node)
    std::priority_queue<State, std::vector<State>, std::greater<State>> pq;

    gCost[start] = 0;
    pq.push({h[start], 0, start});

    while (!pq.empty()) {
        auto [f, g, u] = pq.top();
        pq.pop();
        if (g != gCost[u]) continue;
        if (u == goal) break;

        for (const auto& e : graph[u]) {
            int ng = g + e.w;
            if (ng < gCost[e.to]) {
                gCost[e.to] = ng;
                prev[e.to] = u;
                pq.push({ng + h[e.to], ng, e.to});
            }
        }
    }

    if (gCost[goal] == INF) return {};
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

    std::vector<int> h = {7, 6, 5, 1, 4, 2, 0};
    int start = 0, goal = 6;

    auto path = astar_path(graph, h, start, goal);
    if (path.empty()) {
        std::cout << "No path\n";
        return 0;
    }

    std::cout << "A* Path: ";
    for (size_t i = 0; i < path.size(); i++) {
        if (i) std::cout << " -> ";
        std::cout << path[i];
    }
    std::cout << "\n";
    return 0;
}

