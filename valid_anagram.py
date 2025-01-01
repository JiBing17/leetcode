class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # impossible to be anagram if not same length
        if len(s) != len(t):
            return False

        # dictionay to keep track of frequency of each char in both strings
        s_count = {}
        t_count = {}


        # populate dict using string s
        for char in s:
            if char not in s_count:
                s_count[char] = 0
            s_count[char] += 1

        # populate dict using string t
        for char in t:
            if char not in t_count:
                t_count[char] = 0
            t_count[char] += 1
        
        # Check if both dictionaries are equal (same frequency)
        return s_count == t_count
