class Solution:
	def sortColors(self, nums: List[int]) -> None:
		"""
		Do not return anything, modify nums in-place instead.
		"""
		mask = {0: 0, 1: 0, 2: 0}
		N = len(nums)

		for i in nums:
			if i in mask.keys():
				mask[i] += 1
			else:
				print("Unrecognized element!")

		nums[0:mask[0]] = [0] * mask[0]
		nums[mask[0]:(mask[0]+mask[1])] = [1] * mask[1]
		nums[(mask[0]+mask[1]):N] = [2] * mask[2]