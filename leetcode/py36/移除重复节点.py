class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        has_set = set()

        orghead = head
        father = None

        while (head):
            if head.val in has_set:
                head = head.next
                continue
            else:
                if father:
                    print(father.val)
                    father.next = head
                father = head

                has_set.add(head.val)
                head = head.next
        father.next = None
        return orghead


a = ListNode(1)
b = ListNode(2)
c = ListNode(2)
d= ListNode(1)
a.next = b
b.next = c
c.next = d
Solution().removeDuplicateNodes(a)
