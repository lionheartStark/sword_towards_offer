# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        """
        passed
        """
        if not root:
            return []
        else:
            res = []
            this_layer = [root]
            root.the_path = [root.val]
            while this_layer:
                next_layer = []
                for t in this_layer:
                    if t.left:
                        t.left.the_path = []
                        t.left.the_path.extend(t.the_path)
                        t.left.the_path.append(t.left.val)
                        next_layer.append(t.left)
                    if t.right:
                        t.right.the_path = []
                        t.right.the_path.extend(t.the_path)
                        t.right.the_path.append(t.right.val)
                        next_layer.append(t.right)
                    if not t.left and not t.right:
                        if sum(t.the_path) == expectNumber:
                            res.append(t.the_path)
                this_layer = next_layer
            res.sort(key=lambda x:len(x),reverse=True)
            return res
