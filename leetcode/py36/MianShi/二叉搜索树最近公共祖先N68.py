# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def dfs(a_root, a_p, a_q):
            if a_root is None:
                return None
            # 这一句写的不太好
            else :
                if (a_p and a_root.val == a_p.val) or (a_q and a_root.val == a_q.val):
                    return a_root
                else:
                    if a_q.val < a_root.val:
                        left = dfs(a_root.left, a_p, a_q)
                        return left
                    if a_p.val > a_root.val:
                        right = dfs(a_root.right, a_p, a_q)
                        return right
                    else:
                        return a_root

        a = [p, q]
        a.sort(key=lambda x: x.val)
        return dfs(root, a[0], a[1])

a = TreeNode(6)

b = TreeNode(2)
c = TreeNode(8)

a.left = b
a.right = c

d = TreeNode(0)
e = TreeNode(4)

b.left = d
b.right = e

k = Solution().lowestCommonAncestor(a, d, c)
print(k.val)