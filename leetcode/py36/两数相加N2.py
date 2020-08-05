# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    """

    给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

    如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

    您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
    """


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode()
        head = res
        jinwei = 0
        while l1 or l2:
            if l1 and l2:
                res.next = ListNode((l1.val + l2.val + jinwei) % 10)
                jinwei = (l1.val + l2.val + jinwei) // 10
                res = res.next
                l1 = l1.next
                l2 = l2.next
            elif l1:
                res.next = ListNode((l1.val + jinwei) % 10)
                jinwei = (l1.val + jinwei) // 10
                res = res.next
                l1 = l1.next
            elif l2:
                res.next = ListNode((l2.val + jinwei) % 10)
                jinwei = (l2.val + jinwei) // 10
                res = res.next
                l2 = l2.next
        if jinwei == 1:
            res.next = ListNode((jinwei) % 10)
        return head.next
