'''
# Version 0
# 需要找到可达的字符集，转化为路径搜索问题
# No pass
class Solution:
	def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
'''


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
'''



# Version 2
# 并查集
# Not pass
# 没有考虑图多分叉情况(含多个父节点)
class Pair:
	def __init__(self, str, val):
		self.str = str
		self.val = val
	def toString(self):
		return 'Pair{str=' + str + ', val=' + val + '}'
class UnionFind():
	def __init__(self):
		self.parent = {}
	def find(self, A):
		if A != self.parent[A].str:
			# 如果不是根节点，继续找
			p = self.find(self.parent[A].str)
			# 把A的父结点指向p，这是路径压缩
			self.parent[A].str = p.str
			self.parent[A].val *= p.val
		return self.parent[A]
	
	def union(self, A, B, val):
		if A not in self.parent and B not in self.parent:
			self.parent[A] = Pair(B, val)
			self.parent[B] = Pair(B, 1.0)
			return 
		# 如果A是独立的，就把A指向B
		if A not in self.parent:
			self.parent[A] = Pair(B, val)
			return
		# 如果B是独立的，就把B指向A:
		if B not in self.parent:
			self.parent[B] = Pair(A, 1.0/val)
			return 
		# 走到这里，A和B都在一个集合里
		rootA = self.find(A)
		rootB = self.find(B)
		if rootA != rootB:
			rootA.str = rootB.str
			rootA.val *= (val * rootB.val)

class Solution:
	def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
		equationsSize = len(equations)
		uf = UnionFind()
		for i in range(equationsSize):
			A = equations[i][0]
			B = equations[i][1]
			k = values[i]
			uf.union(A, B, k)
		queriesSize = len(queries)
		res = [-1] * queriesSize  
		for i in range(queriesSize):
			X = queries[i][0]
			Y = queries[i][1]
			if X not in uf.parent or Y not in uf.parent:
				continue
			rootX = uf.find(X)
			rootY = uf.find(Y)
			if rootX.str == rootY.str:
				res[i] = rootX.val / rootY.val
		return res



'''
# Version 3
# Floyd Algorithm
# TC: O(N^3), SC: O(N^2)
class Solution:
	def calcEquation(self, equations:List[List[str]], values: List[List[str]], queries: List[List[str]]) -> List[float]:
		# 集合建立等式映射关系
		res = []
		eqmap = {}
		strs = set()
		for i in range(len(equations)):
			eqmap[(equations[i][0], equations[i][1])] = values[i]
			eqmap[(equations[i][1], equations[i][0])] = 1/values[i]
			strs.add(equations[i][0])
			strs.add(equations[i][1])
		keys = eqmap.keys()

		# 初始化dp
		N = len(strs)
		elems = list(strs)
		dp = [[float("Inf") for _ in range(N+1)] for _ in range(N+1)]
		for i in range(1, N+1):
			for j in range(1, N+1):
				if (elems[i-1], elems[j-1]) in keys:
					dp[i][j] = eqmap[(elems[i-1], elems[j-1])]

		# Floyd
		for k in range(1, N+1):
			for i in range(1, N+1):
				for j in range(1, N+1):
					if dp[i][k] != float("inf") and dp[k][j] != float("inf"):
						dp[i][j] = dp[i][k] * dp[k][j]

			# query
			for i in range(len(queries)):
				num_q, den_q = queries[i][0], queries[i][1]
				if num_q not in strs or den_q not in strs:
					res.append(-1)
					continue
				id_num, id_den = elems.index(num_q), elems.index(den_q)
				tmp = dp[id_num+1][id_den+1] if dp[id_num+1][id_den+1] != float("inf") else -1
				res.append(tmp)
			return res
'''


# Version4
# BFS
# BFS的判断条件相较DFS的递归要复杂些，考虑下一层的递归节点及更新值合并在一起入列，
# 同时考虑以及本层的节点数、查询是否成功、停止条件等情况
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        from collections import defaultdict
        d = defaultdict(list)
        for i in range(len(equations)):
            for j in range(2):
                d[equations[i][j]].append((equations[i][1-j], values[i])) # 这里对同一个list的两个值互相构图
                values[i] = 1/values[i]
        res = []
        for querie in queries:
            start, end = querie[0], querie[1]
            if (start == end and start in d):
                res.append(1.0)
                continue
            deque = [(start, 1.0)]
            visited = set()
            n = len(res)
            while deque:
                s, num = deque.pop(0)
                if s in visited:
                    continue
                visited.add(s)
                for item in d[s]:
                    if item[0] == end:
                        res.append(num*item[1])
                        break
                    deque.append((item[0], item[1]*num))
            if len(res) == n:
                res.append(-1.0)
        return res 
