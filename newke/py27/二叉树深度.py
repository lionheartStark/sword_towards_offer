# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot:
            return max(1+self.TreeDepth(pRoot.left), 1+self.TreeDepth(pRoot.right))
        else:
            return 0