# https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNodes(self, l1: ListNode, l2: ListNode, isTen=False) -> ListNode:
        next1, next2 = None, None
        if not isTen:
            finalVal = 0
        else:
            finalVal = 1
        if l1 is not None:
            finalVal += l1.val
            next1 = l1.next
        if l2 is not None:
            finalVal += l2.val
            next2 = l2.next
        newTen = False
        if finalVal >= 10:
            finalVal -= 10
            newTen = True
        if next1 is None and next2 is None:
            if not newTen:
                return ListNode(finalVal)
            else:
                return ListNode(finalVal, ListNode(1))
        node = ListNode(finalVal, self.addTwoNodes(next1, next2, newTen))
        return node

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node = self.addTwoNodes(l1, l2)
        return node
