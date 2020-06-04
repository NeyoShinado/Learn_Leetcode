'''
# Version 0
# Not pass
# 保证nums[0:i],nums[(j+1):N]是升序的
# 且nums[i:j]的最小值大于nums[i],最大值小于nums[j+1]
# 两端遍历直到子序列长度最小
class Solution:
	def findUnsortedSubarray(self, nums: List[int]) -> int:
		# init
		res = 0
		N = len(nums)
		L = 0
		R = N-1

		if N < 2:
			return res

		while nums[L] <= nums[L+1]:
			L += 1
			if L == N-1:
				return res

		while nums[R] >= nums[R-1]:
			R -= 1
			if R == 0:
				return res

		min_sel = nums[L+1]
		max_sel = nums[L+1]
		for i in range(L+1, R):
			min_sel = min(min_sel, nums[i])
			max_sel = max(max_sel, nums[i])

		#* special case
		if L == R-1:
			res = 2
			return res

		while nums[L] > min_sel:
			L -= 1
			if L == 0:
				break

		while nums[R] < max_sel:
			R += 1
			if R == N-1:
				break

		res = R - L - 1
		return res 
'''


'''
# Version 1
# Brute Force二次遍历
# 遍历所有元素nums[i]，确定其是否在其他子数组的正确位置，不是就记录索引；
# 直到确定最大无序数组的左右边界
# TC: O(N^2), SC: O(1)
class Solution:
	def findUnsortedSubarray(self, nums):
		N = len(nums)
		L = N-1
		R = 0
		for i in range(N-1):
			for j in range(i+1, N):
				if nums[j] < nums[i]:
					R = max(R, j)
					L = min(L, i)
		res = 0 if R-L<=0 else R-L+1
		return res
'''


'''
# Version 2
# 排序
# TC: O(NlogN), SC: O(N)
class Solution:
	def findUnsortedSubarray(self, nums):
		sorted_nums = nums.copy()
		sorted_nums.sort()
		N = len(nums)
		L = N
		R = 0

		for i in range(N):
			if sorted_nums[i] != nums[i]:
				L = min(L, i)
				R = max(R, i)

		res = 0 if R-L<0 else R-L+1
		return res
'''


'''
# Version 3
# 栈
# 不用把所有数的大小关系都知道，只需要知道无序数组中最大值
# 和最小值对应的正确位置，就知道无序数组应该从哪里开始改动
# 用栈正序遍历一次找到最小值，再出栈以确定其正确位置，最大值同样逆序操作一遍
# TC: O(N), SC: O(N)
class Solution:
	def findUnsortedSubarray(self, nums):
		stack = []
		N = len(nums)
		L = N
		R = 0

		for i in range(N):
			while stack and nums[stack[-1]] > nums[i]:
				L = min(L, stack.pop())
			stack.append(i)		# 顺便解决了单元素情况

		stack = []
		for i in range(N-1, -1, -1):
			while stack and nums[stack[-1]] < nums[i]:
				R = max(R, stack.pop())
			stack.append(i)
		res = 0 if R <= L else R-L+1
		return res
'''


# Version 4
# 与上述同一思路
# 两次遍历，一次找最大最小值，一次确认位置


# Version 5
# 一次遍历版本
# https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/solution/shi-jian-chao-guo-100de-javajie-fa-by-zackqf/