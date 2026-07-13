class Solution:
    def rob(self, nums: List[int]) -> int:

        #edge cases -> len = 0, 1, 2, 3
        houses = len(nums)

        if houses == 0:
            return 0
        elif houses == 1:
            return nums[0]
        elif houses == 2:
            return max(nums[0], nums[1])
        elif houses == 3:
            return max(nums[0] + nums[2], nums[1])

        #max amount of money taht is able to be robbed at each house
        #base case -> 0, 1, 2
        robbed = [nums[0], nums[1], nums[2] + nums[0]]
        print(robbed)

        #we want to calculate at each posisble location starting from 0, 1
        maximum = max(robbed[0], robbed[1], robbed[2]) #value is our baseline

        #find which one has max value -> tabulation
        for i in range(3, houses):
            print(maximum)
            
            money = nums[i] + max(robbed[i-2], robbed[i-3])
            print(money)
            maximum = max(money, maximum)
            robbed.append(money)

        return maximum
        