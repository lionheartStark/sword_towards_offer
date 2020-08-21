# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        p2 = l2

        new_head = ListNode()
        p3 = new_head
        while p1 or p2:
            if p1 and p2:
                if p1.val < p2.val:
                    new_head.next = p1
                    p1 = p1.next
                else:
                    new_head.next = p2
                    p2 = p2.next
            elif p1:
                new_head.next = p1
                p1 = p1.next
            elif p2:
                new_head.next = p2
                p2 = p2.next
            new_head = new_head.next
        return p3.next


l1 = None
l2 = ListNode(0)

d = Solution().mergeTwoLists(l1, l2)

print(d)
