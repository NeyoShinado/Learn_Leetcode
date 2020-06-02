class Solution:
	def dailyTemperatures(self, T: List[int]) -> List[int]:
		# init
		res = []
		N = len(T)
		max = 0
		temp = 0
		max_id = None
		temp_id = None

		if N == 0:
			return res
		elif N == 1:
			res.append(0)
			return res

		for i in range(N-1, -1, -1):
			if T[i] >= max:
				max = T[i]
				max_id = i
				res.insert(0, 0)

			else:
				if i < N-1 and T[i] < T[i+1]:
					res.insert(0, 1)
					temp = T[i+1]
					temp_id = i+1
				else:
					if T[i] < T[temp_id]:
						res.insert(0, temp_id-i)
					else:
						for id in range(temp_id, max_id+1):
							if T[id] > T[i]:
								res.insert(0, id-i)
								temp = T[id]
								temp_id = id
								break

		return res