class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #check for length of array
        if len(prices) < 2:
            return 0

        #sliding window technique
        minimum = prices[0]
        back = 1
        curr = prices[back] - minimum
        best = 0

        while back < len(prices):
            #if negative that means first price is too big


            curr = prices[back] - minimum

            if curr > best:
                best = curr

            if minimum > prices[back]:
                minimum = prices[back]
            
            back = back + 1




        return best