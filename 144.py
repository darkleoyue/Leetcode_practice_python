# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def VLR(self, curNode, res):
        
        if not curNode:
            return
        res.append(curNode.val)
        self.VLR(curNode.left, res)
        self.VLR(curNode.right, res)
        
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        if not root:
            return []
        res = []
        self.VLR(root, res)

        return res
