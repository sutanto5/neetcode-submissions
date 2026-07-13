class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #non empty so dont need to check null

        #return the int that appears once

        #O(n) go through every element and use a hash set -> Compare to see if element exists
        #However takes O(n) space
        seen = set()

        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                seen.remove(num)
        
        return list(seen).pop()
        
