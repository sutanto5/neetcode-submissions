class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        min_price = prices[0]

        for price in prices:
            maxProfit = max(price - min_price, maxProfit)
            min_price = min(min_price, price)

        return maxProfit