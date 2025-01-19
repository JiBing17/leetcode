# Given a binary tree, determine if it is height-balanced 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # global boolean used to check if entire tree is balanced
        self.is_balanced = True

        # helper function used to traverse through and compare the height's of the 2 subtrees
        def dfs(root):

            # reached end of tree
            if not root:
                return 0
            
            # obtain the height of the left and right subtrees
            left , right = dfs(root.right), dfs(root.left)

            # if height difference is more than 1, then entire tree is not balanced, change boolean
            if abs(left - right) > 1:
                self.is_balanced = False

            # return height of current tree (+1 for current level)
            return 1 + max(left, right)

        # run helper function using given root node
        dfs(root)
        # return wheter is boolean was changed or not during fucntion call
        return self.is_balanced