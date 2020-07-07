# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1 = l1
        p2 = l2
        head = ListNode()
        p3 = head


        while p1 and p2:
            if p1.val < p2.val:
                head.next = p1
                p1 = p1.next
                head = head.next
            else:
                head.next = p2
                p2 = p2.next
                head = head.next
        if p1:
            head.next = p1
        elif p2:
            head.next = p2

        return p3.next


a = ListNode(1)
b = None

Solution().mergeTwoLists(a, b)