class Solution:
	def subsets(self, nums: List[int]) -> List[List[int]]:
		# return 2^n terms combinations
		#! init for the first round
		res = [[nums[0]]]
		N = len(nums)

		for i in nums[1:N]:
			# each round add i or don't add i for every element
			for j in res:
				# just append the add i term
				# cuz no i term already exist
				#* None type object error
				temp = j.copy()
				res.append(temp.append(i))
			res.append([i])
		res.append([])

		return res