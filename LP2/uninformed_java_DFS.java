import java.util.*;

public class uninformed_java_DFS {
    static boolean dfs(int u, int goal, List<List<Integer>> graph, boolean[] visited, int[] prev) {
        visited[u] = true;
        if (u == goal) return true;
        for (int v : graph.get(u)) {
            if (!visited[v]) {
                prev[v] = u;
                if (dfs(v, goal, graph, visited, prev)) return true;
            }
        }
        return false;
    }

    static List<Integer> dfsPath(List<List<Integer>> graph, int start, int goal) {
        int n = graph.size();
        boolean[] visited = new boolean[n];
        int[] prev = new int[n];
        Arrays.fill(prev, -1);

        if (!dfs(start, goal, graph, visited, prev)) return Collections.emptyList();

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
        List<Integer> path = dfsPath(graph, start, goal);
        if (path.isEmpty()) {
            System.out.println("No path");
            return;
        }

        System.out.print("DFS Path: ");
        for (int i = 0; i < path.size(); i++) {
            if (i > 0) System.out.print(" -> ");
            System.out.print(path.get(i));
        }
        System.out.println();
    }
}
