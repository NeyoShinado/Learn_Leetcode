# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def invertTree(self, root: TreeNode) -> TreeNode:
		res = None
		if not root or not(root.left or root.right):
			res = root
			return res

		res = invert(root)
		return res

def invert(node):
	if node.left or node.right:
		node.tmp = node.left
		node.left = node.right
		node.right = node.tmp
		del node.tmp
	if node.left:
		node.left = invert(node.left)
	if node.right:
		node.right = invert(node.right)
	return node