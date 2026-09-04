import heapq

class Solution:
    def minimumEffortPath(self, heights):

        rows = len(heights)
        cols = len(heights[0])

        
        effort = [[float('inf')] * cols for _ in range(rows)]

        
        effort[0][0] = 0

        
        heap = [(0, 0, 0)]

        directions = [
            (1, 0),    # down
            (-1, 0),   # up
            (0, 1),    # right
            (0, -1)    # left
        ]

        while heap:

            current_effort, r, c = heapq.heappop(heap)

           
            if r == rows - 1 and c == cols - 1:
                return current_effort

            
            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                
                if 0 <= nr < rows and 0 <= nc < cols:

                    
                    difference = abs(
                        heights[r][c] - heights[nr][nc]
                    )

                    
                    new_effort = max(
                        current_effort,
                        difference
                    )

                    
                    if new_effort < effort[nr][nc]:

                        effort[nr][nc] = new_effort

                        heapq.heappush(
                            heap,
                            (new_effort, nr, nc)
                        )

        return 0