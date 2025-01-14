# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
# The testcases will be generated such that the answer is unique.

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        
        # invalid case since t needs to be a substring of s
        if len(t) > len(s):
            return ""

        # dicts used for counting freq of each char in string s and t
        seen_s = {}
        seen_t = {}

        # vars to keep track of current shortest length of the start and end indexes of that string
        shortest_length = float("inf")
        shortest_seen = [-1,-1]
        
        # count freq for substring t and store in dict
        for char in t:
            if char not in seen_t:
                seen_t[char] = 0 
            seen_t[char] += 1   

        # needed contains the length of unique letters to satisfy substring 
        needed = len(seen_t)
        # var used to keep track fo current window of satisfied letters 
        have = 0

        # left pointer for window' left end
        l = 0

        # move right end of window each iteration
        for r in range(len(s)):
            
            # update freq of current char for window's seen dict
            if s[r] not in seen_s:
                seen_s[s[r]] = 0
            seen_s[s[r]] += 1

            # if char is contained in string t and now has the same freq, add 1 to have since letter is satisifed
            if s[r] in seen_t and seen_t[s[r]] == seen_s[s[r]]:
                    have += 1 

            # once all satisfied, keep remvoing letters in window's left end to see shortest valid string
            while have == needed:
                
                # update string if shorter (change indexes and length to newest shortest valid string)
                if shortest_length > r - l + 1:
                    shortest_seen = [l,r] # indexes
                    shortest_length = r - l + 1 # length
                
                # reduce count of left most char in window
                seen_s[s[l]]  -= 1

                # update if we remove a char that was satisfied for string t
                if s[l] in seen_t and seen_t[s[l]] > seen_s[s[l]]:
                    have -= 1

                # move left pointer right
                l += 1
        
        # get the shortest valid string's left and right indices
        l,r = shortest_seen

        # return that string unless it hasn't changed since start, in that case return ""
        return s[l:r + 1] if shortest_length!= float("inf") else ""
            
            