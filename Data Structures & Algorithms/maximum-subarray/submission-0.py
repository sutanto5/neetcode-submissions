class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #track of current
        curr = 0
        #track of. max
        maximum = float("-inf")

        #run through each var
        for num in nums:
            print(curr)
            curr = max(curr + num, num)

            maximum = max(maximum, curr)

        return maximum


        
        

