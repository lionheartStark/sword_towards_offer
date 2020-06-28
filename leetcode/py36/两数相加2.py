# -*- coding:utf-8 -*-

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def string2List(self, s):
        father = None
        head = None
        for i in s:
            a = ListNode(int(i))
            a.next = father
            father = a
        return father

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1 = l1
        p2 = l2

        num1 = ""
        num2 = ""
        while p1:
            num1 = f"{p1.val}" + num1
            p1 = p1.next

        while p2:
            num2 = f"{p2.val}" + num2
            p2 = p2.next

        res = self.string2List(str(int(num1)+int(num2)))

        return res

a = ListNode(2)
b = ListNode(4)
c = ListNode(3)
a.next = b
b.next = c
a1 = ListNode(5)
b1 = ListNode(6)
c1 = ListNode(4)
a1.next = b1
b1.next = c1
print(Solution().addTwoNumbers(a,a1))