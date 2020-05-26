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