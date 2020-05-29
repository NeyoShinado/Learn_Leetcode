# 30'
class Solution:
	def numIslands(self, grid: List[List[str]]) -> int:
		# init
		L = None
		R = None
		connect = []		#* list shows the connect sit of downline
		res = 0
		map = []

		M = len(grid)		# row
		if M == 0:
			return res
		N = len(M[0])		# col

		# line scan
		for i in range(M):
			l = grid[i]
			map.append([])
			for j in range(N):
				if l[j] == "1" and not L:
					L = j
					continue
				elif l[j] == "1" and not R:
					R = j
					map[i].append([L, R])
					L = None
					R = None

		# edge merge
		for i in range(1, M):
			if i == 1:
				down_line = map[i-1]
			up_line = map[i]
			[res, down_line] = edge_merge(up_line, down_line, connect, res)

		return res

def edge_merge(up, down, connect, cnt):

