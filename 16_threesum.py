'''
# Version1
# Brute Force
# 该方法按照正负两组数之和的组合查找第三数
# 忽视了遍历过程中两两配对重复一次出现的情况，且要在组合和数组之间切换，异常复杂
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
# 给数组排序以略过重复的情况
# 遍历单一元素，按#两数之和#O(N)找出对应的所有组合
# 注：后期的遍历组合都与遍历过的元素无关，所以不会遗漏
# TC:O(N^2)  SC:O(1)
class Solution:
	def threeSum(self, nums:List[int]) -> List[List[int]]:
		#init 
		nums.sort()
		N = len(nums)
		res = []

		# special case
		if sum(nums[:3]) > 0 or sum(nums[-3:]) < 0:
			return res

		for i in range(N):
			# 去重
			if i > 0 and nums[i] == nums[i-1]:
				continue
			L = i + 1
			R = N - 1
			while R > L:
				Sum = nums[i] + nums[L] + nums[R]
				if  Sum == 0:
					res.append([nums[i],nums[L],nums[R]])
					while R > L and nums[R] == nums[R-1]:
						R -= 1
					while R > L and nums[L] == nums[L+1]:
						L += 1
					R -= 1
					L += 1
				elif Sum > 0:
					R -= 1
				else:
					L += 1
		return res
