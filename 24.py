# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def swapTwo(self, node0):
        node1 = node0.next
        node2 = node1.next
        node3 = node2.next
        node2.next = node1
        node1.next = node3
        node0.next = node2
        return node1

    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        node0 = ListNode(0, head)
        res = head.next
        while node0 and node0.next and node0.next.next:
            node0 = self.swapTwo(node0)

        return res
