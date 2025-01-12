# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # s1 needs to be substring of s2
        if len(s1) > len(s2):
            return False

        # arrays for strings to count freq of each char
        freq_1 = [0] * 26
        freq_2 = [0] * 26

        # var used to check how many chars match (full match : 26)
        matches = 0

        # update freq arrays based on s1 length (the substring)
        for i in range(len(s1)):
            freq_1[ord(s1[i]) - ord('a')] += 1
            freq_2[ord(s2[i]) - ord('a')] += 1
        
        # count matches for each array entry
        for i in range(len(freq_1)):
            if freq_1[i] == freq_2[i]:
                matches += 1
        # left pointer for sliding window
        l = 0

        # start from where we left off for counting freq
        for r in range(len(s1), len(s2)):

            # found valid case
            if matches == 26:
                return True
            
            # update freq for s2 each iteration of r (adding char from right)
            index = ord(s2[r]) - ord('a')
            freq_2[index] += 1 

            # if updating made a match, increment matches
            if freq_2[index] == freq_1[index]:
                matches += 1
            # if updating lost a match, decrement matches
            if freq_2[index] == freq_1[index] + 1:
                matches -= 1
            
            # same as above code but for moving left pointer (removing char from left) 
            # we do this to slide window to keep length as s1
            index = ord(s2[l]) - ord('a')
            freq_2[index] -= 1
            if freq_2[index] == freq_1[index]:
                matches += 1
            if freq_2[index] == freq_1[index] - 1:
                matches -= 1
            l += 1

        # return bool since matches can be 26 after last iteration 
        return matches == 26