'''
# Brute Force
# TC: O(N^2), SC: O(1)
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
		for L in range(N):
			for R in range(L+1, N+1):
				res += check_palindrome(s[L:R])

		# for the last one char
		#res += 1

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
'''


'''
# Version 2
# 中心扩展法
# 等价于字符间隔中增'#' 扩展中心位置索引
# 如此奇偶字符串都能通过L = N//2, R = L + N%2实现匹配
# TC: O(N^2), SC: O(1)
class Solution:
	def countSubstrings(self, S):
		N = len(S)
		res = 0
		for center in range(2*N-1):
			L = center // 2
			R = L + center % 2
			while L >= 0 and R < N and S[L] == S[R]:
				res += 1 
				L -= 1
				R += 1
		return res
'''


# Version 3
# Manacher
# TC: O(N), SC: O(N)
class Solution:
	def countSubstrings(self, S):
		def manachers(S):
			A = '@#' + '#'.join(S) + '#$'
			Z = [0] * len(A)
			center = right = 0
			for i in range(1, len(A)-1):
				if i < right:
					Z[i] = min(right-i, Z[2*center - i])
				while A[i + Z[i] + 1] == A[i - Z[i] - 1]:
					Z[i] += 1
				if i + Z[i] > right:
					center, right = i, i + Z[i]
			return Z
		res = sum((v+1)/2 for v in manachers(S))
		return res