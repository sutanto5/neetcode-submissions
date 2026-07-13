class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #the double for loop
            #space complexity: O(1)
            #time complexity: O(n**2)

        #use a set -> if length of set is equivalent to length of arr
        #O(n) time complexity
        set_nums = set(nums)

        return not len(set_nums) == len(nums)

