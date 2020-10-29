# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    
    def sumNumbers(self, root: TreeNode) -> int:

        res = []

        def DSF(curNode, curInt):
            if not curNode:
                return
            if not curNode.left and not curNode.right:
                curInt = curInt * 10 + curNode.val
                res.append(curInt)
                return
            curInt = curInt * 10 + curNode.val
            DSF(curNode.left, curInt)
            DSF(curNode.right, curInt)
        
        DSF(root, 0)

        return sum(i for i in res)
