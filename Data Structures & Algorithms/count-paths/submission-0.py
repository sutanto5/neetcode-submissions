class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #top left is always start value

        #create the grid
        
        target_x = m - 1
        target_y = n - 1

        ways = 0
        
        def dfs(x, y):
            nonlocal ways 

            if x >= m or y >= n:
                return
            
            if x == target_x and y == target_y:
                ways = ways + 1
                return
            
            else:
                dfs(x+1, y)
                dfs(x, y + 1)
        
        dfs(0, 0)
        return ways
