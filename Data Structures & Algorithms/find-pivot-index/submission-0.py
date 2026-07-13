class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        

        # [ 1, 7, 3, 6, 5, 6]

        # prefix sum [ [1, 8, 11,]17, [22, 28] ]

        # Brute Force:

        # go through every index and calculate sum of left and right

        #

        # 1. find the cumulative sum at every point

        # 2. go through every index and find the 

        pre = [0] * len(nums)

        pre[0] = nums[0]

        length = len(nums) - 1

        for i in range(1, len(nums)):
            pre[i] = pre[i - 1] + nums[i]

        for i in range(0, len(nums)):
            if i == 0 and pre[length] - pre[0] == 0:
                return 0
            
            if pre[i - 1] == pre[length] - pre[i]:
                return i

        return -1