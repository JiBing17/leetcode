# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        
        result = []
        # decreasing deque data struct (biggeest num on the left)
        q = collections.deque()
        # left and right indices for sliding window
        l,r = 0, 0 

        
        while r < len(nums):
            
            # keep removing elements in deque if num we are about to add is bigger than right most element
            while q and nums[q[-1]] <= nums[r]:
                q.pop()
            q.append(r)
            
            # if length is k, add the biggest in window which is stored in left most part of deque
            if r - l + 1 >= k:
                result.append(nums[q[0]])
                l += 1 # only move window from left to right one space once k is reached

            # remove number that is no longer in window from left
            if l > q[0]:
                q.popleft()


            r += 1 # expand window 
            
        return result