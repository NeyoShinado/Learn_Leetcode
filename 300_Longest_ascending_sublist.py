'''
# Version 0
# not pass
class Solution:
	def lengthOfLIS(self, nums: List[int]) -> int:
		N = len(nums)
		helper = [0] * N 	#* 1 for pass
		length = 1

		if N == 0:
			res = 0
		else:
			ser_temp = 0
			res = 1

		for L in range(N-1):
			if helper[L]:
				continue
			length = 1
			ser_temp = nums[L]
			for R in range(L, N):
				#! 同一个元素有多种递增子序列
				if nums[R] > ser_temp:
					length += 1
					helper[R] = 1
					ser_temp = nums[R]
					#* res的更新要在内部循环，否则会错过最后一轮
					res = max(res, length)

		return res
'''

'''
# Version1
# 动态规划
# 此版本dp假设错了：nums[0:i]的最大LIS长度，这样会混淆区间内等长的LIS
class Solution:
	def lengthOfLIS(self, nums: List[int]) -> int:
		if not nums:
			return 0

		# init
		N = len(nums)
		dp = [0] * N
		dp[0] = 1

		# DP
		for i in range(1, N):
			dp[i] = dp[i-1] # 当前dp[i] 最起码等于dp[i-1]
			j = i-1
			while dp[j] == dp[i] and j >= 0:
				#* 这里出错了，dp[j]的最长子序列可能并不以nums[j]结尾
				#if nums[i] > nums[j]:
				#	dp[i] = dp[j] + 1
				#	break
				j -= 1
			# 找到当前最大子序列的结尾
			#* 这个做法也不可取，因为没有挑选出等长LIS中合适的LIS结尾和nums[i]对比
			j += 1
			if nums[j] < nums[i]:
				dp[i] = dp[j] + 1
		return dp[N-1]
'''
'''
# TC: O(N^2), SC: O(N)
class Solution:
	def lengthOfLIS(self, nums: List[int]) -> int:
		if not nums:
			return 0
		N = len(nums)
		dp = []

		for i in range(N):
			dp.append(1)
			for j in range(i):
				if nums[i] > nums[j]:
					dp[i] = max(dp[i], dp[j]+1)
		return max(dp)
'''


# Version 2
# 贪心 + 二分查找
# TC: O(NlogN), SC: O(N)
# 此版本其实解决了Version1未通过版的核心问题：
# 即遍历到nums[i]时，能知道nums[i]更新的应该是哪一个内部LSI的最大长度，以及该最大长度能否刷新目前的最大值
class Solution:
	def lengthOfLIS(self, nums: List[int]) -> int:
		d = []
		for n in nums:
			if not d or n > d[-1]:
				d.append(n)
			else:
				# 二分查找
				l, r = 0, len(d)-1
				loc = r
				while l <= r:
					mid = (l+r) // 2
					if d[mid] >= n:
						loc = mid	# 要查找大于n的d[loc]，即d[mid]>n时才能更新loc
						r = mid - 1 # 中值大就收缩右边界
					else:
						l = mid + 1 # 中值小就收缩左边界
				d[loc] = n
		return len(d)