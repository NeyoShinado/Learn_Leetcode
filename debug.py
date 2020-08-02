# Version0
# 约定前序遍历
# TC：O(N), SC:O(N)
# ! how to save the structure in a series?
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """
        Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        se_str = serializeStep(root, "")
        return se_str.strip(",")

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")
        if len(data) == 1:
            root = None
            return root

        root = TreeNode(0)  # init with 0 root
        root, data = deserializeStep(root, data)
        return root


def serializeStep(node, se_str):
    # 先序遍历，外加None,None确定叶结点
    if node == None:
        se_str += "None,"
    else:
        se_str += str(node.val) + ","
        se_str = serializeStep(node.left, se_str)
        se_str = serializeStep(node.right, se_str)

    return se_str


def deserializeStep(node, se_list):
    # 同源的当层节点在当前函数中更新，所以只需传递序列数组就能重建子树
    # 函数返回更改后的序列数组
    # 当左子树为空时，返回的序列数组已将左子树元素弹出，重建当前节点右子树
    # 当左右子树都为空时，返回的序列数组已经将当前子节点树元素弹出，返回父节点重建其右子树
    # 最终返回给根节点的数组是空的
    val = se_list.pop(0)
    if val != "None":  # 只有非空才是节点对象
        node = TreeNode(int(val))

    else:
        node = None
        return node, se_list

    node.left, se_list = deserializeStep(node.left, se_list)
    node.right, se_list = deserializeStep(node.right, se_list)

    return node, se_list


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    t = Codec()
    print(t.serialize(root))
    res = t.deserialize(t.serialize(root))
    print(res.val)