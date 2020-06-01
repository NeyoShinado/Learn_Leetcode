class Solution:
	def subarraySum(self, nums: List[int], k: int) -> int:
		# init
		res = 0
		N = len(nums)
		sum = 0

		if N == 0:
			return res
		elif N == 1:
			if nums[0] == k:
				res += 1
			return res

		for L in range(N):
			sum = nums[L]
			if sum == k:
				res += 1
			for R in range(L+1, N):
				sum += nums[R]
				if sum == k:
					res += 1

		return res