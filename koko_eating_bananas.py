# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # binary search using range from 1 to max number in piles (max: eating all bannas from a pile in an hour)
        l,r = 1, max(piles)

        # worst case where we finish a pile per hour
        result = r

        while l <= r:

            # pick a middle k value
            k = ( l + r ) // 2
            
            hours_needed = 0 
            # sum up hours needed to finish the piles given that k 
            for pile in piles:
                hours_needed += math.ceil(pile / k)
            # can't be done, look at right half for a bigger k value to try
            if hours_needed > h:
                l = k + 1
            # can be done, look at left half for a smaller k if possible
            else:
                r = k - 1
                # update overall smallest k that is valid
                result = min(result, k)

        # return smallest overall k given the input
        return result

    
