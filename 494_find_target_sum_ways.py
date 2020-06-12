'''
# Version 0
# TC: O(2^N), SC: O(1)
# 根据每个位置上出现±的两种情况遍历2^N种方案
class Solution:
	def findTargetSumWays(self, nums: List[int], S:int) -> int:
		# init
		N = len(nums)
		res = 0

		for i in range(1, 2**N+1):
			id = 0
			summation = 0
			quotient = i
			if sum(nums[1:]) - nums[0] == S:
				res += 1
			while quotient != 1:
				resid = quotient % 2
				if resid == 1:
					summation = summation - nums[id]
				else:
					summation = summation + nums[id]
				quotient = quotient // 2
				
				if quotient == 0:
					summation = summation + sum(nums[id+1:])
				id += 1

			if summation == S:
				res += 1

		return res
'''


# Version 1
# 使用递归遍历所有排列
# 超时
# TC: O(2^N), SC: O(N) 栈空间层数
class Solution:
	def findTargetSumWays(self, nums, S):
		self.res = 0
		self.calculate(nums, 0, 0, S)
		return self.res

	def calculate(self, nums, i, sum, S):
		if i == len(nums):
			if sum == S:
				self.res += 1
		else:
			self.calculate(nums, i+1, sum + nums[i], S)
			self.calculate(nums, i+1, sum - nums[i], S)


# Version 2
# DFS(深度优先搜索)
# 


# Version 3
# 01背包
