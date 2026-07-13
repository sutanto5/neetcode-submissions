class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)
        
        middle = (start + end) // 2

        while start != end:
            if nums[middle] == target:
                return middle
            elif target < nums[middle]:
                end = middle
            else:
                start = middle + 1

            middle = (start + end) // 2
            
        return -1
            