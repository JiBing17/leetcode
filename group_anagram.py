class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        # dict used to keep track of words with same frequency
        freq = {}

        for string in strs:
            
            # array used to count freq for each letter of word
            count = [0 for i in range(26)]

            # counts frequency for letters in word
            for c in string:
                index = ord(c) - ord("a")
                count[index] += 1

            # convert to tuple for hash key purposes
            count = tuple(count)

            # case if no key yet 
            if count not in freq:
                freq[count] = []

            # add string to where the count key maps to
            freq[count].append(string)
            
        # return all values (arrays of strings)
        return freq.values()