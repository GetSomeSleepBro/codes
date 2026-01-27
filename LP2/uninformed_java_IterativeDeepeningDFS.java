import java.util.*;

public class uninformed_java_IterativeDeepeningDFS {
    static boolean dls(int u, int goal, int depth, int limit, List<List<Integer>> graph,
                       boolean[] onPath, int[] prev) {
        onPath[u] = true;
        if (u == goal) return true;
        if (depth == limit) {
            onPath[u] = false;
            return false;
        }
        for (int v : graph.get(u)) {
            if (!onPath[v]) {
                prev[v] = u;
                if (dls(v, goal, depth + 1, limit, graph, onPath, prev)) return true;
            }
        }
        onPath[u] = false;
        return false;
    }

    static List<Integer> iddfsPath(List<List<Integer>> graph, int start, int goal, int maxDepth) {
        int n = graph.size();
        for (int limit = 0; limit <= maxDepth; limit++) {
            boolean[] onPath = new boolean[n];
            int[] prev = new int[n];
            Arrays.fill(prev, -1);
            if (dls(start, goal, 0, limit, graph, onPath, prev)) {
                List<Integer> path = new ArrayList<>();
                for (int at = goal; at != -1; at = prev[at]) path.add(at);
                Collections.reverse(path);
                return path;
            }
        }
        return Collections.emptyList();
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
        int maxDepth = 5;
        List<Integer> path = iddfsPath(graph, start, goal, maxDepth);
        if (path.isEmpty()) {
            System.out.println("No path within max depth " + maxDepth);
            return;
        }

        System.out.print("IDDFS Path: ");
        for (int i = 0; i < path.size(); i++) {
            if (i > 0) System.out.print(" -> ");
            System.out.print(path.get(i));
        }
        System.out.println();
    }
}
