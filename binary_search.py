# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # intialize 2 pointers
        l,r = 0, len(nums) - 1

        while l <= r:
            
            #  find mid element index
            mid = (l + r) // 2

            # target found
            if nums[mid] == target:
                return mid
            # if mid element is greater, ignore all elements from the right since sorted
            elif nums[mid] > target:
                r = mid - 1 
            # same but ignore from left if target is bigger than current mid element
            else:
                l = mid + 1

        # if end of program then target is not in array, return -1
        return -1