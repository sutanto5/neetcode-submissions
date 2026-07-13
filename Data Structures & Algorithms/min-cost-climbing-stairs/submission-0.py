class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #index of the top floor
        top = len(cost)

        #base caes -> 0 and 1 index
        steps = [cost[0], cost[1]]

        for i in range(2, top):
            #min cost to reach current level
            next_level = cost[i] + min(steps[i - 1], steps[i - 2])
            steps.append(next_level)
        
        return min(steps[top - 1], steps[top - 2])