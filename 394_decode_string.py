'''
# Version 0
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
'''


'''
# Version 1
# 栈递归
#*注意解决位数大于1的数字
#*不能通过相邻的嵌套结构，编码字符串中有表意字符串，使用栈记录子串首尾位置会有
# 位置动态变化以及要区分表意实意字符的问题
# TC: O(N), SC: O(N)
class Solution:
	def decodeString(self, s:str) -> str:
		# init
		N = len(s)
		stack = []
		num_stack = [] # for nested bracket
		res = ""
		temp = ""
		num = ""
		end = 0
		num_index = 0 # for multi-bit num skip

		for i in range(N):
			# 编码字符
			#*注意双层循环中的重复遍历
			if i < num_index:
				continue
			#*边界条件
			if s[i] < 'a' and s[i] not in ['[', ']']:
				# 判断是否为数字
				for num_id in range(i, N-2):
					if s[num_id] != '[':
						num += s[num_id]
					else:
						num_index = num_id
						num_stack.append(int(num))
						#* 缓存变量要注意初始化、更新以及删除的时刻
						num = ""
						break

			elif s[i] == '[':
				stack.append(i+1)

			## 解码部分
			elif s[i] == ']':
				# 确定并复制的子字符串
				## 若是嵌套字符串，则加上未记载的后段子字符串
				if end == 0:
					temp = s[stack[-1]:i] * num_stack.pop()
				else:
					temp = (temp + s[end:i]) * num_stack.pop()

				## 判断解码字符串是否仍在嵌套结构内
				# 是：更新编码字符子串，记录当前结尾
				if len(stack) > 1:
					#* 注意区分表意实意字符，区别对待字符子串拼接的三种情况
					temp = s[stack[-2]:(stack[-1]-2)] + temp
					end = i+1
				# 否：将子串并入结果，清理嵌套缓存
				else:
					res += temp
					temp = ""
					end = 0
				
				# 推出栈
				stack.pop()
				
			# 正常字符
			else:
				if len(stack) == 0:
					res += s[i]

		return res
'''


'''
# Version 2
# 栈内操作
# not pass
# 识别数字(多数位)、左右括号，遇到右括号之前正常进栈；遇到右括号将
# 编码字符串出栈复制，直到编码字符串遍历完为止
# TC: O(S + s),S s 分别为解码字符串和原字符串长度
# SC: O(S)
class Solution:
	def decodeString(self, s:str) -> str:
		stk = []
		ptr = 0 
		N = len(s)

		while ptr < N:
			#* 多位数字没有考虑指针跳动
			char = s[ptr]
			if char.isdigit(): 
				# 数字进栈
				digit = getdigits(s, ptr)
				stk.append(digit)
			elif char.isalpha() or char == '[':
				# 字母进栈
				stk.append(ptr)
			else:
				# ]出栈
				substr = []
				while stk[-1] != '[':
					substr.append(stk.pop())

				substr = substr[::-1]
				stk.pop()
				reptime = stk.pop()
				substr = substr * reptime
				stk.append(substr)
			ptr += 1

		#! 列表转字符串用join(),字符串转列表用split()
		stk = ''.join(stk)

		return stk

def getdigits(s, id):
	res = ''
	while s[id].isdigit():
		res += s[id]
		id += 1

	res = int(res)
	return(res)
'''


'''
# Version 3⭐
# 辅助栈法
# TC: O(N), SC: O(N)
# 此算法其实是Version 1的优化版本，运用了动态规划的思想
#!通过栈保存嵌套编码字符串的现场--前部子字符串及复制次数，同时解决子串拼接的三种情况
# 同时通过算术进位完成多位数字的遍历，避免重复遍历和指针跳位的问题
class Solution:
	def decodeString(self, s:str) -> str:
		stack, res, multi = [], '', 0
		for c in s:
			if c == '[':
				stack.append([multi, res])
				res, multi = '', 0
			elif c == ']':
				cur_multi, last_res = stack.pop()
				res = last_res + cur_multi * res
			elif c.isdigit():
				# 算术上进位完成多位数字字符的遍历
				multi = multi * 10 + int(c)
			else:
				res += c

		return res
'''


# Version 4
# 递归，也用到了动态规划思想优化状态
#!递归函数返回嵌套结束的位置，解决了递归问题索引跳变的问题
class Solution:
	def decodeString(self, s: str) -> str:
		def dfs(s, i):
			res, multi = "", 0
			while i < len(s):
				if '0' <= s[i] <= '9':
					multi = multi * 10 + int(s[i])
				elif s[i] == '[':
					i, tmp = dfs(s, i + 1)
					res += multi * tmp
					# 乘数使用完要置零，避免影响并列编码乘数进位
					multi = 0
				elif s[i] == ']':
					return i, res
				else:
					res += s[i]
				i += 1
			return res
		return dfs(s,0)
