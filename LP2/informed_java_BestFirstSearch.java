import java.util.*;

public class informed_java_BestFirstSearch {
    static List<Integer> greedyBestFirstPath(List<List<Integer>> graph, int[] h, int start, int goal) {
        int n = graph.size();
        int[] prev = new int[n];
        boolean[] visited = new boolean[n];
        Arrays.fill(prev, -1);

        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0])); // {heuristic, node}
        pq.add(new int[]{h[start], start});

        while (!pq.isEmpty()) {
            int[] cur = pq.remove();
            int u = cur[1];
            if (visited[u]) continue;
            visited[u] = true;
            if (u == goal) break;

            for (int v : graph.get(u)) {
                if (!visited[v]) {
                    if (prev[v] == -1) prev[v] = u;
                    pq.add(new int[]{h[v], v});
                }
            }
        }

        if (!visited[goal]) return Collections.emptyList();
        List<Integer> path = new ArrayList<>();
        for (int at = goal; at != -1; at = prev[at]) path.add(at);
        Collections.reverse(path);
        return path;
    }

    public static void main(String[] args) {
        List<List<Integer>> graph = Arrays.asList(
                Arrays.asList(1, 2),  // 0
                Arrays.asList(3, 4),  // 1
                Arrays.asList(5),     // 2
                Arrays.asList(6),     // 3
                Arrays.asList(6),     // 4
                Arrays.asList(6),     // 5
                Arrays.asList()       // 6
        );

        int[] h = {7, 6, 5, 1, 4, 2, 0};
        int start = 0, goal = 6;

        List<Integer> path = greedyBestFirstPath(graph, h, start, goal);
        if (path.isEmpty()) {
            System.out.println("No path");
            return;
        }

        System.out.print("Best-First (Greedy) Path: ");
        for (int i = 0; i < path.size(); i++) {
            if (i > 0) System.out.print(" -> ");
            System.out.print(path.get(i));
        }
        System.out.println();
    }
}
