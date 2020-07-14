class Solution:
    def __init__(self):
        self.ans = 0

    def dfs(self, root, sum):

        if root is None:
            return
        if root.val == sum:
            self.ans += 1
        self.dfs(root.left, sum - root.val)
        self.dfs(root.right, sum - root.val)
        #

    def pathSum(self, root, sum):
        if root is None:
            return self.ans
        self.dfs(root, sum)
        self.pathSum(root.left, sum)
        self.pathSum(root.right, sum)
        return self.ans
