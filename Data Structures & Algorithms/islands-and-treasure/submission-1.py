class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = []
        visited = set()
        width = len(grid)
        height = len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i,j))
        
        while len(queue) != 0:
            x,y = queue[0]

            #mark as visited
            visited.add((x,y))

            #remove from queue
            queue = queue[1:]

            # add neighbors

            #check up
            if y+1 < height and grid[x][y+1] == 2147483647:
                grid[x][y+1] = grid[x][y] + 1
                visited.add((x,y+1))
                queue.append((x,y+1))

            #check right
            if x+1 < width and grid[x+1][y] == 2147483647:
                grid[x+1][y] = grid[x][y] + 1
                visited.add((x+1,y))
                queue.append((x+1,y))

            #check left
            if x-1 > -1 and grid[x-1][y] == 2147483647:
                grid[x-1][y] = grid[x][y] + 1
                visited.add((x-1,y))
                queue.append((x-1,y))


            #check down
            if y-1 > -1 and grid[x][y-1] == 2147483647:
                grid[x][y-1] = grid[x][y] + 1
                visited.add((x,y-1))
                queue.append((x,y-1))
        

