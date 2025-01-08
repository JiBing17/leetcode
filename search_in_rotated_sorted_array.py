# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # two pointers for finding pivot's position / index
        l,r = 0, len(nums) - 1

        # algorithm used in prev leetcode to find pivot (ends at left pointer (l))
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
    
        # start contains pivot position
        start = l

        # new left and right pointer for binary search
        left = 0
        right = len(nums) - 1

        # use binary search on left or right half depending on target value
        if target >= nums[start] and target <= nums[right]:
            left = start
        else:
            right = start
        
        # basic binary search after setting up the bounds
        while left <= right:
            mid = ( left + right ) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        # can't find element if program terminates
        return -1

        