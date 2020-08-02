# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    给定一个二叉树，原地将它展开为一个单链表。
    """
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        res = []
        stack = [root]
        if not root:
            return None
        else:
            while stack:
                a_node = stack.pop()

                if a_node.right:
                    stack.append(a_node.right)
                if a_node.left:
                    stack.append(a_node.left)
                if res:
                    res[-1].right = a_node
                    res[-1].left = None
                res.append(a_node)
        if res:
            res[-1].right = None
            res[-1].left = None
            
class Solution:
    def flatten(self, root: TreeNode) -> None:
        while root:
            if root.left:   #左子树存在的话才进行操作
                sub_left = root.left
                while sub_left.right:   #左子树的右子树找到最深
                    sub_left = sub_left.right
                sub_left.right = root.right #将root的右子树挂到左子树的右子树的最深
                root.right = root.left      #将root的左子树挂到右子树
                root.left = None            #将root左子树清空
            root = root.right