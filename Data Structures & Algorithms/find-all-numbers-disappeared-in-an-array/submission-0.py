class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        target_nums = []

        for i in range(1, n+1):
            target_nums.append(i)

        for num in nums:
            if num in target_nums:
                target_nums.remove(num)
        
        return target_nums