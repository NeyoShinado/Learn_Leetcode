class Solution:
	def longestConsecutive(self, nums:List[int]) -> int:
		res = 0
		N = len(nums)
		# ele-list of min & max of seq, and list is sorted by min
		sort_set = []

		if N == 0:
			return res
		else:
			sort_set.append([nums[0]*2])

		for i in nums:
			# 从小到大
			for j in range(len(sort_set)):
				if i == sort_set[j][0] - 1:
					sort_set[j][0] = i
					if j != 0 and sort_set[j-1][1] == i-1:
						sort_set[j][0] = sort_set[j-1][0]
						del sort_set[j-1]
						break
				elif i == sort_set[j][1] + 1:
					sort_set[j][1] = i
					if j != len(sort_set)-1 and sort_set[j+1][0] == i+1:
						sort_set[j][1] = sort_set[j+1][1]
						del sort_set[j+1]
						break
				elif i >= sort_set[j][0] and i <= sort_set[j][1]:
					continue
				elif i < sort_set[j][0] and j == 0:
					sort_set.insert(j, [i]*2)
					break
				elif i > sort_set[j][1] and j == len(sort_set):
					sort_set.append([i]*2)
		
		for i in sort_set:
		    res = max(i[1] - i[0] + 1, res)

		return res			
