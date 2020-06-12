# Version 0
# 使用哈希表遍历所有子串
# 超时
'''
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


