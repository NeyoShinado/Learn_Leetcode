# 19'
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
	def detectCycle(self, head: ListNode) -> ListNode:
		# init
		map = []
		res = None
		pos = 0

		if head:
			if head.next:
				node = head
			else:
				return res
		else:
			return res

		while node:
			if node in map:
				res = node
				return res
			else:
				if node.next:
					map.append(node)
					node = node.next
				
		return res