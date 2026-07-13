class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
       #start from goal and move back
        goal = len(nums) - 1 #final ind

        for i in range(goal-1, -1, -1):
            print("goal" + str(goal))
            print(nums[i])
            #check whether curr ind can reach goal
            if (i + nums[i]) >= goal: #this means we have enough jumps to make it to the goal
                goal = i
        
        if goal == 0: #we had a path from start to finish
            return True
        else:
            return False

        
