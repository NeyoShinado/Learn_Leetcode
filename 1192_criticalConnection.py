# Version 0
import sys
class Solution:
	def criticalConnections(self, N:int, connections:List[List[int]])->List[List[int]]:
		#* 只用一个preNode就能避免DFS的重复遍历问题
		def dfs(node, pre, graph, ranks, curRank, cycleEdges):
			# >=0 说明遍历过，是环形
			if ranks[node] >= 0:
				return ranks[node]

			#* 需要记录三个状态值
			#①环中各点的步数 -- ranks[node]
			#②DFS末端返回环的最低起点步数作为环点的标识 -- lowestRank
			# 保证归来时能识别出环，且不受分叉节点的影响(步数一定更多)
			#③归来返回的末端状态 -- lastRank：不能闭环肯定步数更多；闭环的肯定小于当前步数
			lowestRank = curRank
			ranks[node] = curRank

			# 先遍历所有邻点，看是否成环，都不成环就列为关键连接/或成环的连接记录起来
			for neighbor in graph[node]:
				if neighbor == pre:
					continue
				lastRank = dfs(neighbor, node, graph, ranks, curRank+1, cycleEdges)
				# 
				if lastRank <= curRank:
					cycleEdges.add((node, neighbor))
					lowestRank = min(lowestRank, lastRank)
			return lowestRank


		# init
		graph = [[] for _ in range(N)]
		for c in connections:
			graph[c[0]].append(c[1])
			graph[c[1]].append(c[0])

		# 类似于步数统计，是环形记为正数，不是环形在递归中被-1覆盖
		ranks = [-1 for _ in range(N)]
		# 记录所有环形的link
		cycleEdges = set()
		dfs(0, sys.maxsize, graph, ranks, 0, cycleEdges)

		result = []
		for c in connections:
			if (c[0], c[1]) not in cycleEdges \
				and (c[1], c[0]) not in cycleEdges:
				result.append(c)
		return result