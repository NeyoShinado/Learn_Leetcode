'''
# Version 0
# not pass
class Solution:
	def topKFrequent(self, nums: List[int], k:int) -> List[int]:
		# init
		N = len(nums)
		cnt = []
		biase = 0

		if N == 1:
			res = nums
			return res
		cnt.append(nums[0])
		res = [1]

		for i in range(1, N):
			for j in range(len(cnt)):
				if nums[i] == cnt[j]:
					res[j] += 1
					id = j
					while id != 0 and res[id] >= res[id-1]:

						res[id-1] = res[id-1] + res[id]
						res[id] = res[id-1] - res[id]
						res[id-1] = res[id-1] - res[id]
						biase += 1
						id = id - 1
					cnt.insert(id-biase, cnt.pop(j))	
					biase = 0
				else:
					cnt.append(nums[i])
					res.append(1)

		res = res[0:k]
		return res
'''


# Version 1
# 排序算法按频率对元素排序


'''
# Version 2
# 最小堆
# TC: O(NlogK), SC: O(K)
# 根节点索引为1
class Solution:
	def topKFrequent(self, nums, k) -> List[int]:
		# k: 堆的大小
		def shift_down(arr, node, k):
			#* 创建变量，在循环开头和结尾进行取值和赋值，减少代码冗余，2行代码完成换值和指针更新
			# 否则，在循环中进行替换共需要4行代码(交换值3行、更新指针1行)
			val = arr[node]
			# 最多下沉k层
			while node << 1 < k:
				child = node << 1
				# 交换左右孩子的较小者
				if child|1 < k and arr[child|1][1] < arr[child][1]:
					child |= 1
				# 与更小子节点比较
				if arr[child][1] < val[1]:
					arr[node] = arr[child]
					node = child
				else:
					break
			arr[node] = val

		def shift_up(arr, child):
			val = arr[child]
			while child >> 1 > 0 and val[1] < arr[child>>1][1]:
				arr[child] = arr[child>>1]
				child >>= 1
			arr[child] = val

		#*借助collections库统计频数
		stat = collections.Counter(nums)
		stat = list(stat.items())
		
		heap = [(0, 0)]
		# 建立堆，根节点索引1，方便寻址
		for i in range(k):
			heap.append(stat[i])
			shift_up(heap, len(heap)-1)
		for i in range(k, len(stat)):
			if stat[i][1] > heap[1][1]:
				heap[1] = stat[i]
				shift_down(heap, 1, k+1)
		return [item[0] for item in heap[1:]]
'''
'''
def heapSort(arr):
    arr = [0] + arr
    k = len(arr)
    for i in range((k-1)>>1, 0, -1):
        sift_down(arr, i, k) 
    for i in range(k-1, 0, -1):
        arr[1], arr[i] = arr[i], arr[1]
        sift_down(arr, 1, i)
    return arr[1:]
'''


'''
# Version 3
# 桶排序
# TC: O(N), SC: O(N)
class Solution:
	def topKFrequent(self, nums, k) -> List[int]:
		map = {}
		for i in nums:
			#* set_get
			map[i] = map.get(i, 0) + 1
		max_time = max(map.values())
		bucket = [[] for i in range(max_time+1)]

		for key, value in map.items():
			bucket[value].append(key)
		res = []
		for i in range(max_time, 0, -1):
			if bucket[i]:
				#* list_extend
				res.extend(bucket[i])
			if len(res) >= k:
				return res[:k]
'''


# Version 4
# Counter
from collections import Counter
class Solution:
	def topKFrequent(self, nums, k) -> List[int]:
		return [i[0] for i in Counter(nums).most_common(k)]