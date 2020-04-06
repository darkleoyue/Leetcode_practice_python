# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        liste = []
        
        def to_list(node):
            if node:
                liste.append(node.val)
                to_list(node.left)
                to_list(node.right)
        
        to_list(root)
        return len(set(liste)) == 1
