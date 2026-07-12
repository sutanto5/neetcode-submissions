class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        #first and last ind
        l, r = 0, len(numbers) -1
        

        while l < r:
            print(l)
            print(r)
            total = numbers[r] + numbers[l]
            if total == target:
                return [l+1, r+1]
            elif total < target:
                l += 1
            else:
                r-= 1
        
        return []


        