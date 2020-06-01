class Solution:
	def findUnsortedSubarray(self, nums: List[int]) -> int:
		# init
		res = 0
		N = len(nums)
		L = 0
		R = N-1

		if N < 2:
			return res

		while nums[L] <= nums[L+1]:
			L += 1
			if L == N-1:
				return res

		while nums[R] >= nums[R-1]:
			R -= 1
			if R == 0:
				return res

		min_sel = nums[L+1]
		max_sel = nums[L+1]
		for i in range(L+1, R):
			min_sel = min(min_sel, nums[i])
			max_sel = max(max_sel, nums[i])

		#* special case
		if L == R-1:
			res = 2
			return res

		while nums[L] > min_sel:
			L -= 1
			if L == 0:
				break

		while nums[R] < max_sel:
			R += 1
			if R == N-1:
				break

		res = R - L - 1
		return res 
