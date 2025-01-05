# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

class Solution:

    # custom function used to determine if character was a alphanumeric or not
    def alphaNum(self, s):

        # used ord() for number boundary checks
        if ord("A") <= ord(s) <= ord("Z") or ord("a") <= ord(s) <= ord("z") or ord("0") <= ord(s) <= ord("9"): 
            return True
        return False

    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1 # left and right pointers

        while l < r:

            # skip all non alphanumeric char by moving left pointer right
            while l < r and not self.alphaNum(s[l]):
                l += 1
            # skip all non alphanumeric char by moving right pointer left
            while r > l and not self.alphaNum(s[r]):
                r -= 1 

            # once valid check if both pointer's characters are the same, if not return false
            if s[l].lower() != s[r].lower():
                return False

            # go to next to characters
            l += 1
            r -= 1

        # return true if no errors from program
        return True
