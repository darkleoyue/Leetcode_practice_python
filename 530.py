# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def insertNodes(self, node, listOfValues):
        if not node:
            return
        listOfValues.append(node.val)
        self.insertNodes(node.left, listOfValues)
        self.insertNodes(node.right, listOfValues)

    def getMinimumDifference(self, root: TreeNode) -> int:
        listOfValues = []
        self.insertNodes(root, listOfValues)
        listOfValues.sort()
        res = float(inf)
        n = len(listOfValues)
        for i in range(1, n):
            if listOfValues[i] - listOfValues[i - 1] < res:
                res = listOfValues[i] - listOfValues[i - 1]
        return res
