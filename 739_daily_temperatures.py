# Brute Froce
# 从后往前遍历，根据距离由近至远依次与明天、气温超过明天的暂高天以及遍历过来气温最高的天数对比
# 以此尽可能减少每次遍历对比的次数
# TC: O(N^2), SC: O(1)
'''
class Solution:
	def dailyTemperatures(self, T: List[int]) -> List[int]:
		# init
		res = []
		N = len(T)
		max = 0
		temp = 0
		max_id = None
		temp_id = None

		if N == 0:
			return res
		elif N == 1:
			res.append(0)
			return res

		for i in range(N-1, -1, -1):
			if T[i] >= max:
				max = T[i]
				max_id = i
				res.insert(0, 0)

			else:
				if i < N-1 and T[i] < T[i+1]:
					res.insert(0, 1)
					temp = T[i+1]
					temp_id = i+1
				else:
					if T[i] < T[temp_id]:
						res.insert(0, temp_id-i)
					else:
						for id in range(temp_id, max_id+1):
							if T[id] > T[i]:
								res.insert(0, id-i)
								temp = T[id]
								temp_id = id
								break

		return res
'''

'''
# Version 2
# 简化边界条件版Brute Force
# 同样逆序遍历，且设定最近的高温索引表，取里面的最小索引值
# TS: O(NW),W为索引表的长度，CS: O(N+W)
class Solution(object):
	def dailyTemperatures(self, T):
		# 气温在[30-100]，指代表的索引
		# 102默认长度为了在100度最高温仍能返回正确的逻辑值
		nxt = [float('inf')] * 102 
		ans = [0] * len(T)
		for i in range(len(T)-1, -1, -1):
			warmer_id = min(nxt[t] for t in range(T[i]+1, 102))
			if warmer_id < float('inf'):
				ans[i] = warmer_id - i
			nxt[T[i]] = i

		return ans
'''


'''
# Version 3
# 栈
# 因为升温天数只需知道比T[i]高的日期，后面比T[i]高的日期无需比较
#*问题类型是无前效性，可以通过先进后出的单调栈实现，栈内记住日期索引，
# 且索引代表的气温是严格递增的
# TS: O(N), SC: O(W) W是T[i]的取值数目
# 解法的缺点是反向遍历，不符合实际
class Solution:
	def dailyTemperatures(self, T):
		res = [0] * len(T)
		stack = []
		for i in range(len(T)-1, -1, -1):
			while stack and T[i] >= T[stack[-1]]:
				stack.pop()
			if stack:
				res[i] = stack[-1] - i
			stack.append(i)
		return res
'''


# Version 4
# 正序遍历 + 栈
# TS: O(N), SC: O(W)
# 栈转而存储待比较的日期，保证日期是递减的
# 随着t的右移，所有气温小于t的最近日期都会被处理掉
# 这里的栈是先进先出，所以能正序遍历解决问题
class Solution:
	def dailyTemperatures(self, T: List[int]) -> List[int]:
		N = len(T)
		stack = []
		res = [0] * N

		for id, t in enumerate(T):
			while stack and t > T[stack[-1]]:
				res[stack.pop()] = id - stack[-1]
			stack.append(id)
		return res