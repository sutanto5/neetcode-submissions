class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #store all possibiliites
        res = []

        #current sub -> 2, 2, 5 ex.
        current = []


        #go through every possible array and see if it equals target
        def dfs(currSum):

            #sum of current = target
            
            if currSum == target:
                ordered = sorted(current)
                if ordered not in res:
                    res.append(ordered[:])
                    return
            elif currSum > target:
                return
            
            for num in nums:
                current.append(num)
                dfs(currSum + num)
                current.pop()

        dfs(0)
        return res