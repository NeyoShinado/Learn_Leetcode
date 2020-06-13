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
# 双层递归
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


'''
# Version 2
# TS: O(N), SC: O(N)
# 前缀和 + DFS + 哈希表 + 回溯
# 前缀和指到达当前元素路径上的元素和，两个元素前缀和currSum相等，意味着中间节点的和为0
# 同理，若AB节点的currSum相差target，A到B之间元素之和为target
#*注：前缀和需要两节点间只有一条路径，适用于无环图
class Solution:
	def pathSum(self, root, sum):
		mp = {}
		mp[0] = 1
		res = self.dfs(root, 0, mp, sum)
		
		return res

	def dfs(self, root, path_sum, mp, sum):
		if not root:
			return 0
		# 更新当前pathsum
		path_sum += root.val
		# 先查询符合值再更新路径和表，避免sum=0 时出错
		res = 0 if (path_sum - sum) not in mp.keys() else mp[path_sum - sum]
		# 更新路径和表，并给子树递归
		mp[path_sum] = 1 if (path_sum) not in mp.keys() else mp[path_sum]+1
		res += self.dfs(root.left, path_sum, mp, sum)
		res += self.dfs(root.right, path_sum, mp, sum)
		#！子树遍历完后要清除当前的前缀和，避免回溯到父节点后影响上一层
		# 因为当前前缀和是不属于前缀的
		mp[path_sum] -= 1

		return res
'''


# Version 3
# 回溯搜索
# TC: O(NlogN), SC: O(N)
class Solution:
	def pathSum(self, root, sum):
		def path_sum(root, target, map, curend):
			if not root:
				return 0

			cursum = 0
			res = 0
			map[curend] = root.val
			for i in range(curend, -1, -1):
				cursum += map[i]
				if cursum == target:
					res += 1

			res += path_sum(root.left, target, map, curend+1)
			res += path_sum(root.right, target, map, curend+1)
			return res

		map = [0] * 1000
		return path_sum(root, sum, map, 0)