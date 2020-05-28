class Solution:
	def wordBreak(self, s:str, wordDict: List[str]) -> bool:
		# init
		N = len(s)
		L = 0

		for R in range(1, N):
			if s[L:R] in wordDict:
				L = R

		if L != R:
			return False
		else:
			return True
