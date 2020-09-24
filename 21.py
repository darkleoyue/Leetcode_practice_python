# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def putInList(self, l1, l2, newList):
        if not l2:
            newList.next = l1
            return
        elif not l1:
            newList.next =  l2
            return

        if l1.val >= l2.val:
            temp = l2.next
            l2.next = None
            newList.next = l2
            l2 = temp
            newList = newList.next
        else:
            temp = l1.next
            l1.next = None
            newList.next = l1
            l1 = temp
            newList = newList.next
        self.putInList(l1, l2, newList)
        
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        newList = ListNode()

        self.putInList(l1, l2, newList)

        return newList.next
