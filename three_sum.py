# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # sort for two pointer method 
        nums.sort() 
        res = []

        # skip last 2 elements in loop for two pointer to work
        for i in range(len(nums) - 2):

            # skip if next number is same as before
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # initialize 2 pointer as next value of current and last value
            l,r = i+1, len(nums) - 1

            while l < r:

                # calculate sum of 3
                curr_sum = nums[l] + nums[r] + nums[i]

                if curr_sum == 0:

                    # add answer if valid 
                    res.append([nums[i],nums[l],nums[r]])

                    # move both pointers in
                    l += 1 
                    r -= 1

                    # keep moving if values are the same as before
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                # move left pointer right if value is too small
                elif curr_sum < 0:
                    l += 1
                # same for if value is too big (move right pointer left)
                else:
                    r -= 1
                    
        # return result array of all valid elements
        return res
            