import heapq

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x=0):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head_ptr = ListNode()
        p3 = head_ptr
        heap = []

        for i in lists:
            while i:
                heapq.heappush(heap, i.val)
                i = i.next

        while heap:
            smallest = heapq.heappop(heap)
            head_ptr.next = ListNode(smallest)
            head_ptr = head_ptr.next

        return p3.next