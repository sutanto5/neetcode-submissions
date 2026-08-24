class Solution:
    def search(self, nums: List[int], target: int) -> int:

        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            
            mid = (lo + hi) // 2   
            
        
            # check for target
            if nums[mid] == target:
                
                return mid
            
           # figure out which half is sorted
            if nums[lo] <= nums[mid]:

                # is it within the sorted range
                if nums[lo] <= target <= nums[mid]:
                    hi = mid - 1

                else:
                    lo = mid + 1
            
            else:
                if nums[hi] >= target >= nums[mid]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            

        return -1