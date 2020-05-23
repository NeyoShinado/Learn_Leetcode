'''
# Version1
# Brute Force
class Solution:
	def threeSum(self, nums: List[int]) -> List[List[int]]:
		# init
		pos = []
		neg = []
		zeros = []
		res = []
		N = len(nums)
		match = False
		# separate pos & neg
		for i in range(N):
			if nums[i] > 0:
				pos.append(nums[i])
			elif nums[i] < 0:
				neg.append(nums[i])
			else:
				zeros.append(nums[i])
		del nums

		# one shot match
		# 最多两个元素相同，设立全局flag实现内外循环跳过
		pos_set = set(pos)
		neg_set = set(neg)
		for i in pos_set:
			for j in neg_set:
				match = False
				twosum = i + j
				if twosum > 0:
					id = neg.index(j)
					#! python的列表赋值是快速赋值，做法是添加指针指向不可变对象
					#! 这里temp赋值以及后续的pop 操作都会影响到原来的对象
					#! 应该用copy 方法创建新列表
					temp = neg.copy()
					temp.pop(id)
					for h in set(temp):
						if h + twosum == 0:
							res.append([i, j, h])
							match = True
				elif twosum < 0:
					id = pos.index(i)
					temp = pos.copy()
					temp.pop(id)
					for h in set(temp):
						if h + twosum == 0:
							res.append([i, j, h])
							match = True
				else:
					if zeros:
						res.append([i, j, 0])
						match = True
				#! the single-sign num only match one time
				#! but how to skip the outer loop?
				if match:
					break
			if match:
				continue

		if len(zeros) >= 3:
			res.append([0, 0, 0])
		return res
'''


# Version2

