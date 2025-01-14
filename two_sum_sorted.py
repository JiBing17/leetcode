# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Your solution must use only constant extra space.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # initialize left and right pointers
        l, r = 0, len(numbers) - 1

        while l < r:

            # add both pointer's valueds together
            curr_sum = numbers[l] + numbers[r]

            # found target from the two pointer's values so return indicies of pointers 1 indexed
            if curr_sum == target:
                return l+1, r+1
            # current sum is too big, reduce next sum by moving right pointer to the left since sorted
            elif curr_sum > target:
                r -= 1
            # current sum is too small, increase next sum by moving left pointer to the right 
            else:
                l +=1
        