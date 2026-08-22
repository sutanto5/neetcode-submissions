class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first integer of every row is greater than last of previous row


        # binary seach the first index of each row
        start_row = 0
        end_row = len(matrix) - 1

        likely_row = 0

        while end_row >= start_row:
            # starting row index
            mid = start_row + (end_row - start_row) // 2

            print(mid)
            curr_row_start = matrix[mid][0]
            curr_row_end = matrix[mid][-1]

            #target is within the row
            if curr_row_start <= target and curr_row_end >= target:
                likely_row = mid
                break
            
            #target is less than start of current row
            elif curr_row_start > target:
                end_row = mid - 1
            
            #target is greater than current row
            else:
                start_row = mid + 1


        # row is found now binary search row
        
        target_row = matrix[likely_row]
        print(target_row)

        start = 0
        end= len(target_row) - 1

        if target_row[end] == target or target_row[start] == target:
            return True

        while end >= start:

            print(end)
            print(start)
            # end row index
            mid = start + (end - start) // 2

            curr = target_row[mid]

            #target is within the row
            if curr == target:
                return True
            
            #target is less than start of current row
            elif curr > target:
                end = mid - 1
            
            #target is greater than current row
            else:
                start = mid + 1

        return False


        # binary search the most likely inluded row
       