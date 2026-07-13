class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        max_ind = 0

        for i in range(0, len(nums)):
            #if i < max_ind
            if i > max_ind:
                #means you can't reach that i with your jumps available
                return False
            
            max_ind = max(nums[i] + i, max_ind)
        
        return True

        
