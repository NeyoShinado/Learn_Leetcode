'''
# Version1
class Solution:
	def uniquePaths(self, m: int, n: int) -> int:
		# i,j is the row col location of start point
		i = 1
		j = 1
		N = paths(i, j, m, n)
		return N

def paths(i, j, m, n):
	if i == m or j == n:
		# only one path, add from the outer loop
		return 1
	else:
		return paths(i+1, j, m, n) + paths(i, j+1, m, n)
'''

