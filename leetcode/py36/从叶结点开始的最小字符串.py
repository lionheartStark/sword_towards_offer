class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def dfs(self, root, nowres):
        if not root.left and not root.right:
            tmp = nowres + chr(ord('a') + root.val)
            if self.res:
                if tmp[::-1] < self.res:
                    self.res = tmp[::-1]
            else:
                self.res = tmp[::-1]
        else:
            if root.left:
                self.dfs(root.left, nowres + chr(ord('a') + root.val))
            if root.right:
                self.dfs(root.right, nowres + chr(ord('a') + root.val))

    def smallestFromLeaf(self, root: TreeNode) -> str:
        self.res = None
        if not root:
            return ''
        else:
            self.dfs(root, '')
        return self.res
