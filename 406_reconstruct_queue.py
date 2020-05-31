#! 先将k从小到大按值的大小从小到大排，
# 可能要两端匹配以避免上述没考虑后方排序的问题
class Solution:
	def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
