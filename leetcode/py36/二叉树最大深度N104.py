# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.res = 0
        queue = [(root, 1)]

        def bfs(q):
            while q:
                t_node, deep = q.pop(0)
                if not t_node.left and not t_node.right:
                    self.res = max(self.res, deep)
                if t_node.left:
                    q.append(t_node.left, deep + 1)
                if t_node.right:
                    q.append(t_node.right, deep + 1)

        bfs(queue)
        return self.res
