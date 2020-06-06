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


'''
# Version 1(not pass)
# 每个点的新值等于原点和右节点之和，原节点和左节点分开递归
# TC: O(N), SC: O(H)
class Solution:
	def convertBST(self, root):
		def cumsum(node):
			if not node: return 0
			node.val = node.val + cumsum(node.right)

			if node.left:
			#！问题出现在递归按层从下往上进行，导致左子树不能加上父节点的累加值(即外层节点的和)
				node.left.val = node.val + cumsum(node.left)
			return node.val

		res = cumsum(root)
		return root
'''


'''
# Version 2
# 回溯算法(思路同上一样)
# 搜索二叉树的一个特性就是子树的所有节点都小于/大于根节点值
# 反序中序遍历所有节点，先递归右子树的点(较大值)，再递归左子树(较小值)
# TC: O(N), SC: O(N) 可能的最大层数是N
class Solution:
	def __init__(self):
		self.total = 0

	def convertBST(self, root):
		if root is not None:
			self.convertBST(root.right)    # inplace operation
			self.total += root.val
			root.val = self.total
			self.convertBST(root.left)
		return root
'''


'''
# Version 3
#!栈迭代实现
# 使用先进后出栈实现递归，且使用两层循环记录
# 内层循环想记录所有的右子树中序节点，再通过外层循环逐一将中序节点的左子树遍历
# 指针为空说明左\右子树已遍历完成，推出下一个左子树节点\中序节点
# 指针和栈都为空说明遍历结束，返回结果
# TC: O(N), SC: O(N)
class Solution:
	def convertBST(self, root):
		total = 0

		node = root
		stack = []
		while stack or node is not None:
			while node is not None:
				stack.append(node)
				node = node.right

			node = stack.pop()
			total += node.val
			node.val = total
			node = node.left

		return root
'''


# Version 4
# 反序中序Moris遍历
