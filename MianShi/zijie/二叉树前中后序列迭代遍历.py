# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """
        先序遍历
        """
        res = []
        if not root:
            return []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return res


    def posorderTraversal(self, root: TreeNode) -> List[int]:
        """
        后序遍历
        """
        res = []
        if not root:
            return []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return res

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        中序遍历
        """
        res = []
        p = root
        stack = []
        while (p or stack):
            while p:
                stack.append(p)
                p = p.left
            p = stack.pop()
            res.append(p.val)
            p = p.right
        return res