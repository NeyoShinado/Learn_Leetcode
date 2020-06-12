'''
# Version 0 
# 
class Solution:
	def minWindow(self, s:str, t:str) -> str:
		res = ""
		s_set = set(s)
		match = False
		map = {}
		length = 0
		N = len(s)
		N_t = len(t)

		# special case
		if len(t) == 0:
			return res

		for char in t:
			if char not in s_set:
				return res
			if char in s_set and N == 1:
				res = s
				return res

		# searching
		for i in range(N):
			if s[i] in t:
				map[s[i]] = i

			# start match judge
			#* it will skip the first round cuz match check
			if not match:
				if N_t == len(map):
					match = True

			else:
				L = min(map.values())
				R = max(map.values())

				if not res and match:
					# init res
					res = s[L:(R+1)]
					length = R - L
					
				elif res and match:
					if (R - L) <= length:
						length = R - L
						res = s[L:(R+1)]

		return res
'''


'''
# Version 1
# 滑动窗口
# TC: O(N), SC: O(N)
class Solution:
	def minWindow(self, s, t):
		# init
		need = {}
		win = {}
		N = len(s)
		for char in t:
			need[char] = need[char]+1 if char in need.keys() else 1
		L = 0
		R = 0
		val = 0   # win 中满足need 的字符数
		start = 0
		length = N+1

		while R <= N-1:
			char = s[R]
			R += 1
			if char in need.keys():
				win[char] = win[char]+1 if char in win.keys() else 1
				if win[char] == need[char]:
					val += 1

			while val == len(need):
				if R - L < length:
					start = L
					length = R - L

				char = s[L]
				L += 1
				if char in need.keys():
					if win[char] == need[char]:
						val -= 1
					win[char] -= 1   # 因为match 时右指针停下，所以肯定不会过减

		if length == N+1:
			res = ""
		else:
			res = s[start:(start+length)]
		return res
'''


# Version 2
# 