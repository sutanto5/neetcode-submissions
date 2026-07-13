class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #return all possible subsets of nums

        #results array [[]]
        res = [[]]

        seen = set()

        arr = []

        #dfs
        def backtrack():

            #siginifies branch is already full
            if len(arr) == len(nums):
                return

            for num in nums:
                
                if num not in arr:
                    #add new subset
                    arr.append(num)
                    #add to subet tracker
                    if sorted(arr) not in res:
                        res.append(sorted(arr[:]))
                    #we have a new arr
                    backtrack()
                    arr.pop()

        backtrack()
        return res
