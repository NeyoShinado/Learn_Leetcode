'''
# Version 0
# Not pass
# 递归函数不对，且只能处理过根节点的情况
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Diameter = left_depth + right_depth
class Solution:
	def diameterOfBinaryTree(self, root: TreeNode) -> int:
		# init
		res = 0

		if not root:
			return res

		#! 递归函数在一个端口输出会是什么格式？
		if root.left and root.right:
			res = diameter_Tree(root.left, 0) + diameter_Tree(root.right, 0)
		elif root.left:
			res = diameter_Tree(root.left, 0)
		elif root.right:
			res = diameter_Tree(root.right, 0)

		return res


def diameter_Tree(node, depth):
	#init
	res = 0

	depth += 1
	if node.left:
		node.left.depth = depth
		res = diameter_Tree(node.left, depth)
	if node.right:
		node.right.depth = depth
		res = diameter_Tree(node.right, depth)

	if not node.right and not node.left:	# leaf node
		res = depth

	return res
'''


# Version 1
# 递归
#*任意一条路径都能看作某个节点为根节点的左右子树深度和
#*递归函数向下遍历各节点并返回其最大深度，再设一个全局变量记录各节点的最大路径

class Solution:
	def diameterOfBinaryTree(self, root):
		self.res = 1
		def depth(node):
			if not node: return 0
			L = depth(node.left)
			R = depth(node.right)
			self.res = max(self.res, L+R+1)
			return max(L, R) + 1

		depth(root)
		return self.res-1