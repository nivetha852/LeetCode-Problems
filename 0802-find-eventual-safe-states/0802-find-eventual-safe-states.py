from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)

        reverse = [[] for _ in range(n)]
        outdegree = [0] * n

        
        for i in range(n):
            outdegree[i] = len(graph[i])

            for neighbor in graph[i]:
                reverse[neighbor].append(i)

        
        queue = []

        for i in range(n):
            if outdegree[i] == 0:
                queue.append(i)

        safe = []

        
        while queue:
            node = queue.pop(0)
            safe.append(node)

            for prev in reverse[node]:
                outdegree[prev] -= 1

                if outdegree[prev] == 0:
                    queue.append(prev)

        return sorted(safe)   