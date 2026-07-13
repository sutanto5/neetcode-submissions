class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #double for loop -> O(n)
        prevMap = {} # val: index



        #run through each

        #enumerate adds a counter to a list/array and returns a tuple
        for i, n in enumerate(nums):
            diff = target - n

            if diff in prevMap:
                return [prevMap[diff],i]
            
            prevMap[n] = i

        return 
