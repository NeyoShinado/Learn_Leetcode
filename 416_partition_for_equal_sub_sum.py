'''
# Version 0
#! 问题转化为sum/2 的零钱问题
# TC: O(2^N), SC: O(N)
# 一般方法要2^N次确定能否匹配sum/2
# 递归遍历所有组合
# 超时
class Solution:
	def canPartition(self, nums: List[int]) -> bool:
		N = len(nums)
		total = sum(nums)
		total = total / 2
		if total % 1 != .0:
			return False

		if N <= 1:
			return False

		res = self.subsetsum(0, total, 0, N, nums)
		return res

	#* 类下函数定义时需要添加self参数
	def subsetsum(self, cursum, target, i, N, nums) -> bool:
		if i == N:
			return False

		if cursum == target or cursum+nums[i] == target:
			return True

		return self.subsetsum(cursum, target, i+1, N, nums) or self.subsetsum(cursum+nums[i], target, i+1, N, nums)
'''


'''
# Version 1
# 动态规划--背包问题
# not pass
# TC: O(NC), SC: O(NC).C 元素和的一半
class Solution:
	def canPartition(nums):
		N = len(nums)
		if N == 0:
			return False

		total = sum(nums)
		# 位运算确定奇偶数
		if total & 1 == 1:
			return False
		total = total / 2

		# N * (target+1) matrix recorde match res of diff interval
		dp = [[0] for i in range(N)]
		if nums[0] <= total:
			dp[0][nums[0]] = True

		for i in range(1, N):
			for j in range(int(total)):
				dp[i].append(dp[i-1, j])

				if nums[i] == j:
					dp[i][j] == true
					continue

				if nums[i] < j:
					dp[i][j] == dp[i-1][j] || dp[i-1][j-nums[i]]
		return dp[N-1][total]
'''


'''
# Version 2
# 背包
# TC: O(NC), SC: O(NC).C 元素和的一半
class Solution:
	def canPartition(self, nums):
		N = len(nums)
		total = sum(nums)
		if total % 2 == 1: return False
		#!整除返回的是整型
		target = total // 2

		#!列表生成多维矩阵
		# dp[i][j]代表用i个数能否组成和为j的bool值
		dp = [[False]*(target+1) for _ in range(N)]

		# 除了不选，没有构成0的正整数
		dp[0][0] = True
		if nums[0] <= target+1:
			dp[0][nums[0]] = True

		# 从1开始
		for i in range(1, N):
			for j in range(target+1):
				# 确保不越界
				if j >= nums[i]:
					#!从选i-1到选i个数的状态转移方程可分为：
					# 不选nums[i]，dp[i][j]取决于dp[i-1][j]；选择nums[i],dp[i][j]取决于dp[i-1][j-nums[i]]
					dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
				else:
					# dp[i][j]不能选nums[i]
					dp[i][j] = dp[i-1][j]
				#!只要最后一列有一个能符合，就能提前结束，剪枝操作
				if dp[i][target]:
					return true
		return dp[-1][-1]
'''


'''
# Version 3
# 背包，空间优化版
# TC: O(NC), SC: O(2C)
class Solution:
	def canPartition(self, nums):
		N = len(nums)
		total = sum(nums)
		if total % 2 == 1: return False
		target = total // 2

		pre = [False] * (target+1)
		cur = [False] * (target+1)

		pre[0] = True
		#!
		if nums[0] <= (target+1): pre[nums[0]] = True

		for i in range(1, N):
			for j in range(target+1):
				if j >= nums[i]:
					cur[j] = pre[j] or pre[j-nums[i]]
				else:
					cur[j] = pre[j]

			pre = cur
			cur = [False]*(target+1)

		return pre[-1]
'''


# Version 
# 背包，状态压缩至一维，同时从后往前填表
# 从后往前能提前找到不满足nums[i] <= j的情况，提前剪枝
# TC: O(NC), SC: O(C)
class Solution:
	def canPartition(self, nums):
		N = len(nums)
		if N == 0:
			return False

		total = sum(nums)
		if total&1 == 1:
			return False

		target = total // 2
		dp = [False] * (target+1)
		dp[0] = True

		if nums[0] <= target:
			dp[nums[0]] = True

		for i in range(1, N):
			for j in range(target, 0, -1):
				if nums[i] <= j:
					break

				if dp[target]:
					return True

				dp[j] = dp[j] or dp[j-nums[i]]
		return dp[target]