# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []

        if not root:
            return []
        this_layer = [root]

        while this_layer:
            res.append([node.val for node in this_layer])
            next_layer = []
            for t in this_layer:
                if t.left:
                    next_layer.append(t.left)
                if t.right:
                    next_layer.append(t.right)
            this_layer = next_layer

        return res
