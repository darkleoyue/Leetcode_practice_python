# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def InsertNodes(self, curNode, queue):

        if not curNode:
            return
        
        if not curNode.left and not curNode.right:
            queue.append(curNode)
        else:
            self.InsertNodes(curNode.left, queue)
            self.InsertNodes(curNode.right, queue)
            queue.append(curNode)

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        
        if not root:
            return []
        
        res = []
        queue = collections.deque()
        self.InsertNodes(root, queue)
        while queue:
            res.append(queue.popleft().val)
        
        return res
