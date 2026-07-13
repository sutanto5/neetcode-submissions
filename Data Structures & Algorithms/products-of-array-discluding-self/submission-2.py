class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # output --> where output[i] = nums -> nums[i]


        # zeroes -> if one zero then ooutput total
        zeroes = 0

        # if two zeroes output zero for whole array
        total = 1

        for i in range(len(nums)):
            if nums[i] == 0:
                zeroes = zeroes + 1

                if zeroes >= 2:
                    total = 0

            else:
                total = total * nums[i]

        output = []
        for i in range(len(nums)): 
            if zeroes > 0:
                if nums[i] == 0:
                    output.append(total)
                else:
                    output.append(0)
            else:
                output.append(int(total / nums[i]))
            
        return output
                
            

        