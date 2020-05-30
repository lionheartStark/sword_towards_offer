# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        this_lay = []
        this_lay.append(root)

        res = []
        while this_lay:
            #print([t.val for t in this_lay])
            res.extend([t.val for t in this_lay])
            next_lay = []
            for i in this_lay:
                next_lay.append(i.left) if i.left else []
                next_lay.append(i.right) if i.right else []
            this_lay = next_lay
        return res

# a=TreeNode(1)
# b=TreeNode(2)
# c=TreeNode(3)
# d=TreeNode(4)
# a.left=b
# a.right=c
# b.left=d
# Solution().PrintFromTopToBottom(a)