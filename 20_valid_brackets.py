#* 原始问题是一种括号的匹配，合理情况是遍历时右括号的总数总≤
# 左括号的总数，这时只需要对左括号设置一个计数器就能解决问题
# 多括号的计数器没有考虑括号的先后顺序，因而行不通

'''
# Version1
# Brute Force
# 考虑到每个右括号肯定紧挨着对应的左括号
# 遍历一次字符串，遇到右括号先判定相邻括号是否匹配
# 初始化一个偏移变量，匹配就将该括号对抛出字符串，然后偏移量加2
# 遇到下一个右括号就减去偏移量再匹配，直到结束
# 缺点是会对原字符串有删减操作
# TC:O(N), SC:O(1)

class Solution:
	def isValid(self, s: str) -> bool:
		n = len(s)
		r_set = ')]}'
		#* changable str
		biase = 0
		# even check
		if n % 2 != 0:
			return False

		if n == 0:
			return True

		for i in range(1, n):
			# curren len
			m = len(s)
			id = i - biase
			#* specific l_r match
			if(s[id] in r_set and lr_match(s[id-1], s[id])):
				biase += 2
				if (id == 1):
					s = s[2:m]
				else:
					s = s[0:(id-1)] + s[(id+1):m]
			elif(s[id] in r_set and not lr_match(s[id-1], s[id])):
				return False

		if s:
			return False
		else:
			return True

def lr_match(l, r):
	if l == '(' and r == ')':
		return True
	if l == '{' and r == '}':
		return True
	if l == '[' and r == ']':
		return True

	return False
'''


# Version2
#* 该问题是递归结构，可以用数据栈结构
# 因为我们不清楚真正的整体嵌套结构
# 但是我们能用栈由外到内地处理递归问题
# TC:O(N), SC:O(N)
class Solution(object):
	def isValid(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		stack = []
		map = {")": "(", "}": "{", "]": "["}

		for char in s:
			if char in map:
				top_element = stack.pop() if stack else '#'
				if map[char] != top_element:
					return False
			else:
				stack.append(char)
		return not stack