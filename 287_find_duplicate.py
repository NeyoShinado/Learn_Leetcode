# 22'
class Solution:
	def findDuplicate(self, nums: List[int]) -> int:
		res = None
		N = len(nums)

		if N == 2:
			res = nums[0]
			return res

		for i in range(N):
			for j in range(i+1, N):
				if nums[i] == nums[j]:
					res = nums[i]
					return res