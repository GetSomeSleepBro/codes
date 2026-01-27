import java.util.*;

public class java_BidirectionalSearch {
    static List<Integer> buildPath(int meet, int[] parentA, int[] parentB) {
        List<Integer> left = new ArrayList<>();
        for (int at = meet; at != -1; at = parentA[at]) left.add(at);
        Collections.reverse(left); // start -> meet

        List<Integer> right = new ArrayList<>();
        for (int at = parentB[meet]; at != -1; at = parentB[at]) right.add(at); // meet -> goal (excluding meet)

        left.addAll(right);
        return left;
    }

    static List<Integer> bidirPath(List<List<Integer>> graph, int start, int goal) {
        int n = graph.size();
        boolean[] visA = new boolean[n];
        boolean[] visB = new boolean[n];
        int[] parentA = new int[n];
        int[] parentB = new int[n];
        Arrays.fill(parentA, -1);
        Arrays.fill(parentB, -1);

        Queue<Integer> qa = new ArrayDeque<>();
        Queue<Integer> qb = new ArrayDeque<>();
        visA[start] = true;
        visB[goal] = true;
        qa.add(start);
        qb.add(goal);

        while (!qa.isEmpty() && !qb.isEmpty()) {
            int szA = qa.size();
            while (szA-- > 0) {
                int u = qa.remove();
                if (visB[u]) return buildPath(u, parentA, parentB);
                for (int v : graph.get(u)) {
                    if (!visA[v]) {
                        visA[v] = true;
                        parentA[v] = u;
                        qa.add(v);
                    }
                }
            }

            int szB = qb.size();
            while (szB-- > 0) {
                int u = qb.remove();
                if (visA[u]) return buildPath(u, parentA, parentB);
                for (int v : graph.get(u)) {
                    if (!visB[v]) {
                        visB[v] = true;
                        parentB[v] = u;
                        qb.add(v);
                    }
                }
            }
        }

        return Collections.emptyList();
    }

    public static void main(String[] args) {
        // Undirected graph (so bidirectional search is simple)
        List<List<Integer>> graph = Arrays.asList(
                Arrays.asList(1, 2),       // 0
                Arrays.asList(0, 3, 4),    // 1
                Arrays.asList(0, 5),       // 2
                Arrays.asList(1, 6),       // 3
                Arrays.asList(1, 6),       // 4
                Arrays.asList(2, 6),       // 5
                Arrays.asList(3, 4, 5)     // 6
        );

        int start = 0, goal = 6;
        List<Integer> path = bidirPath(graph, start, goal);
        if (path.isEmpty()) {
            System.out.println("No path");
            return;
        }

        System.out.print("Bidirectional Path: ");
        for (int i = 0; i < path.size(); i++) {
            if (i > 0) System.out.print(" -> ");
            System.out.print(path.get(i));
        }
        System.out.println();
    }
}

