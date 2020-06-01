# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def pathSum(self, root: TreeNode, sum: int) -> int:
		# init
		res = 0
		node = root

		if root:
			traverse(node, sum)

		return res


def nextsum(presum, node, sum):
	# init
	cnt = 0
	curnsum = presum + node.val

	if curnsum == sum:
		cnt += 1

	if node.left and node.right:
		cnt += nextsum(curnsum, node.left, sum) + nextsum(curnsum, node.right, sum)
	elif node.left:
		cnt += nextsum(curnsum, node.left, sum)
	elif node.right:
		cnt += nextsum(curnsum, node.right, sum)
	
	return cnt


def traverse(node, sum):
	# init
	res = 0
	if not hasattr(node, 'check'):
		res += nextsum(0, node, sum)
		node.check = True

	if node.left and node.right:
		res += traverse(0, node.left, sum) + traverse(0, node.right, sum)
	elif node.left:
		res += traverse(0, node.left, sum)
	elif node.right:
		res += traverse(0, node.right, sum)
	
	return res
