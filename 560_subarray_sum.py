'''
# Version 0
# Brute Force
# TC: O(N^2), SC: O(1)
class Solution:
	def subarraySum(self, nums: List[int], k: int) -> int:
		# init
		res = 0
		N = len(nums)
		sum = 0

		for L in range(N):
			sum = 0
			if sum == k:
				res += 1
			for R in range(L, N):
				sum += nums[R]
				if sum == k:
					res += 1

		return res
'''


# Version 1⭐
# 前缀和 + 哈希表索引
#*暴力解法的问题在于每一个点都需要枚举所有的子数组求和的重复计算量
#*动态规划中sum[i]的和都是由sum[i-1]+nums[i]构成的
#*即任意子数组和sum[i,j]可以表示为sum[j]-sum[i-1]只要差值为k，即为符合条件的数组起始点
#*所以只需要遍历一次数组，一边以和为关键字，次数为值记在哈希表中(索引速度快)，一边在表中查找符合条件的起始点
#*即dict[sum[i]-k]，加在计数器上
#*因为表的更新后于遍历指针移动，确保0≤i≤j，不会有前效性
#*注意：第一次k出现的时候需要0配对，所以字典初始化时要先把0：1写入
# TC: O(N), SC: O(N)
class Solution:
	def subarraySum(self, nums, k):
		res = 0
		map = {0:1}
		N = len(nums)
		cursum = 0
		
		for i in range(N):
			cursum += nums[i]
			if cursum - k in map:
				res += map[cursum-k]
			#*注意cursum[i]-k=cursum[i](即k=0)的特例，因此需要先找起始点再把和写入表内
			if cursum in map:
				map[cursum] += 1
			else:
				map[cursum] = 1
		return res
