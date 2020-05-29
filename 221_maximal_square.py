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