# 26'
class LRUCache:

	def __init__(self, capacity: int):
		self.capacity = capacity
		self.key = []
		self.value = []
		self.len = 0

	def get(self, key: int) -> int:
		pos = 0
		if key in self.key:
			pos = self.key.index(key)
			self.value.append(self.value[pos])
			self.key.append(key)
			del self.key[pos]
			del self.value[pos]
			return self.value[-1]
		else:
			return -1

	def put(self, key: int, value: int) -> None:
		pos = 0
		if self.len == self.capacity:
			del self.key[0]
			del self.value[0]
			self.key.append(key)
			self.value.append(value)
		else:
			self.len += 1
			if key in self.key:
				pos = self.key.index(key)
				del self.key[pos]
				del self.value[pos]
			self.value.append(self.value[pos])
			self.key.append(key)
			
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)