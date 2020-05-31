class Solution:
	def moveZeroes(self, nums: List[int]) -> None:
		'''
		inplace
		'''
		# init
		N = len(nums)
		biase = 0

		for i in range(N):
			if nums[i-biase] == 0:
				nums.append(nums.pop(i-biase))
				biase += 1

