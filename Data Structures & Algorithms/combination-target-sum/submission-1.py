class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        

        def backtrack(start, currSum, subset):
            if currSum == target:
                res.append(subset[:])
                return

            if currSum > target:
                return

            # 2, 2, 2, 2, 2, 2, 2... O(n/t/m)
            for i in range(start, len(nums)):
                num = nums[i]

                subset.append(num)
                backtrack(i, currSum + num, subset)
                subset.pop()
                
        
        backtrack(0, 0, [])
        return res

            

                    

                

