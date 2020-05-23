'''
# Version1
# something wrong
class Solution:
	def maxArea(self, height: List[int]) -> int:
		n = len(height)
		sort_height = height.copy()
		sort_height.sort()
		res = 0
		# special case
		if(height[0] in sort_height[-3:-1] and height[-1] in sort_height[-3:-1]):
			vol = (n-1) * min(height[0], height[-1]) ** 2
			return vol

		for i in range(n-1):
			id = height.index(sort_height[i])
			longer = sort_height[(i+1):n]
			max_dist = 0
			for j in range(n-i-1):
				next_id = height.index(longer[j])
				dist = abs(next_id - id)
				if dist > max_dist:
					max_dist = dist
			vol = sort_height[i] ** 2 * max_dist
			if vol > res:
				res = vol
		return res
'''


# Version2
# Bi-pointer 双指针法
# 水桶容积受短木板限制，长木板内移只会减少容积
# 所以短木板向内移动，宽度减一，若新木板变长，容积有可能增大
# 两木板等长时移动哪一块效果都一样，如此遍历一次即可
class Solution:
	def maxArea(self, height: List[int]) -> int:
		i, j, res = 0, len(height)-1, 0
		while i<j:
			if(height[i] < height[j]):
				res = max(res, height[i] * (j-i))
				i += 1
			else:
				res = max(res, height[j] * (j-i))
				j -= 1
		return res