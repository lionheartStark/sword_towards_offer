# Definition for a binary tree node.
import re
from collections import defaultdict


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        layer_nodes = defaultdict(list)
        i = 0
        res = None
        while i < len(S):
            layer = 0
            num_str = ''
            while S[i] == '-':
                layer += 1
                i += 1
            while i < len(S) and S[i] != '-':
                num_str += S[i]
                i += 1
            print(layer, num_str)
            # 处理入栈和出栈
            if layer == 0:
                my = TreeNode(int(num_str))
                layer_nodes[layer].append(my)
                res = my
            else:
                my = TreeNode(int(num_str))
                layer_nodes[layer].append(my)
                father = layer_nodes[layer - 1][-1]
                if father.left is None:
                    father.left = my
                elif father.right is None:
                    father.right = my
        return res


res = Solution().recoverFromPreorder("1-2--3--4-5--6--7")
print(res)
