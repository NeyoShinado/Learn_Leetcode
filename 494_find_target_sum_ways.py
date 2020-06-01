class Solution:
	def findTargetSumWays(self, nums: List[int], S:int) -> int:
		# init
		N = len(nums)
		res = 0

		for i in range(1, 2**N+1):
			id = 0
			summation = 0
			quotient = i
			if sum(nums[1:]) - nums[0] == S:
				res += 1
			while quotient != 1:
				resid = quotient % 2
				if resid == 1:
					summation = summation - nums[id]
				else:
					summation = summation + nums[id]
				quotient = quotient // 2
				
				if quotient == 0:
					summation = summation + sum(nums[id+1:])
				id += 1

			if summation == S:
				res += 1

		return res