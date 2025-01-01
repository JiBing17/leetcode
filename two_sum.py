class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # dict used to keep track of all numbers with their indices that was seen already
        seen = {}
        for i in range(len(nums)):
            
            # find the complement number that is used to with current num to add up to sum
            difference = target - nums[i]
            if difference in seen:
                # if complemnt is found, return both current indice and complent's indice
                return seen[difference], i
            # store current number and index in seen before continuing
            seen[nums[i]] = i