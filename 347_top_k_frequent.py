class Solution:
	def topKFrequent(self, nums: List[int], k:int) -> List[int]:
		# init
		N = len(nums)
		cnt = []
		biase = 0

		if N == 1:
			res = nums
			return res
		cnt.append(nums[0])
		res = [1]

		for i in range(1, N):
			for j in range(len(cnt)):
				if nums[i] == cnt[j]:
					res[j] += 1
					id = j
					while id != 0 and res[id] >= res[id-1]:

						res[id-1] = res[id-1] + res[id]
						res[id] = res[id-1] - res[id]
						res[id-1] = res[id-1] - res[id]
						biase += 1
						id = id - 1
					cnt.insert(id-biase, cnt.pop(j))	
					biase = 0
				else:
					cnt.append(nums[i])
					res.append(1)

		res = res[0:k]
		return res