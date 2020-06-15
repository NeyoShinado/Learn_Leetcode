<<<<<<< HEAD
=======
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


# Version 1
# 动态规划
# 
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
>>>>>>> 2641fde0ffa9857e0614f28db37286034c32f53d
