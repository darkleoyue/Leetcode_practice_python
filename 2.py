# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def addNum(self, l1, l2, i):
        
        if not l1 and not l2 and not i:
            return None

        value = (l1.val if l1 else 0) + (l2.val if l2 else 0) + i
        node = ListNode(value % 10)
        node.next = self.addNum(l1.next if l1 else None, l2.next if l2 else None, value // 10)

        return node

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        res = self.addNum(l1, l2, 0)

        return res
