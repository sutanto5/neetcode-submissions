class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(index):
            if index >= len(nums):
                return
            
            #append
            subset.append(nums[index])
            res.append(subset[:])
            #recurse 
            dfs(index+1)
            subset.remove(nums[index])
            dfs(index + 1)

            

        dfs(0)
        res.append([])
        return res
        
