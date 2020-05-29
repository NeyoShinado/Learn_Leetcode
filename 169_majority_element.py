# 12'
class Solution:
	def majorityElement(slef, nums: List[int]) -> int:
		#init
		map = {}
		N = len(nums)
		thre = int(N / 2)
		res = None

		if N == 0:
			return res
		if N <= 2:
			return nums[0]

		for i in nums:
			if i in map.keys():
				map[i] += 1
				if map[i] > thre:
					res = i
					return res
			else:
				map[i] = 1
