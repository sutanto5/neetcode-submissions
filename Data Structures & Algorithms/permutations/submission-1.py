class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        length = len(nums)

        def dfs(arr):
            nonlocal length 
            if len(arr) == length:
                res.append(arr[:])
                return

            for num in nums:
                if num not in arr:
                    arr.append(num)
                    dfs(arr)
                    arr.pop()

        dfs([])
        return res
        

            