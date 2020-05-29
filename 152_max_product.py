# 30'
class Solution:
	def maxProduct(self, nums: List[int]) -> int:
		#init
		N = len(nums)
		# be care of negative num
		pro = None
		subpro = None

		if N == 0:
			res = []
			return res
		res = nums[0]

		for i in range(N):
			res = max(res, nums[i])
			if nums[i] != 0:
			#init
				if not pro and nums[i] > 0:
					pro = nums[i]
				elif pro and nums[i] > 0:
					pro = pro * nums[i]
					res = max(res, pro)
				else:
					pro = None

				if not subpro:
					subpro = nums[i]
				else:
					#! 错了，奇数个负数的情况下要根据最大绝对值选
					subpro = nums[i] * subpro
					res = max(res, subpro)
			
			else:
				# restart when meet 0
				pro = None
				subpro = None			

		return res
