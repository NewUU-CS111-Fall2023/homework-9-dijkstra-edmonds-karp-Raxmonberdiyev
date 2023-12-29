/*
 * Author:
 * Date:
 * Name:
 */

import java.util.*;

class Node {
    int cap;
    int flow;
}

public class Main {
    static int bfs(HashMap<Integer, HashMap<Integer, Node>> graph, int s, int t, int[] pred) {
        Queue<Integer> queue = new LinkedList<>();
        Set<Integer> visited = new HashSet<>();
        queue.add(s);
        visited.add(s);
        pred[s] = -1;

        while (!queue.isEmpty()) {
            int u = queue.poll();
            for (int v : graph.get(u).keySet()) {
                if (!visited.contains(v) && graph.get(u).get(v).cap - graph.get(u).get(v).flow > 0) {
                    visited.add(v);
                    pred[v] = u;
                    queue.add(v);
                }
            }
        }

        return pred[t] != -1 ? 1 : 0;
    }

    static int edmondsKarp(HashMap<Integer, HashMap<Integer, Node>> graph, int s, int t) {
        int flow = 0;
        int[] pred = new int[graph.size()];

        while (bfs(graph, s, t, pred) == 1) {
            int f = Integer.MAX_VALUE;
            int v = t;
            while (v != s) {
                f = Math.min(f, graph.get(pred[v]).get(v).cap - graph.get(pred[v]).get(v).flow);
                v = pred[v];
            }

            flow += f;
            v = t;
            while (v != s) {
                int u = pred[v];
                graph.get(u).get(v).flow += f;
                graph.get(v).get(u).flow -= f;
                v = pred[v];
            }
        }

        return flow;
    }

    public static void main(String[] args) {
        // Your code here
    }
}
