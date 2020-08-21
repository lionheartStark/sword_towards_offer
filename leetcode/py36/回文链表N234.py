# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        fast_p = head
        slow_p = head
        pre = None
        is_ou = True
        while True:
            if fast_p.next:
                if fast_p.next.next:
                    fast_p = fast_p.next.next
                else:
                    fast_p = fast_p.next
                    is_ou = False

            tmp = slow_p.next
            slow_p.next = pre
            pre = slow_p
            slow_p = tmp
            if not fast_p.next:
                break
        if is_ou:
            # 后半截会多
            slow_p = slow_p.next
            while slow_p:
                if slow_p.val != pre.val:
                    return False
                slow_p = slow_p.next
                pre = pre.next
            return True

        else:
            # 前后等
            while slow_p:
                if slow_p.val != pre.val:
                    return False
                slow_p = slow_p.next
                pre = pre.next
            return True


a_list = [1, 2]
head = ListNode(0)
p = head
for i in a_list:
    p.next = ListNode(i)
    p = p.next
print(Solution().isPalindrome(head.next))
