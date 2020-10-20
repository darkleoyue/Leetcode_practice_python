# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
    
    #Do not return anything, modify head in-place instead.
        if not head:
            return None
        stack = []
        curNode = head
        while curNode:
            stack.append(curNode)
            curNode = curNode.next

        n = len(stack)
        i = 0
        curNode = head
        while i < (n - 1) // 2:
            tempNode = stack.pop()
            tempNode.next =  curNode.next
            curNode.next = tempNode
            curNode = tempNode.next
            i += 1

        stack.pop().next = None
