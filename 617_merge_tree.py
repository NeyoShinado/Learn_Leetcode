# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
	def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
		if t1 and t2:
			res = merge(t1, t2)
		elif t1:
			res = merge(t1, None)
		elif t2:
			res = merge(None, t2)
		else:
			res = None

		return res


def merge(node1, node2):
	# init
	nl1 = None
	nl2 = None
	nr1 = None
	nr2 = None

	# merge cur_node
	if node1 and node2:
		node1.val += node2.val
		# merge sub_node
		if node1.left and node2.left:
			nl1 = node1.left
			nl2 = node2.left
		elif node1.left:
			nl1 = node1.left
		elif node2.left:
			nl2 = node2.left

		if node1.right and node2.right:
			nl1 = node1.right
			nl2 = node2.right
		elif node1.right:
			nr1 = node1.right
		elif node2.right:
			nr2 = node2.right
		
	elif node2:
		node1.val = node2.val
		if node2.left:
			nl2 = node2.left
		if node2.right:
			nr2 = node2.right
	elif node1:
		if node1.left:
			nl1 = node1.left
		if node1.right:
			nr2 = node2.right

	node1.left = merge(nl1, nl2)
	ndoe1.right = merge(nr1, nr2)


	return node1