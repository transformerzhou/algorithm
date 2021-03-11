from heapq import *


#Cruskal算法
def minCostConnectPoints(points) -> int:
    n = len(points)
    father = list(range(n))

    def find(x):
        if x != father[x]:
            father[x] = find(father[x])
        return father[x]

    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
            edges.append([dist, i, j])

    n_edges = 0
    ans = 0

    heapify(edges)
    while (n_edges < n - 1):
        a, b, c = heappop(edges)
        if find(b) != find(c):
            ans += a
            n_edges += 1
            father[find(b)] = father[c]
    return ans

#prim算法