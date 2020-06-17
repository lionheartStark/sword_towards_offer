# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def bianli_tree(self, this_layer, tree_list):
        while len(this_layer) != this_layer.count(None):
            next_layer = []
            for i in this_layer:
                if i is None:
                    tree_list.append(None)
                    #next_layer.extend([None, None])
                else:
                    tree_list.append(i.val)
                    next_layer.extend([i.left, i.right])
            this_layer = next_layer
        return tree_list

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        tree_list = []
        if root == None:
            return [None]
        return self.bianli_tree([root], tree_list)


    def make_tree(self, this_layer, data, root):

        while len(data):
            next_layer = []
            for i in this_layer:
                if i:
                    i.left = TreeNode(data.pop(0)) if data[0]!=None else data.pop(0)
                    i.right = TreeNode(data.pop(0)) if data[0]!=None else data.pop(0)
                    next_layer.extend([i.left, i.right])
                else:
                    pass
                    # data.pop(0)
                    # data.pop(0)
                    # next_layer.extend([None, None])
            this_layer = next_layer

        return  root
    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: list
        :rtype: TreeNode
        """
        this_layer = []
        if data == [None]:
            return None
        else:
            root = TreeNode(data.pop(0))
            root = self.make_tree([root], data, root)
            return root



a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
a.left = b
a.right = c
d = TreeNode(4)
e = TreeNode(5)
c.left = d
c.right = e

codec = Codec()
#print(codec.serialize(a))

tree =(codec.deserialize(codec.serialize(a)))
tree = codec.deserialize([1,None,2])
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))