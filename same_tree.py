# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # both trees are at the end, return True sense no errors were detected the way down
        if not p and not q:
            return True
        
        # p tree ends and q doesn't end (not same tree)
        if not p and q:
            return False

        # similar case but vice versa
        if p and not q:
            return False
        
        # # current value doesn't match
        if p.val != q.val:
            return False
        
        # check subtrees to make sure the right and left are both the same and return that boolean
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
