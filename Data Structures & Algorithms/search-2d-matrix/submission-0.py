class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        #binary search -> split the row into uper half and lower half until base case
        
        print(matrix)

        #if rows in matrix == 1
        if len(matrix) == 1:
            #search for num
            
            for num in matrix[0]:
                print(num)
                if target == num:
                    return True 
            
            #doenst exist in row
            return False
        
        #splice matrix
        else:
            split = math.ceil(len(matrix)/2)

            #if the first eelment in the row
            if matrix[split][0] > target:
                #go with the bottom half
                return self.searchMatrix(matrix[0:split], target)
            else:
                return self.searchMatrix(matrix[split:], target)
            
        return False
