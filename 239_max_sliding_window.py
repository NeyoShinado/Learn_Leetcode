# 20'
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    	N = len(nums)
    	res = nums[0]
    	# special case
    	if N == 1:
    		return res

    	for i in range(k, N):
