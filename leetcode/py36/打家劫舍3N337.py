# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rob(self, root: TreeNode) -> int:
        dp_map = {}

        def get_max(root):
            if not root:
                return 0
            the_hash = hash(root)
            if the_hash in dp_map:
                return dp_map[the_hash]
            else:
                use_this_max = root.val
                dont_use_this_max = 0

                if root.left:
                    use_this_max += get_max(root.left.left) + get_max(root.left.right)
                    dont_use_this_max += get_max(root.left)
                if root.right:
                    use_this_max += get_max(root.right.left) + get_max(root.right.right)
                    dont_use_this_max += get_max(root.right)
                res = max(use_this_max, dont_use_this_max)
                dp_map[the_hash] = res
                return res

        return get_max(root)
