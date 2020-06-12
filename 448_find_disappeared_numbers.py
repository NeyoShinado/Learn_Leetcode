'''
# Version 0
# TC: O(2N), SC: O(k) 元素集合的长度
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
'''


# Version 1
# 原址修改
#*由于元素范围[1,N]，可在数组|nums|对应索引i上取负(或者加N等类似哈希处理也可以)表示元素i是否出现过
# 因此，第一次遍历将独立元素转负，第二次遍历检索[1,N]的出现情况
# TC: O(N), SC: O(1)
class Solution:
	def findDisappearedNumbers(self, nums):
		N = len(nums)
		res = []

		for i in range(N):
			if nums[abs(nums[i]) - 1] > 0:
				nums[abs(nums[i]) - 1] *= -1
		
		for i in range(1, N+1):
			if nums[i-1] > 0:
				res.append(i)

		return res
