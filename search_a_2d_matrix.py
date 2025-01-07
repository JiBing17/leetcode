# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # Initialize the current row to the first row
        current_row = 0

        # Find the row where the first element is bigger than target
        while current_row < len(matrix) and matrix[current_row][0] <= target:
            current_row += 1
        
        # look at row before the bigger element of target's row (correct spot to perform binary search)
        current_row -= 1

        # basic binary search on certain row of 2d matrix
        l,r = 0, len(matrix[0]) - 1

        while l <= r:
            mid = (l + r) // 2

            # found
            if matrix[current_row][mid] == target:
                return True
            # look at left half
            elif matrix[current_row][mid] > target:
                r = mid - 1
            # look at right half
            else:
                l = mid + 1
        # not found if program terminates
        return False