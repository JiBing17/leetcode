# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # left start pointer
        l = 0
        # dict for counting char frequency
        seen = {}
        # vars used for overall longest length and count of the most frequent char
        longest_length = 0
        maxF = 0 

        for r in range(len(s)):

            # update frequency 
            if s[r] not in seen:
                seen[s[r]] = 0
            seen[s[r]] += 1

            # update maxF if needed after new addition
            maxF = max(maxF, seen[s[r]])

            # If the remaining characters in the window after replacing exceed k, shrink the window
            while (r - l + 1) - maxF > k:
                seen[s[l]] -= 1
                l += 1

            # Update the longest length after getting new valid string 
            longest_length = max(longest_length, r - l + 1)

        # return overall longest out of all valid strings
        return longest_length