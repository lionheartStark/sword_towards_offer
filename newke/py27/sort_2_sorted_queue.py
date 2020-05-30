# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表


    def Merge(self, pHead1, pHead2):
        # TODO: learn
        # write code here
        l1 = pHead1
        l2 = pHead2
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.Merge(l1.next, l2)
            return l1
        else:
            l2.next = self.Merge(l1, l2.next)
            return l2

