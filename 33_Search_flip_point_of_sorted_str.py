class Solution:
	def search(self, nums, target):
		# init
		N = len(nums)
		ll = 0
		rr = N-1
		insortstr = False
		#! biase id for dichotomy
		biase = 0

		if N % 2 == 0:
			# even
			lr = N/2 - 1
			rl = N/2
		else:
			# odd 
			lr = int(N/2)
			rl = int(N/2) + 1
		
		# special case mid
		if N == 0:
			return -1

		# flipstr & find flip sub
		while(N >= 4):
			if nums[rr] < nums[rl]:
				# flip point in right substr
				if nums[rr] == target:
					return rr
				elif nums[rl] == target:
					return rl
				elif nums[rr] < target ^ nums[rl] < target:
					# target in right_flipstr
					nums = nums[(rl+1):(rr)]
				else:
					# target in sort str
					nums = nums[ll:(lr+1)]
					insortstr = True
					break
			
			else:
				# flip point in left substr
				if nums[ll] == target:
					return ll
				elif nums[lr] == target:
					return lr
				elif nums[ll] < target ^ nums[lr] < target:
					# target in left_flipstr
					nums = nums[(ll+1):lr]
				else:
					# target in sort str
					nums = nums[rl:(rr+1)]
					insortstr = True
					break

			N = len(nums)
			if N % 2 == 0:
				# even
				lr = N/2 - 1
				rl = N/2
			else:
				# odd 
				lr = int(N/2)
				rl = int(N/2) + 1

		# sorted str
		if insortstr:
			# two tree

		# N = 2,3 flipstr left
		for i in len(nums):
			if nums[i] == target:
				return i

		return -1

