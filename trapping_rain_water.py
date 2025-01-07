class Solution:
    def trap(self, height: List[int]) -> int:

        # if the height array is empty, no water can be trapped
        if not height:
            return 0
        
        # initialize two pointers
        l, r = 0, len(height) - 1
        
        # variables to store the maximum heights from the left and right
        maxL = height[l]
        maxR = height[r]
        
        # total amount of water trapped
        water_trapped = 0

        while l < r:

            # calculate side with the smaller height seen so far
            if maxL <= maxR:

                # caculate water trapped next to it
                l += 1

                # Update tallest structure 
                maxL = max(maxL, height[l])

                # Calculate water trapped at the current position based on tallest seen
                water = maxL - height[l]

                # add water to the total if it's positive
                if water > 0:
                    water_trapped += water

            # same case but for right side 
            else:
                r -= 1
                maxR = max(maxR, height[r])
                water = maxR - height[r]
                if water > 0:
                    water_trapped += water

        # return the total amount of water trapped
        return water_trapped
