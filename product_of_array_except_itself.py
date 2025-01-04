# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # array used to store result for each number entry
        res = [1 for i in range(len(nums))] 

        # vars used to keep track of cumumulative sum from both directions
        prefix = 1
        postfix = 1

        # populate res array with prefix for each entry from left to right
        for i in range(len(nums)):

            # We set res[i] first to store the current prefix because res[i] needs the prefix product 
            # before nums[i] is included in the calculation.
            res[i] = prefix 
            prefix *= nums[i]

        # populate res array with prefix for each entry from right to left
        for i in range(len(nums)-1, -1,-1):

            # Multiply res[i] with postfix to include the cumulative product from the right side to get final answer.
            res[i] *= postfix
            postfix *= nums[i] 

        return res