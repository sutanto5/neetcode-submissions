class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #we need a way to traverse islands
        #need a way to track what we've visited so far
        #we need some way to keep track of the max area of an island
        maxArea = 0
        currArea = 0
        visited = set()


        #scope out the island (bfs)
        def scopeIsland(coord):
            nonlocal visited
            nonlocal currArea

            row, col = coord
            
            #check right
            if col < cols - 1 and (row, col+1) not in visited and grid[row][col + 1]== 1:
                #increment area counter
                currArea = currArea + 1
                #check off square
                visited.add((row, col + 1))
                #recurse
                scopeIsland((row, col+1))

            #check left
            if col > 0 and (row, col - 1) not in visited and grid[row][col - 1]== 1:
                #increment area counter
                currArea = currArea + 1
                #check off square
                visited.add((row, col - 1))
                #recurse
                scopeIsland((row, col-1))

            #check up
            if row > 0 and (row -1, col) not in visited and grid[row - 1][col]== 1:
                #increment area counter
                currArea = currArea + 1
                #check off square
                visited.add((row - 1, col))
                #recurse
                scopeIsland((row - 1,  col))


            #check down
            if row < rows-1 and (row + 1, col) not in visited and grid[row + 1][col]== 1:
                #increment area counter
                currArea = currArea + 1
                #check off square
                visited.add((row + 1, col))
                #recurse
                scopeIsland((row + 1,  col))

        #double for loop going through each node of the grid
            #if the cell is a 1 and its not already visited
                #then that indicates a new island
        
        rows = len(grid)
        cols = len(grid[0])

        #go through each cell of the grid

        for i in range(0, rows):
            for j in range(0, cols):

                coord = (i, j)

                if coord not in visited and grid[i][j] == 1:
                    currArea = 1

                    visited.add(coord)
                    scopeIsland(coord)

                    maxArea = max(currArea, maxArea)
                    #reset area counter
                    currArea = 0

        return maxArea




