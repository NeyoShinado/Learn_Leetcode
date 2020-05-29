# 10'
# Version1
'''
class MinStack:

	def __init__(self):
		"""
		initialize your data structure here.
		"""
		self.min = None
		self.stack = []


	def push(self, x: int) -> None:
		self.stack.append(x)
		if self.min:
			self.min = min(self.min, x)
		else:
			self.min = x

	def pop(self) -> None:
		res = self.stack.pop()
		if self.min == res:
			if self.stack:
				self.min = min(self.stack)
			else:
				self.min = None

	def top(self) -> int:
		res = self.stack[-1]

		return res

	def getMin(self) -> int:
		return self.min
'''

'''
# Version2
# 使用辅助栈记录最小值信息
# 辅助栈和数据栈同步，同步出入，但辅助栈需要多余空间
# TC: O(1), SC: O(N)
class MinStack:
	def __init__(self):
		self.data = []
		self.helper = []
	def push(self, x):
		self.data.append(x)
		if len(self.helper) == 0 or x <= self.helper[-1]:
			self.helper.append(x)
		else:
			self.helper.append(self.helper[-1])

	def pop(self):
		if self.data:
			self.helper.pop()
			return self.data.pop()

	def top(self):
		if self.data:
			return self.data[-1]

	def getMin(self):
		if self.helper:
			return self.helper[-1]
'''

# Version3
# 数据栈和辅助栈不同步
# 入栈时，相同或者较小值辅助栈才同步进栈；出栈时相同元素辅助栈才同步出栈
# 不同步能节省掉存储大值的空间，但是进出操作也慢了些；同时调试定位问题也更复杂
class MinStack:
	def __init__(self):
		self.data = []
		self.helper = []

	def push(self, x):
		self.data.append(x)
		if len(self.helper) == 0 or x <= self.helper[-1]:
			self.helper.append(x)

	def pop(self):
		top = self.data.pop()
		if self.helper and top == self.helper[-1]:
			self.helper.pop()
		return top

	def top(self):
		if self.data:
			return self.data[-1]

	def getMin(self):
		if self.helper:
			return self.helper[-1]
