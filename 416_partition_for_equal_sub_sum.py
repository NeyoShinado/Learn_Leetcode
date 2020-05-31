#! 问题转化为sum/2 的零钱问题
# 关键在于一般匹配方法要N!次才能确定能否匹配sum/2
class Solution:
	def canPartition(self, nums: List[int]) -> bool:
