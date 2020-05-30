# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        """
        输入一个链表，反转链表后，输出新链表的表头。
        """
        p = pHead
        father = None

        while p:
            newp = ListNode(p.val)
            newp.next = father
            father = newp
            p = p.next

        return father

    def ReverseList2(self, pHead):
        # write code here
        # TODO: read
        # write code here
        if not pHead or not pHead.next:
            return pHead

        last = None

        while pHead:
            tmp = pHead.next
            pHead.next = last
            last = pHead
            pHead = tmp
        return last
