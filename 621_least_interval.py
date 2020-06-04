# Not pass
# 忽略了两组或以上最多执行次数任务的情况
'''
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
'''


# Version1
# 设重复次数最高为M，前M-1 个任务单元至少长为n+1。
#!另需考虑最后一个单元的任务数
from collections import Counter

class Solution:
	def leastInterval(self, task: List[str], n: int) -> int:
		ct = Counter(task)
		nbucket = ct.most_common(1)[0][1]
		last_bucket_size = list(ct.values()).count(nbucket)
		res = (nbucket-1)*(n+1) + last_bucket_size

		return max(res, len(task))