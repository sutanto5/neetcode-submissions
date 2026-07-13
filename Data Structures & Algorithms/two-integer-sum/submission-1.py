class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
     seen_nums = {}   # { num : index }

     for i, n in enumerate(nums):
          difference = target - n
          if seen_nums.get(difference) != None:
               return [seen_nums[difference], i]
          else:
               seen_nums[n] = i
          
     return 