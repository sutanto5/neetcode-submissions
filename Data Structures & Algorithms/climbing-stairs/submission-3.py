class Solution:

    #{n: value}
    

    def climbStairs(self, n: int) -> int:
        #create an array to kep track of already calculated values
        memo = {}

        def dfs(n):
            if n <= 0:
                return 0
            elif n == 1:
                return 1
            elif n == 2:
                return 2

            elif n in memo:
                return memo[n]
            
            steps = dfs(n-1) + dfs(n-2)
            memo[n] = steps
            return steps
        
        return dfs(n)







        