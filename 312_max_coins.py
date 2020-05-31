# 每次戳乘积最大的那个气球
class Solution:
	def maxCoins(self, nums: List[int]) -> int:
		# init
		res = 0
		N = len(nums)
		map = []
		prod = 0 	# min product
		id = 0 		# index of min product

		if N == 0:
			return res
		elif N == 1:
			res = nums[0]
			return res

		# build pro map
		for i in range(N):
			if i == 0:
				map.append(nums[i] * nums[i+1])
			elif i == N-1:
				map.append(nums[i] * nums[i-1])
			else:
				map.append(nums[i] * nums[i+1] * nums[i-1])

		# choose max pro and update the map
		while map:
			N = len(nums)
			id = 0
			prod = 0
			for i in range(N):
				if prod < map[i]:
					prod = map[i]
					id = i
			res += prod
			if id > 0 and id < N-1:	# at least 3 nums
				map[id-1] = nums[id-1] * (nums[id-2] if id-2 >= 0 else 1) * nums[id+1]
				map[id+1] = nums[id+1] * (nums[id+2] if id+2 <= N-1 else 1) * nums[id-1]
				map.pop(id)
				nums.pop(id)
			elif id == 0:	# at least 1 nums
				if N >= 2:
					map[id+1] = nums[id+1] * (nums[id+2] if id+2 <= N-1 else 1)
				map.pop(id)
				nums.pop(id)
			elif id == N-1:		# at least 2 nums
				map[id-1] = nums[id-1] * (nums[id-2] if id-2 >= 0 else 1)
				map.pop(id)
				nums.pop(id)

		return res