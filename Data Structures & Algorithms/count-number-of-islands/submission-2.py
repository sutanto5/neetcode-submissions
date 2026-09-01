class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # notes: - not diagnoal
        # - don't need to account for empty arrays
        # - can asume its only 1s and 0s in the graph as well

        # for loop running through every node
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        island_count = 0

        # island check -> want to make sure we dont go over the same nodes again
        def dfs(x, y):
            nonlocal visited

            visited.add((x,y))

            # up
            
            # check bounds
            if x - 1 > -1 and (x-1, y) not in visited and grid[x-1][y] == '1':
                dfs(x-1, y)

            # left
            if y-1 > -1 and (x, y-1) not in visited and grid[x][y-1] == '1':
                dfs(x, y-1)

            # right
            if y + 1 < cols and (x, y+1) not in visited and grid[x][y+1] == '1':
                dfs(x, y+1)

            # down
            if x + 1 < rows and (x+1, y) not in visited and grid[x+1][y] == '1':
                dfs(x+1, y)

            
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited:
                    if grid[i][j] == '1':
                        island_count += 1
                        dfs(i, j)
                    else:
                        visited.add((i,j))

        return island_count
               
                   


