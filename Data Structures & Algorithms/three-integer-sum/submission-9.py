class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # O(nlogn)
        nums_sorted = sorted(nums)
        
        # pivot
        i = 0

        # triplets = 0
        sols = set()

        while i < len(nums) - 2:
            l, r, = i+1, len(nums_sorted) - 1
            while l < r:
                total = nums_sorted[i] + nums_sorted[l] + nums_sorted[r]
                if total == 0:
                    sols.add((nums_sorted[i], nums_sorted[l], nums_sorted[r]))
                    l += 1
                    r -=1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
            
            i += 1
            

        return list(sols)
