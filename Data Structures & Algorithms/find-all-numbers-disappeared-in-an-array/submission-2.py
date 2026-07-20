class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        for num in nums:
            pos_num = abs(num)

            if nums[pos_num - 1] > 0:
                nums[pos_num-1] = -(nums[pos_num-1])

           
        
        sol = []
        for i, num in enumerate(nums):
            
            if num > 0:
                sol.append(i + 1)

        return sol


