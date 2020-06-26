# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def qiu(self, root):
        bilist = [root.val]
        if root.left:
            res_left = self.qiu(root.left)
            if res_left > 0:
                bilist.append(res_left+root.val)
        if root.right:
            res_right = self.qiu(root.right)
            if res_right > 0:
                bilist.append(res_right+root.val)
        if root.left and root.right:
            bilist.append(res_left+root.val+res_right)
        now_res = max(bilist)
        if root.left and root.right:
            bilist.pop(-1)
        give_up = max(bilist)
        print(now_res)
        self.res = max(now_res, self.res)
        return give_up

    def maxPathSum(self, root: TreeNode) -> int:
        self.res = root.val
        self.qiu(root)
        print(self.res)


a = TreeNode(5)
b = TreeNode(4)
c = TreeNode(8)
a.left = b
a.right = c
d = TreeNode(11)
b.left = d
e = TreeNode(7)
f = TreeNode(2)
d.left = e
d.right = f
g = TreeNode(13)
h = TreeNode(4)
i = TreeNode(1)
c.right = h
c.left = g
h.right =i
Solution().maxPathSum(a)