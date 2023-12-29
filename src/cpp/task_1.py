unvisited = {"S", "a", "b", "c", "d", "e"}
visited = {}
P = {}
d = {}

# Creating parent node
P["S"] = None
P["a"] = None
P["b"] = None
P["c"] = None
P["d"] = None
P["e"] = None

# Distance of S and setting infinity to other verteces
d["S"] = 0
d["a"] = float("inf")
d["b"] = float("inf")
d["c"] = float("inf")
d["d"] = float("inf")
d["e"] = float("inf")

# finding the shortest path to each vertex
d["S"] += 1
d["a"] = 1
P["a"] = "S"

d["S"] += 5
d["b"] = 5
P["b"] = "S"

unvisited = {"a", "b", "c", "d", "e"}
visited = {"S"}

d["a"] += 2
d["c"] = 3
P["c"] = "a"

d["a"] += 1
d["d"] = 2
P["d"] = "a"

d["a"] += 2
d["d"] = 3
P["d"] = "a"

unvisited = {"b", "c", "d", "e"}
visited = {"S","a"}


d["d"] += 2
d["e"] = 4
P["d"] = "d"

unvisited = {"b", "c", "e"}
visited = {"S", "a", "d"}

d["b"] += 2
unvisited = {"c", "e"}
visited = {"S", "a", "d", "b"}

d["c"] += 1
unvisited = {"e"}
visited = {"S", "a", "d", "b", "c"}

unvisited = {}
visited = {"S", "a", "d", "b", "c", "e"}

/*
 * Author:
 * Date:
 * Name:
 */

class Problem1 {
public:
};