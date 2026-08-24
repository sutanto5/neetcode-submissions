import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # represents array of possible k values [1... k]
        k_max = max(piles)
        k_min = math.ceil(sum(piles) / h)
        last_sucess = k_max

        while k_min <= k_max:

            # 13
            banana_amt = (k_min + k_max) // 2
            total_hrs = 0

            for pile in piles:
                total_hrs += math.ceil(pile / banana_amt)

            # invalid k
            if h < total_hrs:
                k_min = banana_amt + 1


            # valid k - try somethign smaller
            else:
                k_max = banana_amt - 1
                last_sucess = min(last_sucess, banana_amt)
           
        return last_sucess
            


        
        

    