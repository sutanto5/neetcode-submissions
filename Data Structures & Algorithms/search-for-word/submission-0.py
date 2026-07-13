class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        height = len(board)          # number of rows
        width = len(board[0])        # number of cols

        def search(x: int, y: int, currLetter: int) -> bool:
            nonlocal checked

            # current cell must match current letter
            if board[x][y] != word[currLetter]:
                return False

            # if we've matched the last letter, success
            if currLetter == len(word) - 1:
                return True

            # mark visited
            checked.add((x, y))

            nextLetter = currLetter + 1

            # up
            if x - 1 >= 0 and (x - 1, y) not in checked:
                if search(x - 1, y, nextLetter):
                    checked.remove((x, y))
                    return True

            # down
            if x + 1 < height and (x + 1, y) not in checked:
                if search(x + 1, y, nextLetter):
                    checked.remove((x, y))
                    return True

            # left
            if y - 1 >= 0 and (x, y - 1) not in checked:
                if search(x, y - 1, nextLetter):
                    checked.remove((x, y))
                    return True

            # right
            if y + 1 < width and (x, y + 1) not in checked:
                if search(x, y + 1, nextLetter):
                    checked.remove((x, y))
                    return True

            # backtrack
            checked.remove((x, y))
            return False

        for i in range(height):
            for j in range(width):
                if board[i][j] == word[0]:
                    checked = set()
                    if search(i, j, 0):
                        return True

        return False