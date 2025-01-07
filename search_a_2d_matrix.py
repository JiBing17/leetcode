# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        
        # binary search for row that target will be in
        top_row = 0
        bottom_row = len(matrix) - 1

        while top_row <= bottom_row:

            # look at first and last elements of mid row to decide what half of the rows to look at 
            mid = (top_row + bottom_row) // 2

            # look at bottom half of the rows
            if target > matrix[mid][-1]:
                top_row = mid + 1
            # look at top half of the rows
            elif target < matrix[mid][0]:
                bottom_row = mid - 1
            # found a mid row with that the target might be in
            else:
                break
                
        # store that row as current_row to perform binary search
        current_row = (top_row + bottom_row) // 2

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