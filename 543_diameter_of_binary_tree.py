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
			res = 2 + diameter_Tree(root.left, 0) + diameter_Tree(root.right, 0)
		elif root.left:
			res = diameter_Tree(root.left, 0) + 1
		elif root.right:
			res = diameter_Tree(root.right, 0) + 1

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