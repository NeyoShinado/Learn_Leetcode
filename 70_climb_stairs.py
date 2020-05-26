class Solution:
	def climbStairs(self, n: int) -> int:
		res = path(n)

		return res

def path(n):
	if n == 0 or n == 1:
		return 1
	elif n < 0:
		return 0
	else:
		return (path(n-1) + path(n-2))