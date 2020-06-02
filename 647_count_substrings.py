class Solution:
	def countSubstrings(self, s: str) -> int:
		# init
		res = 0
		N = len(s)

		# special case
		if N == 0:
			return res
		elif N == 1:
			res = 1
			return res

		# traverse
		for L in range(N-1):
			for R in range(L+1, N):
				res += check_palindrome(s[L:R])

		# for the last one char
		res += 1

		return res


def check_palindrome(s: str) -> int:
	res = 0
	N = len(s)
	L = 0
	R = N-1

	if L == R:
		res = 1
		return res

	while L < R:
		if s[L] == s[R]:
			L += 1
			R -= 1
		else:
			return res

	res = 1

	return res