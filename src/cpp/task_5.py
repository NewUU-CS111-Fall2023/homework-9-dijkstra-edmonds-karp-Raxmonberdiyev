import heapq
from collections import defaultdict

def find_cheapest_price(n, flights, src, dst, K):
    graph = defaultdict(list)
    for u, v, w in flights:
        graph[u].append((v, w))

    min_heap = [(0, src, K+1)]  # price, city, remaining stops
    while min_heap:
        price, city, stops = heapq.heappop(min_heap)
        if city == dst:
            return price
        if stops > 0:
            for v, p in graph[city]:
                heapq.heappush(min_heap, (price+p, v, stops-1))

    return -1
