# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.sumLeaves = 0

    def ChildIsLeftLeave(self, Node: TreeNode):
        if not Node:
            return False

        if Node.left and not Node.left.left and not Node.left.right:
            self.sumLeaves += Node.left.val
            self.ChildIsLeftLeave(Node.right)
        else:
            self.ChildIsLeftLeave(Node.left)
            self.ChildIsLeftLeave(Node.right)

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.ChildIsLeftLeave(root)
        return self.sumLeaves
