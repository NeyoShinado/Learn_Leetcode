# Wrong
class Solution:
	def decodeString(self, s: str) -> str:
		if len(s) == 0:
			res = ""
		else:
			res = decode_once(s)

		return res


def decode_once(s: str) -> str:
	# init
	left = ""
	right = ""
	code_str = ""
	N = len(s)
	
	for l in range(N):
		if s[l] == "[":
			if l >= 1:
				left = s[0:(l-1)]
			cnt = int(s[l-1])
			for r in range(-1, -N, -1):
				if s[r] == "]":
					right = s[(r+1):N]
					code_str = s[(l+1):r]
					break

			if code_str:
				res = left + cnt * decode_once(code_str) + right
				break
		if l == N-1:
			res = s

	return res