class Solution:
	def leastInterval(self, task: List[str], n: int) -> int:
		# init
		round = 0
		N = len(task)
		map = {}
		res = 0

		if N == 0:
			return res

		for i in task:
			if i in map:
				map[i] += 1
			else:
				map[i] = 1
		
		repN = map[max(map)]
		round = repN - 1
		#!
		max_inter = round * (n+1) + 1

		if N - repN <= round * n:
			res = max_inter
		else:
			res = N

		return res