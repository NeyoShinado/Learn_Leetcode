# Version0
# 动态规划
# 维护一个[loc,w,h]二元矩阵记载当前行的矩形信息
# 状态设置得太复杂，要复杂的逻辑去维护
# dp[i][j] 型则简洁不少
# Not pass，应该是坐标处理问题
'''
class Solution:
	def maximalSquare(self, matrix: List[List[str]]) -> int:
		res = 0
		M = len(matrix)
		if M == 0:
			return res
		N = len(matrix[0])
		# with [loc, w, h] in each row of list
		# first dim is row map, second dim is map element
		map = []

		# scan
		for line in matrix:
			map.append([])
			for i in range(N):
				if line[i] == 1 and i == 0:
					map[-1].append([i, 1, 1])
				elif line[i] == 1 and nums[i-1] == 1:
					map[-1][-1][1] += 1
				else:
					map[-1].append([i, 1, 1])

		# match
		biase_up = 0
		biase_down = 0
		for row in range(1, N):
			for down_id in range(len(map[row])):
				if res >= 1 and map[row][down_id-biase_down][1] == 1:
					del map[row][down_id-biase_down]
					biase_down += 1
					continue
				elif map[row][down_id-biase_down][1] == 1 and res ==0:
					res = 1
					continue

				for up_id in range(len(map[row-1])):
					if res >= 1 and map[row-1][up_id-biase_up][1] == 1:
						del map[row-1][up_id-biase_up]
						biase_up += 1
						continue
					elif map[row-1][up_id-biase_up][1] == 1 and res ==0:
						res = 1
						del map[row-1][up_id-biase_up]
						biase_up += 1
						continue

					if map[row-1][up_id-biase_up][0] == map[row][down_id-biase_down][0] and map[row-1][up_id-biase_up][1] == map[row][down_id-biase_down][1]:
						# loc and weight match
						if map[row][down_id-biase_down][1] == map[row][down_id-biase_down][2] + 1:
							# square match
							res = max(res, map[row][down_id-biase_down][1] ** 2)
							del map[row][down_id-biase_down]
							biase_down += 1
							continue
						else:
							map[row][down_id-biase_down][2] += 1
							continue

		return res
'''


# Version1
# 暴力
# 每遇到1尝试将其作为左上角，在下新增一行在右新增一列尝试找最大正方形
# TC: O(MNmin(m,n)^2), SC: O(1)
class Solution:
	def maximalSquare(self, matrix: List[List[str]]) -> int:
		if len(matrix)==0 or len(matrix[0])==0:
			return 0

		# init
		M = len(matrix)
		N = len(matrix[0])
		x = 0
		y = 0
		l = 1
		res = 0

		# scan
		for i in range(M):
			for j in range(N):
				if matrix[i][j] == "1":
					stop = False
					l = 1
					res = max(res, 1)
					# sub-square search
					while not stop and i+l < M and j+l < N:
						res = max(res, l**2)
						l += 1
						for sx in range(i, i+l):
							if matrix[sx][j+l-1] != "1":
								stop = True
								break
						for sy in range(j, j+l):
							if stop or matrix[i+l-1][sy] != "1":
								stop = True
								break
		return res


class Solution:
	def maximalSquare(self, matrix):
		if len(matrix)==0 or len(matrix[0])==0:
			return 0
		
		l = 0
		M, N = len(matrix), len(matrix[0])
		for i in range(M):
			for j in range(N):
				if matrix[i][j] == "1":
					l = max(l, 1)
					max_l = min(M-i, N-j)
					for k in range(1, max_l):
						stop = False
						if matrix[i+k][j+k] == "0":
							break
						for m in range(k):
							if matrix[i+k][j+m] == "0" or matrix[i+m][j+k]=="0":
								stop = True
								break
						if not stop:
							l = max(l, k+1)
						else:
							break
		res = l ** 2
		return res