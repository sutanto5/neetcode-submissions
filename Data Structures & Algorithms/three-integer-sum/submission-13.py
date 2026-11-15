class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        nums.sort()

        for i in range(0, len(nums) - 2):

            if i > 0 and nums[i - 1] == nums[i]:
                continue
            
            l, r = i + 1, len(nums) - 1

            while l < r:

                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l = l + 1

                    while l < r and nums[l] == nums[l - 1]:
                        l = l + 1

                    r = r - 1

                    while r > l and nums[r] == nums[r + 1]:
                        r = r - 1
                    
                elif total > 0:
                    r = r - 1
                else:
                    l = l + 1
            
            
        
        return res
