class Solution:
    def jump(self, nums: List[int]) -> int:

        #goal 
        target = len(nums) - 1
        
        jumps = 0

        #valid answer

        #represent the window of possible outcomes
        first = 0
        last = 0

        #likely looking for an O(n)
        while last < target:
            maximum = 0
            for i in range(first, last + 1):

                #farthest value you can get of the stuff in the range
                maximum = max(maximum, i + nums[i])
                
            first = last
            last = maximum
            

            jumps = jumps + 1
                

        return jumps
    
        
