class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr_subset = []

        def dfs(i):
            #for each number we can decided to include it or not include it
            if i >= len(nums):
                res.append(curr_subset[:])
                return
            #include
            curr_subset.append(nums[i])
            #run where it is
            dfs(i+1)

            #not include
            curr_subset.pop()
            #dfs -> run the scenario where this isn't included
            dfs(i+1)

        dfs(0)
        return res