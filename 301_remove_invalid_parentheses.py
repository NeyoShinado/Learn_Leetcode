# 组合输出问题
'''
# Version 1
# DFS
# TC:O(2^N) , SC:O(N),N为字符串长度
class Solution:
	
	def removeInvalidParentheses(self, s:str) -> List[str]:
		
		def dfs(s:str, st:int, l:int, r:int):
			N = len(s)
			# 返回第一个满足条件的结果并终止dfs，相当于最小删除量
			#！对于不存在合法匹配的结果，异常符号计数的清零会使字符串为空获只剩下字母，同样满足要求
			if l==0 and r==0:
				if check(s):
					res.append(s)
				return

			for i in range(st, N):
				#*去重
				if i-1 >= st and s[i] == s[i-1]:
					continue
				if l > 0 and s[i] == "(":
					dfs(s[0: i] + s[i+1: N], i, l-1, r)
				if r > 0 and s[i] == ")":
					dfs(s[0: i] + s[i+1: N], i, l, r-1)


		# 验证字符串合法性
		def check(s:str):
			cnt = 0
			for char in s:
				if char == "(":
					cnt += 1
				if char == ")":
					cnt -= 1
					if cnt < 0: return False

			return cnt == 0

		#！全局变量保存多结果问题的解
		res = ['']
		# 多余括号的类型
		left = 0
		right = 0
		#！分类统计多余及异常符号的数量
		for char in s:
			if char == "(":
				left += 1
			if char == ")":
				if left > 0:
					left -= 1
				else:
					right += 1

		# DFS
		#*要合法地删除多余/异常符号，且需要去重
		dfs(s, 0, left, right)

		return res
'''


'''
# Version 2
# BFS
# 
# DFS 考虑的是删除哪个括号，每个遍历都要进行到底；
# BFS 则考虑删除几个括号，一但达到需求（最小删除数）就停止
class Solution:
	def removeInvalidParentheses(self, s:str) -> List[str]:
		def isvalid(s: str) -> bool:
			cnt = 0
			for char in s:
				if char == "(": cnt += 1
				elif char == ")" and cnt > 0:
					cnt -= 1
				elif char == ")" and cnt <= 0:
					return False
			return cnt == 0

		# BFS
		level = {s}	# 使用集合去重
		while True:
			valid = list(filter(isValid, level))	# 筛选合法字符集
			if valid: return valid
			next_level = set()	# 集合去重
			for item in level:	# 遍历删除一个括号的结果集
				for i in range(len(item)):
					if item[i] in "()":
						next_level.add(item[:i] + item[i+1:])
			level = next_level
'''


# Version 3
# 通过双向扫描及顺序去重删除实现



