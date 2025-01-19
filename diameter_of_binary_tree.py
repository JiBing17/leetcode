# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # overall longest length between any 2 nodes 
        self.longest = 0 

        # helper function used to traverse down the subtrees to find diameter 
        def dfs(root):
            
            # end of tree
            if not root: 
                return 0

            # longest height within left and right subtrees
            left, right = dfs(root.left), dfs(root.right)

            # update longest diameter based on current left and right subtree's height
            self.longest = max(self.longest, left + right)

            # return longest height of current (+1) tree given the 2 from the subtrees
            return 1 + max(left, right)

        # start helper func with root node
        dfs(root)
        # at end, self.longest will have the longest overall length between any two nodes in the tree
        return self.longest

