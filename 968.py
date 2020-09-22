# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def SFB(self, curNode):
        
        if not curNode:
            return 0

        left = self.SFB(curNode.left)
        right = self.SFB(curNode.right)
        if left == 0 and right == 0:
            curNode.val = 1
        elif left == 1 or right == 1:
            curNode.val = 2
            self.cameras += 1
        else:
            curNode.val = 0
        return curNode.val

    def minCameraCover(self, root: TreeNode) -> int:
        
        self.cameras = 0
        self.nodeVal = self.SFB(root)
        return int(self.nodeVal == 1) + self.cameras
