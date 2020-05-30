# 20'
# double side
class Solution:
	def productExceptSelf(self, nums: List[int]) -> List[int]:
		# init
		N = len(nums)
		res = [1]
		multi = 1

		for i in range(N-1):
			multi = multi * nums[i]
			res.append(multi)

		multi = 1
		for i in range(-1, -N, -1):
			multi = multi * nums[i]
			res[i-1] = res[i-1] * multi

		return res