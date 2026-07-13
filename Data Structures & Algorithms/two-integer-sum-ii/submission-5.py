class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #Hash Map/Dict: Key -> index, and the number is the Value 
        #Hash lookup is O(1) -> We only need to go through the array once

        #We subtract our number from our target
        #We want to look up the number in the hash

        #dict storing seen nums {index: number}
        seenNums = {}

        #enumerate we can get both index and the curr number
        for i, num in enumerate(numbers):
            diff = target - num

            #if diff exists in seen -> Then soln
            #.get uses the key as the lookup not the val
            lookup = seenNums.get(diff)
           
            if lookup == None:
                seenNums.update({num:i})
            else:
                #diff exists
                return list([lookup + 1, i + 1])
        
        return None




