class Solution:
    def getIntersectionNode(self, headA, headB):
        if headA == None or headB == None:
            return None
        a, b = headA, headB
        while (a != b):
            if a == None:
                a = headB
            else:
                a = a.next
            if b == None:
                b = headA
            else:
                b = b.next
        return a
