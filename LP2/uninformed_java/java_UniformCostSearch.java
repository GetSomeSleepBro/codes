import java.util.*;

public class java_UniformCostSearch {
    static class Edge {
        int to, w;
        Edge(int to, int w) { this.to = to; this.w = w; }
    }

    static List<Integer> ucsPath(List<List<Edge>> graph, int start, int goal) {
        int n = graph.size();
        int[] dist = new int[n];
        int[] prev = new int[n];
        Arrays.fill(dist, Integer.MAX_VALUE / 4);
        Arrays.fill(prev, -1);

        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0])); // {cost, node}
        dist[start] = 0;
        pq.add(new int[]{0, start});

        while (!pq.isEmpty()) {
            int[] cur = pq.remove();
            int cost = cur[0], u = cur[1];
            if (cost != dist[u]) continue;
            if (u == goal) break;

            for (Edge e : graph.get(u)) {
                int nc = cost + e.w;
                if (nc < dist[e.to]) {
                    dist[e.to] = nc;
                    prev[e.to] = u;
                    pq.add(new int[]{nc, e.to});
                }
            }
        }

        if (dist[goal] >= Integer.MAX_VALUE / 8) return Collections.emptyList();
        List<Integer> path = new ArrayList<>();
        for (int at = goal; at != -1; at = prev[at]) path.add(at);
        Collections.reverse(path);
        return path;
    }

    public static void main(String[] args) {
        List<List<Edge>> graph = Arrays.asList(
                Arrays.asList(new Edge(1, 2), new Edge(2, 4)), // 0
                Arrays.asList(new Edge(3, 7), new Edge(4, 3)), // 1
                Arrays.asList(new Edge(5, 1)),                 // 2
                Arrays.asList(new Edge(6, 1)),                 // 3
                Arrays.asList(new Edge(6, 5)),                 // 4
                Arrays.asList(new Edge(6, 3)),                 // 5
                Arrays.asList()                                // 6
        );

        int start = 0, goal = 6;
        List<Integer> path = ucsPath(graph, start, goal);
        if (path.isEmpty()) {
            System.out.println("No path");
            return;
        }

        System.out.print("UCS Path: ");
        for (int i = 0; i < path.size(); i++) {
            if (i > 0) System.out.print(" -> ");
            System.out.print(path.get(i));
        }
        System.out.println();
    }
}

