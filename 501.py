# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def insertInDict(self, node, dictInsert):
        
        if not node:
            return

        if node.val in dictInsert:
            dictInsert[node.val] += 1
        else:
            dictInsert[node.val] = 1
        
        self.insertInDict(node.left, dictInsert)
        self.insertInDict(node.right, dictInsert)

    def findMode(self, root: TreeNode) -> List[int]:

        if not root:
            return []

        dictInsert = {}
        listOfMax = []
        self.insertInDict(root, dictInsert)
        maxVal = max(dictInsert.values())
        for val, num in dictInsert.items():
            if num >= maxVal:
                listOfMax.append(val)
        
        return listOfMax
