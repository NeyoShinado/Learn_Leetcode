'''
# Version0
# Brute Force
# 超时
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
'''


# Version1
# 快速排序（减而治之--分治思想的特例）
# TC: O(N), SC: O(1)原地排序
import random
class Solution:
    def quickSelect(self, a, l, r, index):
        q = self.randomPartition(a, l, r)
        if q == index:
            return a[q]
        else:
            return self.quickSelect(a, q+1, r, index) if q < index else self.quickSelect(a, l, q-1, index)
    def randomPartition(self, a, l, r):
        i = random.randint(l, r)
        a[i], a[r] = a[r], a[i]
        return self.partition(a, l, r)
    def partition(self, a, l, r):        
        x = a[r]
        i = l - 1
        for j in range(l, r):
            if a[j] < x:
                i += 1
                a[i], a[j] = a[j], a[i]
        i += 1
        a[i], a[r] = a[r], a[i]
        return i
            
    def findKthLargest(self, nums, k):
        return self.quickSelect(nums, 0, len(nums)-1, len(nums)-k)


# Version2
# 堆排序
# TC: O(NlogN), SC: O(logN)
# 第一版Not pass
class Solution:
	def findKthLargest(self, nums, k):
		heapSize = len(nums)
		self.buildMaxHeap(nums, heapSize)
		for i in range(len(nums)-1, len(nums)-k, -1):
			nums[0], nums[i] = nums[i], nums[0]
			heapSize -= 1
			self.maxHeapify(nums, 0, heapSize)
		return nums[0]

	def buildMaxHeap(self, a, heapSize):
		for i in range(heapSize//2, -1, --1):
			self.maxHeapify(a, i, heapSize)

	def maxHeapify(self, a, i, heapSize):
		l = i*2 + 1
		r = i*2 + 2
		largest = i
		if l < heapSize and a[l] > a[largest]:
			largest = r
		if largest != i:
			a[i], a[largest] = a[largest], a[i]
			self.maxHeapify(a, largest, heapSize)

# 调用heapq包的最小堆
from typing import List
import heapq


class Solution:

    # 使用容量为 k 的小顶堆
    # 元素个数小于 k 的时候，放进去就是了
    # 元素个数大于 k 的时候，小于等于堆顶元素，就扔掉，大于堆顶元素，就替换

    def findKthLargest(self, nums: List[int], k: int) -> int:
        size = len(nums)
        if k > size:
            raise Exception('程序出错')

        L = []
        for index in range(k):
            # heapq 默认就是小顶堆
            heapq.heappush(L, nums[index])

        for index in range(k, size):
            top = L[0]
            if nums[index] > top:
                # 看一看堆顶的元素，只要比堆顶元素大，就替换堆顶元素
                heapq.heapreplace(L, nums[index])
        # 最后堆顶中的元素就是堆中最小的，整个数组中的第 k 大元素
        return L[0]
