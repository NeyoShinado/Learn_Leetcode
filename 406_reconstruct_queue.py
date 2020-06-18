'''
# Version 0
# not finish
#! 先将k从小到大按值的大小从小到大排，
# 可能要两端匹配以避免上述没考虑后方排序的问题
class Solution:
	def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
'''		


# Version 1
# 贪心算法
# 先排列高的人，因为身高低的人对他们没影响；身高低的人直接以k值为索引插入队列
# TC: O(N^2)--排序使用O(NlogN),每人插入队列需要O(k),所有人插入需要O(N^2)
# SC: O(N)
class Solution:
	def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
		#! python sort+lambda 实现双关键字排序
		people.sort(key = lambda x: (-x[0], x[1]))
		output = []
		for p in people:
			output.insert(p[1], p)
		return output