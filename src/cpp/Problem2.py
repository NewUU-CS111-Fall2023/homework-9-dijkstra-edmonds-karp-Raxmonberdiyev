
from collections import deque

class Edge:
    def __init__(self, t, rev, cap):
        self.t = t
        self.rev = rev
        self.cap = cap
        self.f = 0

def add_edge(graph, s, t, cap):
    a = Edge(t, len(graph[t]), cap)
    b = Edge(s, len(graph[s]), 0)
    a.rev = b
    b.rev = a
    graph[s].append(a)
    graph[t].append(b)

def bfs(graph, s, t, pred):
    for i in range(len(graph)):
        pred[i] = -1
    pred[s] = -2
    q = deque()
    q.append(s)

    while q:
        cur = q.popleft()
        for e in graph[cur]:
            if e.cap - e.f > 0 and pred[e.t] == -1:
                pred[e.t] = e
                if e.t == t:
                    return True
                q.append(e.t)
    return False

def max_flow(graph, s, t):
    flow = 0
    pred = [0]*len(graph)
    while bfs(graph, s, t, pred):
        df = float('inf')
        cur = t
        while cur != s:
            df = min(df, pred[cur].cap - pred[cur].f)
            cur = pred[cur].rev.t
        flow += df
        cur = t
        while cur != s:
            pred[cur].f += df
            pred[cur].rev.f -= df
            cur = pred[cur].rev.t
    return flow
