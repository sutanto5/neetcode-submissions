class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        freq = {}
        orig_count = Counter(nums)
        nums.sort()
        


        def backtrack(index, arr):
         
            if index == len(nums):
                res.append(arr[:])
                return
            
            curr = nums[index]
            prev = nums[index - 1] if index > 0 else -math.inf

            
            
            arr.append(curr)
            backtrack(index + 1, arr)
            arr.pop()

            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
            
            backtrack(index + 1, arr)
            
          

            

        backtrack(0, [])

        return res
            