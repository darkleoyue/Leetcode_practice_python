# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        
        listOfNodes = [(root, 0)]
        sumOfNodes = 0

        while listOfNodes:
            curNode, ifPassed = listOfNodes.pop()
            if curNode == None:
                continue
            if ifPassed == 1:
                sumOfNodes += curNode.val
                curNode.val = sumOfNodes
            else:
                listOfNodes.append((curNode.left, 0))
                listOfNodes.append((curNode, 1))
                listOfNodes.append((curNode.right, 0))
        
        return root
