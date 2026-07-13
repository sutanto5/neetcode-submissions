class Solution:

    #{n: value}
    

    def climbStairs(self, n: int) -> int:
        #create an array to kep track of already calculated values
        total_poss = 0
        seen = {0:1, 1:1}

        #for each step sum should be equal to n
        def memo(n):
            if n in seen:
                return seen[n]

            #addjing everythign to the set of calculated val
            seen[n] = memo(n-1) + memo(n-2)
            return seen[n]

        #initialize the top approach
        return memo(n)





        