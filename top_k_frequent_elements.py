class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
        """
        
        # dict used to keep track of each number's frequency
        freq = {}
        # array of arrays used to keep track of highest frequency numbers using freq as index
        res = [ [] for i in range(len(nums) + 1) ]
        
        # count frequency of each number by populating dict 
        for n in nums:
            if n not in freq:
                freq[n] = 0
            freq[n] += 1

        # populate array with count as index and numbers with that count as element values
        for n,c in freq.items():
            res[c].append(n)
        
        # array used to display top k numbers
        answer = []
        
        # loop through array of arrays from right to left for most freq first
        for i in range(len(res) - 1, -1,-1):
            
            # popuate answer array with top frequent numbers
            for num in res[i]:
                answer.append(num)
                
                # stop and return once answer array is equal to k top elements
                if len(answer) == k:
                    return answer