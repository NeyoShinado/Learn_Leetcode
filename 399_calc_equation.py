'''
# Version 0
# 需要找到可达的字符集，转化为路径搜索问题
# No pass
class Solution:
	def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
'''


# Version 1
# 构造图 + DFS搜索
#!每次query叠乘边的权重
# 对于“a/b=k”，a到b的有向边赋k，b到a的有向边赋1/k
# 路径不可达就返回-1
# TC: O(N), SC: O(N)
class Solution:
	def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
		graph = {}
		## 构造双向图
		#*zip 打包遍历双循环变量
		for(x,y), v in zip(equations, values):
			#*两层集合实现双向图
			if x in graph:
				graph[x][y] = v
			else:
				graph[x] = {y:v}
			if y in graph:
				graph[y][x] = 1/v
			else:
				graph[y] = {x:1/v}

		# 深度搜索可行路径
		# 定义类间函数，能使用全局变量
		def dfs(s, t) -> int:
			if s not in graph or t not in graph:
				return -1
			if t == s:
				return 1

			for node in graph[s].keys():
				if node == t:
					return graph[s][node]
				#!图的遍历需要查表记录，避免陷入环形循环
				elif node not in visited:
					visited.add(node)
					res = dfs(node, t)
					if res != -1:
						return graph[s][node] * res
			return -1

		res = []
		for qs, qt in queries:
			visited = set()
			res.append(dfs(qs, qt))
		return res