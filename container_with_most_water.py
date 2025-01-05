# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

class Solution:
    def maxArea(self, height: List[int]) -> int:

        # initialize 2 pointers
        l,r = 0, len(height) - 1
        # overall max area 
        max_area = 0 
        while l < r:

            # get distance horizontally of current box 
            distance = r - l

            # current area used for current box size
            curr_area = 0

            # smaller height is within left pointer
            if height[l] < height[r]:

                # caculate area using left pointer's height since cant overflow
                curr_area = distance * height[l]

                # move left pointer right for next size (always move smaller height to capture all sizes)
                l += 1

            # same logic but for if right height was smaller 
            else:
                curr_area = distance * height[r]
                r -= 1
            # get overall max from what we currently have and the overall in total after curr_area calculation
            max_area = max(max_area, curr_area)

        # return overall max area of entire array
        return max_area

            