# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    输入某二叉树的前序遍历和中序遍历的结果，
    请重建出该二叉树。
    假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
    例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
    """
    def get_left(self, tin, val):
        return tin[:tin.index(val)]

    def get_right(self, tin, val):
        return tin[tin.index(val):]

    def konw_dict_to_node(self, konw_dict):
        for nodeval in konw_dict:
            node = TreeNode(nodeval)
            node.left = TreeNode()

        pass



    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        ret_node = None
        # 存储已经知道位置的
        konw_dict = {}
        subtin = tin
        for node_val in pre:
            if konw_dict:
                for k, v in konw_dict.items():
                    if node_val in v["left"]:
                        subtin = v["left"]
                        konw_dict[k]["left"] = [node_val]

                        konw_dict[node_val] = {}
                        konw_dict[node_val]["node"] = TreeNode(node_val)
                        konw_dict[k]["node"].left = konw_dict[node_val]["node"]
                        konw_dict[node_val]["left"] = self.get_left(subtin, node_val)
                        konw_dict[node_val]["right"] = self.get_right(subtin, node_val)
                    elif node_val in v["right"]:
                        subtin = v["right"]
                        konw_dict[k]["right"] = [node_val]
                        konw_dict[node_val] = {}
                        konw_dict[node_val]["node"] = TreeNode(node_val)
                        konw_dict[k]["node"].right = konw_dict[node_val]["node"]
                        konw_dict[node_val]["left"] = self.get_left(subtin, node_val)
                        konw_dict[node_val]["right"] = self.get_right(subtin, node_val)
            else:
                konw_dict[node_val] = {}
                konw_dict[node_val]["node"] = TreeNode(node_val)
                konw_dict[node_val]["left"] = self.get_left(subtin, node_val)
                konw_dict[node_val]["right"] = self.get_right(subtin, node_val)
            # print(konw_dict)
        # print(konw_dict)


        for node_val in pre:
            return konw_dict[node_val]["node"]

    def reConstructBinaryTree_smarter(self, pre, tin):
        """
        做这个题目的核心思想是找到最后的终止条件
        :param pre:
        :param tin:
        :return:
        """
        # write code here
        if len(pre) == 0:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])
        else:
            flag = TreeNode(pre[0])
            flag.left = self.reConstructBinaryTree(pre[1:tin.index(pre[0]) + 1], tin[:tin.index(pre[0])])
            flag.right = self.reConstructBinaryTree(pre[tin.index(pre[0]) + 1:], tin[tin.index(pre[0]) + 1:])
        return flag


if __name__ == "__main__":
    res = Solution().reConstructBinaryTree([1,2,4,7,3,5,6,8], [4,7,2,1,5,3,8,6])
    print(res)