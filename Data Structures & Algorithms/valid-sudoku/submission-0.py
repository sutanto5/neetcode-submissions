class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #O(n^2) -> Check Rows
        for row in board:
            print(row)
            seen = set()
            for val in row:
                if val in seen:
                    return False
                if val != '.':
                    seen.add(val)

        
        #O(n^2) -> Check Cols
        for i in range(0, 9):
            seen = set()
            for j in range(0, 9):
                val = board[j][i]
                if val in seen:
                    return False
                if val != '.':
                    seen.add(val)
        
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        
        return True
        

        