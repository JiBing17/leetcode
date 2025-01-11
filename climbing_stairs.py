# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    def climbStairs(self, n: int) -> int:
        
        # base case for 1 stair step
        if n == 1:
            return 1
        
        # array with state that stores the number of ways to climb i steps
        dp = [0 for i in range(n+1)]

        # initialize base steps (no steps, 1 step, 2 step)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2

        # populate rest using previous references to find optimal way for current step i
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i - 2]

        # return entry for n steps
        return dp[n]
