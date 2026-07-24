class Solution:
     def twoSum(self, nums: List[int], target: int) -> List[int]:
          # { value: index }
          nepo = {}

          for (i,num) in enumerate(nums):

               complement = target - num
               
               if complement not in nepo:
                    nepo.update({num: i})
               else:
                    return ([nepo[complement], i])
          
          return [0,0]


          