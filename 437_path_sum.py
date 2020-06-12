# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
# Version 0
# No pass
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
'''


'''
# Version 1
# 递归实现
# TC: O(N^2), SC: O(N)
# 每条子路径都重复计算了一遍
class Solution:
	def pathSum(self, root, sum):
		if not root:
			return 0

		res = countpath(root, sum)
		Lres = self.pathSum(root.left, sum)
		Rres = self.pathSum(root.right, sum)
		return res+Lres+Rres

def countpath(root, sum):
	if not root:
		return 0

	sum = sum-root.val
	res = 1 if sum == 0 else 0
	return res+countpath(root.left, sum)+countpath(root.right, sum)
'''


# Version 2
# TS: O(N), SC: O(N)
# 前缀和 + 哈希表
# 前缀和指到达当前元素路径上的元素和，两个元素前缀和currSum相等，意味着中间节点的和为0
# 同理，若AB节点的currSum相差target，A到B之间元素之和为target
#*注：前缀和需要两节点间只有一条路径，适用于无环图
