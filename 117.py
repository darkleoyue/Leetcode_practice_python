"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        queue = collections.deque()
        tempQueue = collections.deque()
        queue.append(root)
        while queue:
            curNode = queue.popleft()
            if curNode.left:
                tempQueue.append(curNode.left)
            if curNode.right:
                tempQueue.append(curNode.right)
            if queue:
                nextNode = queue.popleft()
                curNode.next = nextNode
                queue.insert(0, nextNode)
            else:
                curNode.next = None
                queue.extend(tempQueue)
                tempQueue.clear() 
        return root
