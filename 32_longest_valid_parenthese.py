'''
# Version1  ×
# 初步分析每个字串按照闭括号有漏配和过配两种情况，用开括号计数器尝试区分
# 过配则结束计数，对比前子串长度更新结果并重新开始下一子串
#！问题是计数遍历不知道子串的内部结构，子串开始的位置也就不能确定
# 所以不能解决漏配的情况
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
'''


'''
# Version2
# Brute Force
# 遍历所有子串，用栈验证子串是否合法
# TC: O(N^2)  SC: O(N)

class Solution:
	def longestValidParentheses(self, s):
		res = 0
		N = len(s)
		for i in range(N):
			for j in range(i+2, N, 2):
				if(isValid(s[i:j])):
					res = max(res, j-i)
		return res

def isValid(str):
		stack = []
		for char in str:
			if char == '(':
				stack.append(char)
			elif not stack and char == ')':
				stack.pop()
			else:
				return False
'''

'''
# Version3
# 动态规划
# TC: O(N), SC: O(N)
# 采用同Version1相近的思路，以空间换时间，使用数组记录当前长度缓存解决了Version1的问题。
# 首先有效子串长度都记录在')'对应的位置上。
# 遍历中有两种情况，'...()'型和'...))'型。
# 前者加上上一子串长度dp[i-2]加上当前子串长度2
# 后者类洋葱型当s[i-dp[i-1]-1]='('表示匹配成功,当前长度dp[i-1]+2加上上一子串长度dp[i-dp[i-1]-2]
class Solution:
	def longestValidParentheses(self, s):
		res = 0
		N = len(s)
		sub_len = [0] * N

		for i in range(1, N):
			# 初始条件在赋值过程中通过判断句解决
			if s[i] == ')':
				if s[i-1] == '(':
					sub_len[i] = (0 if i < 2 else sub_len[i-2]) + 2
				elif i - sub_len[i-1] > 0 and s[i-sub_len[i-1]-1] == '(':
					#*判断条件解决了过配情况
					sub_len[i] = sub_len[i-1] + (sub_len[i-sub_len[i-1]-2] if i-sub_len[i-1] >2 else 0) + 2
			res = max(res, sub_len[i])
		return res
'''


'''
# Version4
#！ Rejection stack
# 与所有字符串遍历不同，可以先将-1放入栈底，再把下标压入栈内作长度计算。
# 计数将从第一个元素开始，栈空时说明字符串已经不合法，应当拒绝。
# 把新的栈底再补满，计算下一字符串
#* 因为长度和首位差坐标差一，所以初始化时栈底放-1，后期放合法字符串前一字符坐标
#TC: O(N), SC: O(N)
class Solution:
	def longestValidParentheses(self, s):
		res = 0
		stack = []
		stack.append(-1)
		N = len(s)
		for i in range(N):
			if s[i] == '(':
				stack.append(i)
			else:
				stack.pop()
				if stack:
					res = max(res, i - stack[-1])
				else:
					stack.append(i)
		return res
'''


# Version 5
#* 双向遍历
# 单一计数器的问题是会丢失前面字符串的长度，这可以用双计数器解决
# 当两计数器等长时比较长度，一方过大时置零重新计数
# 但单向遍历不能处理漏配的情况，鉴于字符串都是一边缺失导致匹配不上的
# 反向再遍历一次就能解决
# TC: O(N), SC: O(1)
class Solution:
	def longestValidParentheses(self, s):
		left = 0
		right = 0
		res = 0
		for char in s:
			if char == '(':
				left += 1
			else:
				right += 1
			if left == right:
				res = max(res, 2*right)
			elif right >= left:
				left = 0
				right = 0

		left = 0
		right = 0
		for char in s[::-1]:
			if char == '(':
				left += 1
			else:
				right += 1

			if left == right:
				res = max(res, 2*left)
			elif left >= right:
				left = 0
				right = 0
		return res