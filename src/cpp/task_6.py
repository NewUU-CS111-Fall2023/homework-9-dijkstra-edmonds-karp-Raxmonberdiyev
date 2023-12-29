/*
 * Author:Raximberdi
 * Date:
 */

from collections import deque
from heapq import heappush, heappop

def find_shortest_path(n, flights, src, dst, k, f):
 graph = defaultdict(list)
 for u, v, d, ars in flights:
  graph[u].append((v, d, ars))

 # (distance, node, stops, fuel)
 heap = [(0, src, -1, f)]
 visited = defaultdict(lambda: defaultdict(lambda: float('inf')))

 while heap:
  dist, node, stops, fuel = heappop(heap)
  if node == dst:
   return dist
  if node in visited and stops in visited[node] and visited[node][stops] <= fuel:
   continue
  visited[node][stops] = fuel
  if stops < k:
   for v, d, ars in graph[node]:
    extra_fuel = f if ars else 0
    if fuel >= d:
     heappush(heap, (dist + d, v, stops + 1, fuel - d + extra_fuel))

 return -1
