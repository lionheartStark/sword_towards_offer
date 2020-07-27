# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __init__(self):
        self.res = None

    def reverseList(self, head: ListNode) -> ListNode:
        """
        递归
        :param head:
        :return:
        """
        if head.next is None or head is None:
            return head
        else:
            newhead = self.reverseList(head.next)
            head.next.next = head
            head.next = None
            return newhead

    def reverseList(self, head: ListNode) -> ListNode:
        """
        迭代
        :param head:
        :return:
        """
        pre = None
        now = head

        while True:
            tmp = now.next
            now.next = pre
            pre = now
            if tmp:
                now = tmp
            else:
                return pre


