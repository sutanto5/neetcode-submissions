class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #We are not given that the array is sorted
        #If sorting -> O(n* log n)

        #my Soln:
          
            #2. Run through array once to put in a hash map O(n)
            #3. Compare every possible sum O(n^2) -> append triples
      
        #contains all values of arr -> O(1) lookup time
        seen = {}
        res = set()

        #add num to s
        #utilizing hash map/dict {num: freq}
        for num in nums:
            freq = seen.get(num)
            if freq != None:
                freq = freq + 1
                seen[num] = freq
            else:
                seen.update({num:1})

        #check for triples
        for i, num1 in enumerate(nums):
            for j in range(i+1, len(nums)):
                num2 = nums[j]

                target = -num2 - num1

                #check if a triple combo makes it 0
                if target in seen:
                    
                    #check for duplicate
                    if target == num2 or target == num1:
                        #check if the num has a freq greater than 1
                        if seen.get(target) == 2 and target != 0:

                            sort = sorted([num1, num2, target])
                            res.add((sort[0], sort[1], sort[2]))

                        if seen.get(target) >= 3 and target == 0:
                            res.add((0,0,0))

                        
                        
                    else:
                        sort = sorted([num1, num2, target])
                        res.add((sort[0], sort[1], sort[2]))

                    
        
        return list(res)
        