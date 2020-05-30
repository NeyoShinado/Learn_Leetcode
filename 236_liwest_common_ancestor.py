# 48'
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
		# init
		res = None
		height = 1
		node = root

		if p == root or q == root:
			res = root
			return res
		elif p == q:
			res = p
			return q

		# pq scan
		node = scan(node, height, p, q)

		# backtrack
		if p.height  == q.height:
			if p.parent == q.parent:
				res = p.parent
				return res
			else:
				node = p.parent

		elif p.height > q.height:
			node = p.parent
		else:
			node = q.parent

		while node != root:
			if node == q:
				res = q
				return res
			if node == p:
				res = p
				return res
			else:
				node.check = True
			node = node.parent
		
		# search commmon ancestor
		if p.height < q.height:
			node = p.parent
		else:
			node = q.parent
		while node!= root:
			if hasattr(node, 'check'):
				res = node
				return res
			else:
				node = node.parent
		res = root

		return res


def scan(node, height, p, q):
	node.height = height
	height += 1
	if node == p or node == q:
		return node
	else:
		if node.left:
			node.left.parent = node
			node.left = scan(node.left, height, p, q)
		if node.right:
			node.right.parent = node
			node.right = scan(node.right, height, p, q)