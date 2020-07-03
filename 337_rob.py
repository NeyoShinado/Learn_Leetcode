'''
##打家劫舍问题
# Version 0
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
    	res = 0
    	node = root

    	while node != True:
    		node = all_check(root)
		    candid = sum (node all two step) and set node.check
	    	res = max(res, candid)
	    return res


#* add pre
def all_check(node):
	res = True
	if node:
		if hasattr(node, 'check'):
			if node.left:
				res = all_check(node.left)
			if res == True and node.right:
				res = all_check(node.right)
			elif res != True and node.right:
				continue
		else:
			res = node
	else:
		return True


#*
def two_step_sum(node):
	res = 0
	res = node.val + two_step_sum(node.left.left) + two_step_sum(node.left.right) + two_step_sum(node.right.left) + two_step_sum(node.right.right) + two_step_sum(node.pre.leftorright)
	return res
'''


'''
# Version 1
# 暴力动态规划
#!从如下最简单的子结构知有两种组合：①爷爷+孙子们偷的总数  ②儿子们偷的总数
#            爷爷
#     儿子1        儿子2
# 孙子1  孙子2  孙子3  孙子4
# 如此向上递归就有总共的最大金额
# 应该是TC: O(N^4), SC: O(N)
class Solution:
	def rob(self, root):
		if not root:
			return 0

		money = root.val
		if root.left:
			money += self.rob(root.left.left) + self.rob(root.left.right)

		if root.right:
			money += self.rob(root.right.left) + self.rob(root.right.right)

		return max(money, self.rob(root.left) + self.rob(root.right))
'''


'''
# Version 2
# 记忆化 + 解决重复子问题
# 上述暴力递归中，计算爷爷同时要计算2个儿子和4个孙子
# 计算儿子同时要计算孙子“和曾孙”，计算孙子同时要...
#!如此一个节点最多会重复计算三遍，这是重复子问题
# TC: O(N), SC: O(N)
class Solution:
	def rob(self, root) -> int:
		# 使用全局字典记录记忆
		memory = {}
		return robInternal(root, memory)

def robInternal(root: TreeNode, memory: dict):
	if not root:
		return 0

	if root in memory.keys():
		return memory.get(root)

	money = root.val
	if root.left:
		money += robInternal(root.left.left, memory) + robInternal(root.left.right, memory)
	if root.right:
		money += robInternal(root.right.left, memory) + robInternal(root.right.right, memory)

	money = max(money, robInternal(root.left, memory) + robInternal(root.right, memory))
	memory[root] = money

	return money
'''


# Version 3⭐
# 递归函数返回数组解决组合问题
#!进一步优化动态规划为两层的对比，省去孙子节点计算及记忆数据的传输时间
# 用二元数组表示当前总额，res[0]不偷当前节点，res[1]偷当前节点
#!子结构的状态转移方程为:
# 当前不偷--左孩子偷的+右孩子偷的
# 当前偷--当前偷的+左孩子不偷时的+右孩子不偷时的
# 注：当前节点不偷时，左右孩子最多的前与其偷不偷没有关系
class Solution:
	def rob(self, root):
		res = robInternal(root)
		return max(res[0], res[1])

def robInternal(root):
	if not root:
		return [0] * 2

	res = [0] * 2
	left = robInternal(root.left)
	right = robInternal(root.right)

	res[0] = max(left[0], left[1]) + max(right[0], right[1])
	res[1] = left[0] + right[0] + root.val

	return res