# 60'
class Solution:
	def maxSubArray(self, nums):
		#init 
		N = len(nums)
		cur_sum = 0
		max_sum = 0
		cur_l = 0
		max_l = 0
		max_r = 0
		max_num = nums[0]

		if N == 1:
			return nums[0]

		for i in range(N):
			#！ 下面子串和没有考虑全负数组的情况
			if nums[i] > max_num:
				max_num = nums[i]

			# 正增负减
			if nums[i] <= 0:
				if cur_sum + nums[i] >= 0:
					cur_sum += nums[i]
					continue
				else:
					cur_sum = 0
					cur_l = i+1

			else:
				cur_sum += nums[i]
				if cur_sum > max_sum:
					max_sum = cur_sum
					max_r = i+1
					max_l = cur_l

		if max_num > 0:
			res = max(max_sum, max_num)
		else:
			res = max_num

		return res