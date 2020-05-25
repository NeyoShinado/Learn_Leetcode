class Solution:
	def canJump(self, nums):
		# init 
		d = []
		N = len(nums)

		for i in range(-2, -(N+1), -1):
			if nums[i] == 0:
				# 是0点就加到d中
				N_d = len(d)
				for j in range(N_d):
					d[j] += 1
				d.append(1)
			else:
				# 非零点就把d中的0点消去
				if d:
					N_d = len(d)
					biase = 0
					for j in range(N_d):
						if nums[i] <= d[j-biase]:
							# no pass
							d[j-biase] += 1
						else:
							# pass
							#! be careful of pop's effect on id
							d.pop(j-biase)
							biase += 1
				else:
					continue

		if d:
			return False
		else:
			return True

