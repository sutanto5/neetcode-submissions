class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        curr_area = 0
        max_area = 0

        visited = set()

        # in: coord -> tuple (x,y)
        def dfs(coord):
            nonlocal curr_area
            nonlocal visited

            visited.add(coord)
            curr_area+=1

            row = coord[0]
            col = coord[1]

            # up
            if row-1 >= 0 and (row - 1, col) not in visited and grid[row-1][col] == 1:
                dfs((row-1, col))
            # down
            if row+1 < rows and (row + 1, col) not in visited and grid[row+1][col] == 1:
                dfs((row+1, col))
            # left
            if col > 0 and (row, col-1) not in visited and grid[row][col - 1] == 1:
                dfs((row, col-1))
            # right
            if col < cols - 1 and (row, col+1) not in visited and grid[row][col + 1]== 1:
                dfs((row, col+1))
        

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in visited:
                    dfs((i,j))
                    max_area = max(max_area, curr_area)
                    curr_area = 0
        
        return max_area

                   
