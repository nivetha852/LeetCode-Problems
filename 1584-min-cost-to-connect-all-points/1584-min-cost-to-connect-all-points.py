class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)
        edges = []

        # Create all possible edges
        for i in range(n):
            for j in range(i + 1, n):
                cost = abs(points[i][0] - points[j][0]) + \
                       abs(points[i][1] - points[j][1])
                edges.append((cost, i, j))

        # Sort edges based on cost
        edges.sort()

        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            rootA = find(a)
            rootB = find(b)

            if rootA == rootB:
                return False

            parent[rootB] = rootA
            return True

        totalCost = 0
        edgesUsed = 0

        for cost, u, v in edges:
            if union(u, v):
                totalCost += cost
                edgesUsed += 1

                if edgesUsed == n - 1:
                    break

        return totalCost