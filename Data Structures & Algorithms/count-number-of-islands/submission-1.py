class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numIslands = 0
        
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        #set of tuples with every position
        visited = set()
        
        
        
        def scopeIsland(coord):
            nonlocal visited
            
            row, col = coord
            #check if isited already
            #check up
            if row != 0 and grid[row - 1][col] == '1' and (row -1, col) not in visited:
                visited.add((row - 1, col))
                scopeIsland((row-1, col))

            #check down
            if row != rows - 1 and grid[row + 1][col] == '1' and (row + 1, col) not in visited:
                visited.add((row + 1, col))
                scopeIsland((row + 1, col))

            #check left
            if col != 0 and grid[row][col - 1] == '1' and (row, col - 1) not in visited:
                visited.add((row, col - 1))
                scopeIsland((row, col - 1))

            #check right
            if col != cols - 1 and grid[row][col + 1] == '1' and (row, col + 1) not in visited:
                visited.add((row, col + 1))
                scopeIsland((row, col + 1))



        for i in range(0, rows):
            for j in range(0, cols):
                coord = (i, j)
                if coord not in visited and grid[i][j] == '1':
                    #we've found an island:
                    numIslands = numIslands + 1
                    visited.add(coord)
                    scopeIsland(coord)
        

        return numIslands