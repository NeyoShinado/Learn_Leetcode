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