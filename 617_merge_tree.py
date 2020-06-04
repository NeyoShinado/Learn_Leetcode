# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Version 0
# 栈溢出
# TC: O(N), SC: O(N)最坏情况需递归N层栈空间
'''
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
'''


'''
# Version 1
# 递归
# 前序遍历：上-左-右
# TC: O(N),最少节点数；SC: O(D)树的最少层数

class Solution:
	def mergeTrees(self, t1: TreeNode, t2: TreeNode):
		if not t1 and t2:
			return t2

		elif t1 and t2:
			t1.val += t2.val
			t1.left = self.mergeTrees(t1.left, t2.left)
			t1.right = self.mergeTrees(t1.right, t2.right)

		return t1
'''


# Vserion 2
# 迭代
# 会稍慢，因为不借助额外空间无法完成回溯
class Solution:
	def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
		if not t1:
			return t2
		stack = [[t1, t2]]

		while stack:
			node = stack.pop()
			if (not node[0]) or (not node[1]):
				continue
			node[0].val += node[1].val
			if not node[0].left:
				node[0].left = node[1].left
			else:
				stack.append([node[0].left, node[1].left])

			if not node[0].right:
				node[0].right = node[1].right
			else:
				stack.append([node[0].right, node[1].right])

		return t1