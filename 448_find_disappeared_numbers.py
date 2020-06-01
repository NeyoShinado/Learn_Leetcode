class Solution:
	def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
		# init
		N = len(nums)
		map = [1] * N
		res = []

		if N == 0:
			return res

		for i in nums:
			if map[i-1]:
				map[i-1] = 0

		for i in range(N):
			if map[i]:
				res.append(i+1)

		return res