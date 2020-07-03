'''
# Version 1
# 布莱恩算法循环计数
# TC: O(Nk), SC: O(N)
class Solution:
	def countBits(self, num):
		res = []
		for i in range(num+1):
			res.append(popcount(i))
		return res

def popcount(x):
	cnt = 0
	while x != 0:
		cnt += 1
		x = x & x-1
	return cnt
'''


'''
# Version 2
# 动态规划 + 最高有效位
# TC: O(N), SC: O(N)
# 通过列表直接复制的方式，2次方速度完成赋值，可能能达到TC: O(log2N)
#!二进制数二等分可发现除最高位外低位都相同，popcount相差1
# 转移方程 P(x+b) = P(x) + 1, b=2^m恰大于x 的规律
class Solution:
	def countBits(self, num):
		###
		res = [0]
		i = 0
		b = 1
		while b <= num:
			for i in range(len(res)):
				if i+b > num:
					return res
				res.append(res[i] + 1)
			b << 1
		return res
		###
		res = [0] * (num+1)
		i = 0
		b = 1
		while b <= num:
			while i < b and (i+b) <= num:
				res[i+b] = res[i] + 1
				i += 1
			i = 0
			b << 1
		return res
'''


'''
# Version 3
# 动态规划 + 最低有效位
#!同样，除去最低有效位，高位相同的值popcount也只相差1
# 转移方程 P(x) = P(x//2) + (x % 2)
# TC: O(N), SC: O(N)
class Solution:
	def countBits(self, num):
		res = [0] * (num+1)
		for i in range(1, num+1):
			res[i] = res[i >> 1] + (i & 1)
		return res
'''


# Version 4
# 动态规划 + 最后设置位
#!最后设置位是从右至左的第一位1，该位为0的数肯定比该数小(可调用) 
# 且popcount相差1
# 转移方程 P(x) = P(x & (x-1)) + 1
# TC: O(N), SC: O(N)
class Solution:
	def countBits(self, num):
		res = [0] * (num+1)
		for i in range(1, num+1):
			res[i] = res[i & (i-1)] + 1
		return res