class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def recurse(arr, index):
            nonlocal res
            if index >= len(nums):
                res.append(arr[:])
                return

            arr.append(nums[index])
            recurse(arr[:], index + 1)
            arr.pop()
            recurse(arr[:], index + 1)
        
        
        recurse([], 0)

        return res
