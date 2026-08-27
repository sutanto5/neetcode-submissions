class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minCost = math.inf
        goal = len(cost)

        memo = {0: cost[0], 1: cost[1]}

        def dfs(i):
            if i < 0:
                return math.inf

            nonlocal cost
            if i not in memo:
                price = cost[i] + min(dfs(i-1), dfs(i - 2))
                memo[i] = price
                return price
            else:
                return memo[i]
            
        print(memo)
        return min(dfs(goal-1), dfs(goal - 2))

            
        
