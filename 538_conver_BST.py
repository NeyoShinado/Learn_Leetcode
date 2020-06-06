'''
# Version 0
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def convertBST(self, root: TreeNode) -> TreeNode:
		if not root:
			res = root
			return res
		
		root.parent = None
		cumsum(root)
		res = root

		return res


def cumsum(node):
	# right side first
	if node.left:
		node.left.parent = node
		
	if node.right:
		node.right.parent = node
		node.right = cumsum(node.right)
		rsum = node.right.val
	else:
		rsum = 0

	# parent point second
	if node.parent and node.parent.left and node.parent.left == node:
		node.val = node.val + node.parent.val + rsum
	else:
		node.val = node.val + rsum

	# left side last
	if node.left:
		node.left.parent = node
		if node.left.right:
			node.left.right = cumsum(node.left.right)
			node.left.val = node.left.val + node.val + node.left.right.val
		else:
			node.left.val = node.left.val + node.val
	return node
'''


# Version 1
# 每个点的新值等于原点和右节点之和，原节点和左节点分开递归
# TC: O(N), SC: O(H)
class Solution:
	def convertBST(self, root):
		def cumsum(node):
			if not node: return 0
			node.val = node.val + cumsum(node.right)

			if node.left:
				node.left.val = node.val + cumsum(node.left)
			return node.val

		res = cumsum(root)
		return root