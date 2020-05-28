#! 要求O(N)以及inplace运算
class Solution:
	def singleNumber(self, nums:List[int]) -> int:
		map = {}
		N = len(nums)
		biase = 0

		for i in range(N):
			if nums[i-biase] in map:
				nums.pop(i-biase)
				biase += 1
			else:
				map[nums[i-biase]] = []

		res = nums[-1]
		return res
