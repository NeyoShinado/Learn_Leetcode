# 22'
# Version0
# 超时
'''
class Solution:
	def findDuplicate(self, nums: List[int]) -> int:
		res = None
		N = len(nums)

		if N == 2:
			res = nums[0]
			return res

		for i in range(N):
			for j in range(i+1, N):
				if nums[i] == nums[j]:
					res = nums[i]
					return res
'''


# Version1
# 关于计数的二分查找
# TC: O(NlogN), SC: O(1)
'''
class Solution:
	def findDuplicate(self, nums: List[int])-> int:
		N = len(nums)
		l = 1
		r = N-1
		res = -1

		while l <= r:
			mid = (l + r) >> 1
			cnt = 0
			for i in range(N):
				cnt += nums[i] <= mid

			if cnt <= mid:
				l = mid + 1
			else:
				# 查找差值>0 的左边界
				r = mid - 1
				res = mid
		return res
'''


'''
# Version2
#*快慢指针/Floyd判圈法
# TC: O(N), SC: O(1)
class Solution:
	def findDuplicate(self, nums: List[int]) -> int:
		slow = 0
		fast = 0

		slow = nums[slow]
		fast = nums[nums[fast]]
		while slow != fast:
			slow = nums[slow]
			fast = nums[nums[fast]]

		slow = 0
		while slow != fast:
			slow = nums[slow]
			fast = nums[fast]
		return slow
'''


# Version3
# 二进制位投票
# 
