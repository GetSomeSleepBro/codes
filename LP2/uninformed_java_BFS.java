import java.util.*;

public class uninformed_java_BFS {
    static List<Integer> bfsPath(List<List<Integer>> graph, int start, int goal) {
        int n = graph.size();
        int[] prev = new int[n];
        boolean[] visited = new boolean[n];
        Arrays.fill(prev, -1);

        Queue<Integer> q = new ArrayDeque<>();
        visited[start] = true;
        q.add(start);

        while (!q.isEmpty()) {
            int u = q.remove();
            if (u == goal) break;
            for (int v : graph.get(u)) {
                if (!visited[v]) {
                    visited[v] = true;
                    prev[v] = u;
                    q.add(v);
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

        int start = 0, goal = 6;
        List<Integer> path = bfsPath(graph, start, goal);
        if (path.isEmpty()) {
            System.out.println("No path");
            return;
        }

        System.out.print("BFS Path: ");
        for (int i = 0; i < path.size(); i++) {
            if (i > 0) System.out.print(" -> ");
            System.out.print(path.get(i));
        }
        System.out.println();
    }
}
