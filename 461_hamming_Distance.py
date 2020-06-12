'''
# Version 0
# TC: O(1), SC: O(N)
class Solution:
	def hammingDistance(self, x:int, y: int) -> int:
		# init
		res = 0
		xstr = bin(x)[2:]
		ystr = bin(y)[2:]

		Nx = len(xstr)
		Ny = len(ystr)

		if Nx > Ny:
			ystr = '0' * (Nx-Ny) + ystr
		else:
			xstr = '0' * (Ny-Nx) + xstr

		for i in range(len(xstr)):
			res += abs(int(xstr[i]) - int(ystr[i]))

		return res


# Version 1
# 内置函数
class Solution:
	sef hamingDistance(self, x, y):
	return bin(x ^ y).count('1')


# Version 2
# 逻辑移位
# TC: O(1), SC: O(1)
class Solution:
	def hamingDistance(self, x, y):
		xor = x ^ y
		distance = 0
		while xor:
			if xor & 1:    # 使用& 或取模运算检查最右位是否为1
				distance += 1
			xor = xor >> 1
		return distance
'''


# Version 3
# ⭐布莱恩.尼克根算法
# 逐位移动效率较低，尼克根算法跳过1之间的0，直接数边缘位置的1
# num & num-1 能达到上述效果，一次移除最右位1
# 方法二
class Solution:
	def hamingDistance(self, x, y):
		xor = x ^ y
		distance = 0
		while xor:
			distance += 1
			xor = xor & (xor - 1)
		return