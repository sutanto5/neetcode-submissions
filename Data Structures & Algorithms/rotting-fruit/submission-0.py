class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        freshFruit = 0
        queue = []
        time = 0
        height = len(grid[0])
        width = len(grid)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    freshFruit = freshFruit + 1
                elif grid[i][j] == 2:
                    queue.append((i,j))
                
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while freshFruit > 0 and len(queue) != 0:
            length = len(queue)
            for i in range(length):
                x, y = queue[0]
            
                #remove from queue
                queue = queue[1:]

                # for every direction

                for dr, dc in directions:
                    row, col = x + dr, y + dc
                    #if the grid is in range and is a banana
                    if (row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        queue.append((row, col))
                        freshFruit -= 1
            time +=1
        return time if freshFruit == 0 else -1