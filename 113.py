# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:     
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        res = []
        queue = collections.deque()
        queue.append((root, [], 0))
        while queue:
            curNode, curPath, tempSum = queue.popleft()
            if curNode == None:
                continue
            if curNode.left == None and curNode.right == None:
                if tempSum + curNode.val == targetSum:
                    res.append(curPath+ [curNode.val])
            queue.append((curNode.left, curPath + [curNode.val], tempSum + curNode.val))
            queue.append((curNode.right, curPath + [curNode.val], tempSum + curNode.val))
        return res
