class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # add all nums into set for fast lookup
        seen = set(nums)
        longest_length = 0

        for num in seen:
            # if num is the start of a sequence
            if num - 1 not in seen:
                curr_length = 0

                # add to current longest seen for sequence until end
                while num + curr_length in seen:
                    curr_length += 1
                # compare with overall longest seen so far
                longest_length = max(longest_length, curr_length)
        # return overall longest
        return longest_length
