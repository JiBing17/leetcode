# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 

         # Initialize the minimum price (curr) to the first day's price
        curr = prices[0] 

        for price in prices:

            # Calculate the potential profit by selling on the current day
            profit = max(profit, price - curr)

            # Update the minimum price seen so far
            curr = min(curr, price)

        # Return the maximum profit found
        return profit 