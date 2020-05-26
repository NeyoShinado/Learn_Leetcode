class Solution:
	def merge(self, intervals: List[List[int]]) -> List[List[int]]:
		# init
		res = []

		# special case
		if len(intervals) == 0:
			return intervals

		while len(intervals) > 1:
			N = len(intervals)
			biase = 0
			L = intervals[0][0]
			R = intervals[0][1]
			for i in range(1, N):
				if L > intervals[i-biase][1] or R < intervals[i-biase][0]:
					continue
				else:
					L = min(L, intervals[i-biase][0])
					R = max(R, intervals[i-biase][1])
					#* pop 的对象很重要
					intervals.pop(i-biase)
					biase += 1

			res.append([L, R])
			intervals.pop(0)

		if intervals:
			res.append(intervals[0])

		return res