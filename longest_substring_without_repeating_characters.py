# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # empty string return 0
        if s == "":
            return 0

        
        # keeps track of longest length so far
        longest_seen = 0
        # set used to keep track of all characters seen currently
        seen = set()
        # left pointer at starting index
        l = 0

        for r in range(len(s)):
            
            # keep removing characters seen starting from left until string of s[l] to s[r] is valid
            while s[r] in seen:
                seen.remove(s[l]) # remove left most character from left pointer
                l += 1 # adjust left pointer to go right

            seen.add(s[r]) # safe to add character to seen now
            longest_seen = max(longest_seen, r - l + 1) # look at the new length and update longest if there is a bigger length

        return longest_seen # return overall longest after program termination