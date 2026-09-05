import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = {}

        for u, v, w in times:
            if u not in graph:
                graph[u] = []
            graph[u].append((v, w))

        minHeap = [(0, k)]
        visited = set()
        time = 0

        while minHeap:
            t, node = heapq.heappop(minHeap)

            if node in visited:
                continue

            visited.add(node)
            time = t

            for neighbor, weight in graph.get(node, []):
                if neighbor not in visited:
                    heapq.heappush(minHeap, (t + weight, neighbor))

        return time if len(visited) == n else -1