class Solution:
    #nums -> unique
    def permute(self, nums: List[int]) -> List[List[int]]:
        

        if len(nums) == 0:
            return []



        lengthOrig = len(nums)
        res = []
        arr = []
        def dfs(arr):
            nonlocal res
            
            #blank array: 
            if len(arr) == lengthOrig:
                res.append(arr[:])
                return 

            for num in nums:
                if num not in arr:
                    arr.append(num)
                    dfs(arr)
                    #after we've dfs we want to get rid of the variable
                    arr.pop()
        dfs(arr)
        return res


            

