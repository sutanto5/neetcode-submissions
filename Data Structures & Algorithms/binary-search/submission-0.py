import math

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #sorted

        #O(n) -> run one through for loop but this algorithm would be in O(n) time

        #binary search -> splits the array in half till target is found or len() = 1

        #while loop

        #or

        # using recursion

        #I'm gonna use a while loop -> Takes up less space on the stack


        #find the middle of the array
        first = 0
        last = len(nums) - 1
        
        #last element is still greater than the first element
        while last >= first:

            #middle
            mid = first + (last - first) // 2
            print(mid)
            print("first: " + str(first))
            print("last:" + str(last))

            curr = nums[mid]

            
            if curr == target:
                return mid
            elif curr < target:
                first = mid + 1
            else:
                last = mid - 1

        return -1

        