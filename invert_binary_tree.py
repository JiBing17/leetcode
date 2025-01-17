# Given the root of a binary tree, invert the tree, and return its root.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # reached end of tree (children of leaf nodes)
        if not root:
            return None 
        
        # save left child for swap
        left_node = root.left
        # change left child to right child
        root.left= root.right
        # change right child to saved left child (before change)
        root.right = left_node

        # recursively call on both of the new child nodes
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
