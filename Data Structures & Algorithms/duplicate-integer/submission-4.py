class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # empty array

        # invalid array
        return len(set(nums)) != len(nums)