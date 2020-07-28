'''
# Version 0
# 贪心算法，Not pass
# 每次戳乘积最大的那个气球
class Solution:
	def maxCoins(self, nums: List[int]) -> int:
		# init
		res = 0
		N = len(nums)
		map = []
		prod = 0 	# min product
		id = 0 		# index of min product

		if N == 0:
			return res
		elif N == 1:
			res = nums[0]
			return res

		# build pro map
		for i in range(N):
			if i == 0:
				map.append(nums[i] * nums[i+1])
			elif i == N-1:
				map.append(nums[i] * nums[i-1])
			else:
				map.append(nums[i] * nums[i+1] * nums[i-1])

		# choose max pro and update the map
		while map:
			N = len(nums)
			id = 0
			prod = 0
			for i in range(N):
				if prod < map[i]:
					prod = map[i]
					id = i
			res += prod
			if id > 0 and id < N-1:	# at least 3 nums
				map[id-1] = nums[id-1] * (nums[id-2] if id-2 >= 0 else 1) * nums[id+1]
				map[id+1] = nums[id+1] * (nums[id+2] if id+2 <= N-1 else 1) * nums[id-1]
				map.pop(id)
				nums.pop(id)
			elif id == 0:	# at least 1 nums
				if N >= 2:
					map[id+1] = nums[id+1] * (nums[id+2] if id+2 <= N-1 else 1)
				map.pop(id)
				nums.pop(id)
			elif id == N-1:		# at least 2 nums
				map[id-1] = nums[id-1] * (nums[id-2] if id-2 >= 0 else 1)
				map.pop(id)
				nums.pop(id)

		return res
'''


# Version 1
# 回溯算法暴力遍历所有路径
# TC: O(N^3) -- 缓存机制下只计算N^2区间数个递归函数一次，每次迭代复杂度为O(N)
# SC: O(N^2)
# 方案一使用数组作为递归函数的输入，正向模拟了戳气球的情景；
# 问题是列表是可变对象，python不知道缓存了哪些值；解决方法是将其转为不可变和可哈希的元组
# 方案二则使用下标作为输入以便使用缓存机制；其不同的地方还在于通过“加气球”逆向模拟戳气球过程，
# solve(l, r)为(l,r)区间内填满气球后最大的硬币数（通过限制i>=j-1使气球按顺序恢复--即正向的按顺序戳爆）
# 有转换方程solve(i,j)=max nums[i]*max[mid]*max[j]+solve(i,mid)+solve(mid,j)当前区间的最优解
'''
class Solution:
	def maxCoins(self, nums:List[int]) -> int:
		nums = [1] + nums
		nums.append(1)
		@lru_cache(None)  #*
		def helper(lst):
			if len(lst) == 3:
				return lst[1]
			mmax = 0   # 维护最大值
			for i in range(1, len(lst) - 1):
				tmp = lst[i-1] * lst[i] * lst[i+1]
				mmax = max(mmax, tmp+helper(lst[:i] + lst[i+1:]))
			return mmax
		return helper(nums)
'''
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        val = [1] + nums + [1]
        
        @lru_cache(None)
        # 函数输入参数为基本类型方可使用lru缓存机制
        def solve(left: int, right: int) -> int:
            if left >= right - 1:
                return 0
            
            best = 0
            for i in range(left + 1, right):
                total = val[left] * val[i] * val[right]
                total += solve(left, i) + solve(i, right)
                best = max(best, total)
            
            return best

        return solve(0, n + 1)

