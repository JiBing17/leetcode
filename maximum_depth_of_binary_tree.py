# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # return once traversal is at the end of tree (don't take in consideration of NULL as length)
        if not root:
            return 0

        # at each level take the max length of the two subtrees and add 1 (current level) to it
        max_length = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) 

        # that will be max_length of this level 
        return max_length