# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List


class Solution:

    def get_tree(self, val_list):
        n = len(val_list)
        if n == 0:
            return None
        if n == 1:
            return TreeNode(val_list[0])
        mid = n // 2
        midnode = TreeNode(val_list[mid])
        midnode.left = self.get_tree(val_list[:mid])
        midnode.right = self.get_tree(val_list[mid + 1:])
        return midnode

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        val_list = []
        while head:
            val_list.append(head.val)
            head = head.next
        new_head = self.get_tree(val_list)
        return new_head