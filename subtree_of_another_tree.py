# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # helper function to check if two trees are the same
    def is_same_tree(self, root, subRoot):

        # made it to end with no problems, return true
        if not root and not subRoot:
            return True
        # second tree ended while first didnt, return false
        elif root and not subRoot:
            return False
        # first tree ended while second didnt, return false
        elif not root and subRoot:
            return False
        else:
            # values aren't the same, return false
            if root.val != subRoot.val:
                return False
            # check if left and right subtrees are the same and return that boolean
            return self.is_same_tree(root.left, subRoot.left) and self.is_same_tree(root.right, subRoot.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # base cases for first and second tree during traversal
        if not subRoot:
            return True
        if not root:
            return False

        # check if same tree
        if self.is_same_tree(root, subRoot):
            return True
        # if not, check subtrees of tree 1 to see if second tree can be a subtree there and return that boolean
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
