class Solution:
	def findKthLargest(self, nums: List[int], k: int) -> int:
		res = None
		N = len(nums)
		for i in range(N):
			for j in range((i+1), N):
				if nums[i] > nums[j]:
					nums[i] += nums[j]
					nums[j] = nums[i] - nums[j]
					nums[i] = nums[i] - nums[j]
		res = nums[-k]
		return res