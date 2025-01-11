# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

# You can either start from the step with index 0, or the step with index 1.

# Return the minimum cost to reach the top of the floor.

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # base case
        if len(cost) == 2:
            return min(cost[0], cost[1])

        # stores the min cost to reach step i
        dp = [0 for i in range(len(cost))]

        # initialize base cost of step 1 and 2
        dp[0] = cost[0]
        dp[1] = cost[1]

        # populate rest of array 
        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        # could've reached top floor from last step and second last step so take min
        return min(dp[len(cost) - 1] , dp[len(cost) - 2])