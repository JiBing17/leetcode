class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # set used to keep track of all numbers seen so far
        seen = set()
        for num in nums:

            # seen number already so return true
            if num in seen:
                return True
            # otherwise add this new number into seen
            seen.add(num)
        # return false if done with iteration (no duplicates)
        return False
        