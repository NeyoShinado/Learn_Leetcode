'''
# Version 0
# 超时
class Solution:
	def findAnagrams(self, s: str, p: str) -> List[int]:
		# init
		res = []
		p_map = {}
		map = {}
		Np = len(p)
		N = len(s)
		L = 0

		for i in p:
			if i in p_map:
				p_map[i] += 1
			else:
				p_map[i] = 1

		# start traverse
		while L != N-Np+1:

			for R in range(L, L+Np):
				if s[R] not in p_map:
					L = R+1
					map = {}
					break

				if s[R] in map:
					if len(map[s[R]]) < p_map[s[R]]:
						map[s[R]].append(R)
					else:
						L = map[s[R]][0]
						map = {}
						break
				else:
					map[R] = [L]

				if R-L == Np-1:
					res.append(L)
					L += 1
		return res
'''


# Version 1
# 滑动窗口
# TC: O(N), SC:(N)
class Solution:
	def findAnagrams(self, s, t):
		#init
		need = {}
		win = {}
		for char in t:
			need[char] = need[char]+1 if char in need.keys() else 1
		res = []
		val = 0
		L = 0
		R = 0
		N = len(s)
		Nt = len(t)

		while R < N:
			char = s[R]
			R += 1
			if char in need.keys():
				win[char] = win[char]+1 if char in win.keys() else 1
				if win[char] == need[char]:
					val += 1

			while  R-L >= Nt:
				if val == len(need):
					res.append(L)
				
				# shrink window
				char = s[L]
				L += 1
				if char in need.keys():
					if win[char] == need[char]:
						val -= 1
					win[char] -= 1
		return res
