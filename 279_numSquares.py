'''
# Version1
# Brute Force
# 由numSquares(n)=min(numSquares(n-a^2)+1)递归枚举所有可能的组合
# Not pass 爆栈
class Solution:
	def numSquares(self, n):
		square_nums = [i**2 for i in range(1, int(math.sqrt(n)+1))]

		def minNumsquares(k):
			if k in square_nums:
				return 1

			min_num = float('inf')

			for square in square_nums:
				if k < square:
					break
				new_num = minNumsquares(k-square)+1
				min_num = min(min_num, new_num)
			return min_num

		return minNumsquares(n)
'''


'''
# Version2
# TC: O(N*sqrt(N)), SC:O(N)
class Solution:
	def numSquares(self, n):
		square_nums = [i**2 for i in range(0, int(math.sqrt(n)+1))]

		dp = [float('inf')] * (n+1)
		dp[0] = 0

		for i in range(1, n+1):
			for square in square_nums:
				if i < square:
					break
				dp[i] = min(dp[i], dp[i-square]+1)
		return dp[-1]
'''


# Version3
# 贪心枚举优化
# 上述numSquares(N)返回最小组合数的确切值，需要枚举1~N中所有可能的平方和组合
# 贪心优化方案则从1~N遍历cnt判断N能否被cnt个平方数组合而成，一旦找到就是最小的组合数
# TC: O(N^(h/2)), SC: O(sqrt(N)), h为可能发生的最大递归次数
'''
class Solution:
	def numSquares(self, n):
		def is_divided_by(n, cnt):
			if cnt == 1:
				return n in square_nums

			for k in square_nums:
				if is_divided_by(n-k, cnt-1):
					return True
			return False

		square_nums = set([i*i for i in range(1, int(n**0.5)+1)])

		for cnt in range(1, n+1):
			if is_divided_by(n, cnt):
				return cnt
'''


# Version4
# 贪心+BFS
# N展开为sqrt(N)元N层(最多)树，每层节点是余数
# 与一般BFS不同的是，每层余数用set保存，而非通常的queue或list，能消除大量冗余
# TC: O(N^(h/2)),h为N元树的高度，SC: O(sqrt(N)^h)
class Solution:
	def numSquares(self, n):
		square_nums = [i*i for i in range(1, int(n**0.5)+1)]

		level = 0
		queue = {n}
		while queue:
			level += 1
			next_queue = set()
			for remainder in queue:
				for square_num in square_nums:
					if remainder == square_num:
						return level
					elif remainder < square_num:
						break
					else:
						next_queue.add(remainder-square_num)
			queue = next_queue
		return level

