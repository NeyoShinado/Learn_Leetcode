#！
class Solution:
	def longestValidParentheses(self, s):
		#init
		cnt = 0
		N = len(s)
		length = 0
		len_sub = 0
		len_last = 0

		#special case
		if len(set(s)) == 1:
			return 0

		for char in s:
			if char == "(":
				cnt += 1
			elif char == ")":
				cnt -= 1
				# 前串+当前串长度后，当前串置零
				if cnt == 0:
					len_sub += 1
					len_last = 2*len_sub + len_last
					len_sub = 0
					#* 结束时当前串已变为前串
					length = max(length, len_last)
				# 当前串增长
				#！漏配情况未能解决
				elif cnt > 0:
					len_sub += 1
					length = max(length, 2*len_sub)
				# 过配，前串丢失置零，当前串长度和计数器也置零
				else:
					len_last = 0
					len_sub = 0
					cnt = 0
		return(length)

