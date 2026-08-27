class Solution:
    def rob(self, nums: List[int]) -> int:
        # dynamic programming
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        elif len(nums) == 3:
            return max(nums[0] + nums[2], nums[1])
       
        max_money = [nums[0], nums[1], nums[0] + nums[2]]

        for i in range(3, len(nums)):
            money_robbed = nums[i] + max(max_money[i - 2], max_money[i - 3])
            max_money.append(money_robbed)

        print(max_money)
        return max(max_money[-1], max_money[-2])

