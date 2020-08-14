# T1
class Solution:
	def Fast(self):
		# input
		N = int(input())
		nums = list(map(int, input().split()))
		Vs = list(map(int, input().split()))

		# init
		k = 0
		t = 0
		V = sum(nums)		# total goods
		maxBag = max(Vs)
		buckets = [[] for _ in range(maxBag)]

		# main loop
		# bucket sort
		for i in range(len(Vs)):
			buckets[Vs[i]].append(i)

		while V > 0:
			while not buckets[-1]:
				del(buckets[-1])
			# 同容量背包中先选装得最多的，转移量较少
			if len(buckets[-1]) > 1:
				for tmp in range(1, len(buckets[-1])):
					if nums[buckets[-1][tmp]] >= nums[buckets[-1][tmp-1]]:
						index = tmp
					else:
						index = tmp - 1
			else:
				index = 0
			index = buckets[-1][tmp]
			del(buckets[-1][tmp])
			
			V -= Vs[index]
			t += Vs[index] - nums[index]
			k += 1

		print(str(k) + " " + str(t))

if __name__ == "__main__":
	t = Solution()
	t.Fast()


# T2
class Solution:
	def longestPrefix(self):
		# input
		arr = []
		N = int(input())
		for i in range(N):
			arr.append(input())

		while True:
			try:
				x, y = list(map(int, input().split()))
				for i in range(min(len(arr[x-1]), len(arr[y-1]))):
					if arr[x-1][i] != arr[y-1][i]:
						i -= 1
						break
				print(str(i+1))
			except:
				break

if __name__ == "__main__":
	t = Solution()
	t.longestPrefix()


# T3
class Solution:
	def strSort(self):
		
		def swap(a, b):
			arr[a], arr[b] = arr[b], arr[a]

		def strCmp(s1, s2):
			# return True if s1 <= s2
			
		def mergeSort(s):



		# input
		arr = list(map(int, input().split(",")))
		N = len(arr)

		 # main
		# 归并排序
		ind = list(range(N))


#* T4
class Solution:
	def maxVal(self):
		# input

		N = int(input())
		L = [0]
		H = [0]
		for i in range(N):
			l, h = list(map(int, input().split()))
			L.append(l)
			H.append(h)

		# init
		F = [0 for _ in range(N+1)]
		res = 0

		# main
		if N == 0:
			print(str(0))
			return
		if N == 1:
			print(str(max(L[1], H[1])))
			return

		for i in range(N, -1, -2):
			if i == 1:
				break
			F[i-2] = max(F[i]+H[i], F[i]+H[i-1], F[i]+L[i]+L[i-1])

		if i == 1:
			F[0] = F[1] + max(L[1], H[1])
		print(str(F[0]))

if __name__ == "__main__":
	t = Solution()
	t.maxVal()


#### 2020 系统开发
# T3
# 相邻石堆合并，累计和最小
# 区间DP
class Solution:
	def minCost(self):
		# input
		N = int(input())
		arr = list(map(int, input().split()))
		cost = 0
		
		# merge
		while len(arr) > 1:
			curMin = float("inf")
			index = 0
			for i in range(len(arr)-1):
				if arr[i] + arr[i+1] <= curMin:
					curMin = arr[i] + arr[i+1]
					index = i
			cost += curMin
			arr[index] = curMin
			del(arr[index+1])
		
		print(str(cost))

if __name__ == "__main__":
	t = Solution()
	t.minCost()


# T4
# 字符串集最小前缀
# Version0
# 字符串排序后比较
'''
class Solution:
	def uniquePrefix(self):
		# input
		N = int(input())
		arr = []
		for i in range(N):
			arr.append(input())
		
		# prefixarr copy
		prefixArr = arr.copy()
		prefixArr.sort()
		# build index dict
		indexDict = {}
		for i in range(N):
			indexDict[prefixArr[i]] = i

		#* prefixarr update
		for i in range(N-1):
			for end in range(len(arr[i])):
				if prefixArr[i][end] != prefixArr[i+1][end]:
					prefixArr[i] = prefixArr[i][:end+1]
					break

		for end in range(len(prefixArr[-2])):
			if prefixArr[-2][end] != prefixArr[-1][end]:
				prefixArr[-1] = prefixArr[-1][:end+1]
				break
			if end == len(prefixArr[-2])-1:
				prefixArr[-1] = prefixArr[-1][:end+2]

		# res output
		for i in range(N):
			print(prefixArr[indexDict[arr[i]]])
'''


# Version1
# 维护前缀树(字典树)
class Solution:
	def __init__(self):
		self.pretree = {}
	def inset(self, string):
		# 浅拷贝变量，任何改变会累计到原始变量上
		tmp = self.pretree
		for char in string:
			if char not in tmp:
				tmp[char] = {}
			tmp = tmp[char]
	def core(self, string):
		tmp = self.pretree
		res = ""
		for char in string:
			if char in tmp:
				res += char
				tmp = tmp[char]
			else:
				res += char
				return res
		return res

# main
N = int(input())
strings = []
res = []
for i in range(N):
	strings.append(input())
for string in strings:
	a = Solution()
	for string_else in strings:
		if string == string_else:
			continue
		a.inset(string_else)
	res.append(a.core(string))
for x in res:
	print(x)
