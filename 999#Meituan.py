# 2020实习春招
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
# T7
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


# T6
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

# T4
import sys
from functools import lru_cache

sys.setrecursionlimit(10000000)

class Solution:

    def maxScore(self):
        # input
        #N = int(input())
        #arr = [list(map(int, input().split())) for _ in range(N)]
        N = 3
        arr = [[1.08, 1.25, 1.5], [1.5, 1.35, 1.75], [1.22, 1.48, 2.5]]
        vis = []

        #@lru_cache(None)
        def DFS(vis, node):
            level = len(vis)
            if level == N:
                return [0, [vis.pop()]]

            # init
            vis.append(node)
            partRes = 0
            solution = []
            for i in range(N):
                if i not in vis:
                    tmpRes, tmpSolution = DFS(vis, i)
                    if tmpRes > partRes:
                        partRes = tmpRes
                        solution = tmpSolution
            if level > 0:
                partRes += arr[level-1][node]
            return [partRes, solution.insert(0,node)]

        res, callList = DFS(vis, None)

        return [res, callList]

if __name__ == "__main__":
    t = Solution()
    res, callList = t.maxScore()
    print('%.2f' %res)
    for i in range(len(callList)):
        print(" ".join([str(i), str(callList[i])]))


# T12
# 火星文字母排序



# T13
# 无环图的最小遍历步数
# Version0 
# Not pass
	N = int(input())
	graph = dict()
	for i in range(N-1):
	    x, y = map(int, input().split())
	    if x not in graph:
	        graph[x] = [y]
	    else:
	        graph[x].append(y)
	    if y not in graph:
	        graph[y] = [x]
	    else:
	        graph[y].append(x)

	# init
	candid = []
	for i in graph.keys():
	    if len(graph[i]) == 1:
	        candid.append(i)

	# BFS
	for start in candid:
	    queue = [[{start}, start, 0]]
	    res = float('inf')
	    while queue:
	        vis, node, cnt = queue.pop()
	        if len(vis) == N:
	            res = min(res, cnt)
	            break
	        # 会往返叠堆同一对节点造成死循环
	        for nextNode in graph[node]:
	            newVis = vis.copy()
	            newVis.add(nextNode)
	            queue.append([newVis, nextNode, cnt+1])

	print(res)

# Version1
from collections import defaultdict

def minSteps():
    # input
    N = int(input())
    d = defaultdict(list)
    for i in range(N-1):
        a, b = map(int, input().split())
        d[a].append(b)
        d[b].append(a)

    # init
    queue = [1]
    visited = defaultdict(bool)
    visited[1] = True
    maxPath = 0

    # BFS
    while queue:
        tmp = []
        while queue:
            node = queue.pop()
            for nextNode in d[node]:
                if not visited[nextNode]:
                    visited[nextNode] = True
                    tmp.append(nextNode)    # 使用额外变量储存新一层的点，避免混淆
        queue = tmp
        maxPath += 1
    print(2*(N-1) - maxPath + 1)
    
minSteps()


# T14
# 01字符串k位补零的最大连续1位
# Version0
# 60%

def maxConseOne():
    # input
    N, k = list(map(int, input().split()))
    s = list(map(int, input().split()))

    # init
    N = len(s)
    seq = []
    res = 0
    l = -1
    for r in range(N):
        if s[r] == 0:
            seq.append(r-l-1)
            l = r
        if r == N-1:
            if s[r] != 0:
                seq.append(r-l)
            if s[r] == 0:
                seq.append(0)

    if seq is None:
        return N

    # windows
    Nseq = len(seq) - 1   # 0 的数量
    if Nseq <= k:
        return N

    for l in range(1, Nseq-k+1):
        r = l+k-1
        res = max(res, sum(seq[l-1:r+1])+k)

    return res

res = maxConseOne()
print(res)

# Version1
# 维护最多填补k个0的滑动窗口
# input
N, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
#init
l, r = 0, 0
res = 0
while r < N:
	if arr[r] == 1:
		r += 1
	# arr[r] = 0 的情况
	elif k > 0:
		k -= 1
		r += 1
	# k 为0的情况，右指针不能再右移，开始移动左指针
	else:
		res = max(res, r-l)
		# l为1的情况
		while arr[l] == 1:
			l += 1
		# l跳过一个0，跨过左端一个连续区间，r开始移动一个连续区间
		l += 1
		r += 1
res = max(res, r-l)
print(res)


# T15
# 似乎能用单调栈
# 划分山峰与山谷数组后再使用分治
# Version0 
# 部分AC
N = int(input())
arr = list(map(int, input().split()))


# 高程图两端一定以山峰结束，状态1表上升，2表下降
if N == 1:
    print(N)

# init
nums = []
state = 0
for i in range(1, N):
    if state == 0 and arr[i] > arr[0]:
        state = 1
        continue
    elif state == 0 and arr[i] < arr[0]:
        state = 2
        continue

    # up
    if state == 1 and arr[i] >= arr[i-1]:
        continue
    # down
    elif state == 2 and arr[i] <= arr[i-1]:
        continue
    # heap
    elif state == 1 and arr[i] < arr[i-1]:
        nums.append(arr[i-1])
        state = 2
        continue
    # valley
    elif state == 2 and arr[i] > arr[i-1]:
        nums.append(arr[i-1])
        state = 1
        continue

if nums[0] != arr[0]:
    nums.insert(0, arr[0])
if nums[-1] != arr[-1]:
    nums.append(arr[-1])

def divideSum(nums):
    if not nums:
        return 0
    Nnode = len(nums)
    least = nums[0]

    # find min valley
    for i in range(1, Nnode):
        if nums[i] < least:
            least = nums[i]

    cnt = least
    left = 0
    # recurse cnt
    for i in range(Nnode):
        nums[i] -= least
        if nums[i] == 0:
            cnt += divideSum(nums[left:i])
            left = i+1
    if nums[Nnode-1] != 0:
        cnt += divideSum(nums[left:Nnode])

    return cnt

# main
# 单调栈
# TC:O(N), SC:O(1)
if len(nums) <= 2:          
    res = max(nums)
else:
    res = divideSum(nums)
print(res)

# Version1
def minPlant():
    N = int(input())
    nums = list(map(int, input().split()))

    # init
    stack = []
    res = 0

    if N == 1:
        return nums[0]

    for i in range(1, N):
        if nums[i] >= nums[i-1]:
            continue
        else:
            res += nums[i-1] - nums[i]
    res += nums[-1]
    return res

print(minPlant())


# T16 路由器覆盖信号
# 差分问题
# input
N, K = list(map(int, input().split()))
arr = list(map(int, input().split()))

# init
res = 0
dp = [0 for _ in range(N+1)]    # N+1元素是暂存多余的右边界，防止信号提前中断
for i in range(N):
    # left edge
    left = max(0, i - arr[i])
    dp[left] += 1
    # right edge
    right = min(N, i + arr[i] + 1)
    dp[right] -= 1

# accsum
tmp = 0
for i in range(N):
    tmp += dp[i]
    if tmp >= K:
        res += 1
print(res)


# T8 布尔表达式判定
# 分类讨论
def boolExp():
    # input
    s = input().split()
    N = len(s)

    if N % 2 == 0:
        return "error"

    # init
    stack = []
    tmp = True
    for i in range(N):

        if i % 2 == 1 and s[i] not in ["and", "or"]:
            return "error"
        elif i % 2 == 0 and s[i] not in ["true", "false"]:
            return "error"

        if s[i] == "true":
            tmp &= True
        elif s[i] == "false":
            tmp &= False
        elif s[i] == "and":
            continue
        elif s[i] == "or":
            stack.append(tmp)
            tmp = True

        if i == N-1:
            stack.append(tmp)

    # or operation
    res = None
    res = stack.pop()
    while stack:
        res |= stack.pop()

    if res:
        return "true"
    else:
        return "false"

print(boolExp())

