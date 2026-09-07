class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        old = image[sr][sc]

        if old == color:
            return image

        def dfs(r, c):

            
            if r < 0 or r >= len(image):
                return

            if c < 0 or c >= len(image[0]):
                return

           
            if image[r][c] != old:
                return

            image[r][c] = color

            
            dfs(r - 1, c)

            
            dfs(r + 1, c)

           
            dfs(r, c - 1)

            
            dfs(r, c + 1)

        dfs(sr, sc)

        return image