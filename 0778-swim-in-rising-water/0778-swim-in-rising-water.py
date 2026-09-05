import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        minHeap = [(grid[0][0], 0, 0)]
        visited = set()
        visited.add((0, 0))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        time = 0

        while minHeap:
            height, row, col = heapq.heappop(minHeap)

            time = max(time, height)

            if row == n - 1 and col == n - 1:
                return time

            for dr, dc in directions:
                newRow = row + dr
                newCol = col + dc

                if (0 <= newRow < n and
                    0 <= newCol < n and
                    (newRow, newCol) not in visited):

                    visited.add((newRow, newCol))

                    heapq.heappush(
                        minHeap,
                        (grid[newRow][newCol], newRow, newCol)
                    )