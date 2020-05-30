# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        """
        输入一个链表，输出该链表中倒数第k个结点。
        """
        # write code here
        node_list = []
        p = head
        if p:
            node_list.append(p)
        else:
            return None
        while p.next != None:
            p = p.next
            node_list.append(p)
        if k == 0:
            return None
        elif len(node_list) >= k:
            return node_list[-k]
        else:
            return None