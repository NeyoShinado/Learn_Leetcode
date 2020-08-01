# Version3
class Solution:
	def findDuplicate(self, nums:List[int]) -> int:
		N = len(nums)
		res = 0
		bit_max = 31
		while !((N-1) >> bit_max):
			bit_max -= 1

		for bit in range():
			x = 0
			y = 0
			for i in range(N):
				if (nums[i] & ()):
					x += 1
				if (i >= ):
					y += 1

			if x > y:
				res |= 1 << bit

		return res